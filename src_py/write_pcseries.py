import numpy as np
import os
import sys
import argparse
from netCDF4 import Dataset
import pandas as pd
import csv
from datetime import datetime, timedelta, date
from scipy import optimize

#file to project cover for input VOM
#and CO2 from Mauna Loa for applying it in
#the Vegetation Optimality Model (VOM)
#output: 
#pc.txt: input file VOM
#written: Aug 2019, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()


    parser.add_argument("-i", "--input_fpar", help="file with fpar-values")
    parser.add_argument("-id", "--input_fpardates", help="file with dates fpar-values")


    #parser.add_argument("-id", "--dailyweather", help="dailyweatherfile that needs updating")
    parser.add_argument("-p", "--interpolation", help="interpolation method for missing data",nargs='?',const='linear', default='linear')
    parser.add_argument("--meteofile", help="inputfile with meteodata of Silo")
    parser.add_argument("--co2file", help="inputfile with co2data of ManuaLoa")
    parser.add_argument("--var", help="variable to replace", nargs='+')
    parser.add_argument("-s", "--start", help="startdate")
    parser.add_argument("-e", "--end", help="enddate")
    parser.add_argument("-o", "--outputfile", help="outputfile")
    args = parser.parse_args()



    ########################################################
    #settings

    #dailyweather file
    dailyweather = args.dailyweather

    #meteo file
    meteofile = args.meteofile

    #CO2 file
    co2file = args.co2file 

    #interpolation method for missing data
    interp = args.interpolation

    #output folder
    out_file = args.outputfile

    ####################################
    #read data

    fpar = pd.read_csv(args.input_fpar, usecols=[3],  header=None, na_values=-999 )
    fpar_dates = np.genfromtxt(args.input_fpardates, dtype='str', delimiter=',')

    #make a pandas datetime series
    datetime_fpar = pd.to_datetime(fpar_dates[:,1], format="%Y%m")




    #make a pandas index
    index = pd.DatetimeIndex( datetime_fpar)

    #replace index
    fpar.index = index

    #fpar

    #make daily series
    fpar_daily = fpar.resample('D')   

    #fill values
    fpar = fpar.fillna(method = 'backfill')   # [ppm]

    index = fpar.index

    day_daily     = index.day
    month_daily   = index.month
    year_daily    = index.year

    if(args.start is None):
        args.start = index[0] 
    if(args.end is None):
        args.end = index[-1] 

    ####################################
    #fit a sinus through the data
    x_data = np.arange(0, len(fpar))
    params, params_covariance = optimize.curve_fit(fitfunc, x_data, fpar)
                                               


    #final months
    datetime_months = pd.date_range(args.start, args.end, freq='M')

    months_before = int((datetime_fpar[0] - datetime_months[0])/np.timedelta64(1,'M'))
    months_after = int((datetime_months[-1] - datetime_fpar[-1])/np.timedelta64(1,'M'))  

    #Apply to full length of timeseries
    xnew =np.concatenate( (np.arange(-months_before, 0),  x_data ,np.arange(x_data[-1]+1, x_data[-1] + months_after + 1)))

    #fit
    fit = fitfunc(xnew, params[0], params[1])
    

    #final dates
    datetime_extr = pd.date_range(args.start, args.end, freq='D')



    ####################################
    #read CO2 data

    if(co2file is not None):
        co2data = pd.read_csv(co2file, skiprows = 44, na_values = "    NaN", header=None)

        #make a pandas datetime series
        pddatetime = pd.to_datetime(co2data[0])

        #make a pandas index
        index2 = pd.DatetimeIndex( pddatetime)	

        #replace index
        co2data.index = index2

        #extract CO2 series
        co2mlo_pd = pd.Series(co2data[1], dtype = np.float64)

        #make daily series
        co2_daily = co2mlo_pd.resample('D')   # [ppm]

        #fill weekly values
        co2_daily = co2_daily.fillna(method = 'backfill')   # [ppm]


    ########################################################
    #read meteofile

    if(meteofile is not None):
        meteo_data = pd.read_csv(meteofile, skiprows = 43, delimiter=r"\s+", header=None )

        #make a pandas datetime series
        pddatetime = pd.to_datetime( meteo_data[2], format="%d-%m-%Y")

        #make a pandas index
        index = pd.DatetimeIndex( pddatetime)

        #replace index
        meteo_data.index = index

        #extract series
        if( "T.Max" in args.var):
            tempmax_daily = meteo_data[:][3] #oC
        if( "T.Min" in args.var):
            tempmin_daily = meteo_data[:][5] #oC
        if( "Rain" in args.var):
            prec_daily    = meteo_data[:][7] #mm/d
        if( "VP" in args.var):
            vp_daily      = meteo_data[:][13]#hPa
        if( "Radn" in args.var):
            radn_daily    = meteo_data[:][11]#MJ/m2
        if( "Pres" in args.var):
            pres_daily    = meteo_data[:][26]#hPa

        day_daily     = index.day
        month_daily   = index.month
        year_daily    = index.year



    ##################################################
    #append to files

    #file for weather data, input VOM
    weatherfile = open(out_file, mode = 'w')

    #write header
    weatherfile.write("%8s%8s%8s%8s%8s%8s%8s%8s%8s%8s%8s\n" %
        ("Dcum","Day","Month", "Year", "T.Max", "T.Min", "Rain", "Radn", "VP", "Pres", "Ca" ))

    #print(tempmax_daily[0:70])

    for i in range(0,len(day_daily)):
        if( (index[i] >= pd.to_datetime(args.start))  & (index[i] <= pd.to_datetime(args.end)) ):
            weatherfile.write("%8.0f%8.0f%8.0f%8.0f%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f\n" % ( i+1 , 
            day_daily[i] , 
            month_daily[i] ,
            year_daily[i] ,
            tempmax_daily[tempmax_daily.index == index[i]] ,    
            tempmin_daily[tempmin_daily.index == index[i]] ,    
            prec_daily[prec_daily.index == index[i]] ,    
            radn_daily[radn_daily.index == index[i]] ,    
            vp_daily[vp_daily.index == index[i]] ,    
            pres_daily[pres_daily.index == index[i]] ,    
            co2_daily[co2_daily.index== index[i] ] ))



    weatherfile.close()

    print("Script finished")


def fitfunc(x, a, b, c, d):
    return a + b * np.sin(c * x + d) 

main()









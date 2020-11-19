import os
import sys
import argparse
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date

#Create benchmarking dataset following Whitley et al. (2016) and Abramowitz et al. (2012)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--inputfile", help="input to use with regression model")
    parser.add_argument("-ix", "--x_regression", help="inputfiles for x-values regression", nargs='+')
    parser.add_argument("-iy", "--y_regression", help="inputfiles for y-values regression", nargs='+')
    parser.add_argument("-v", "--var", help="variables used for regression", nargs='+')
    parser.add_argument("-o", "--outputfile", help="outputfile with predicted y-values")
    args = parser.parse_args()

    #########################################################################
    #simple linear regression

    #get turbulent flux (LE or GPP)
    y = np.array([])
    y_dates = []

    #get downward shortwave radiation (RS) of multiple sites for regression
    x = np.array([])
    x_all = np.array([len(args.var)])
    x_dates = []

    i = 0
    for file in args.x_regression:

        meteo_data = pd.read_csv(file, skiprows = 43, delimiter=r"\s+", header=None )

        #make a pandas datetime series
        pddatetime = pd.to_datetime( meteo_data[2], format="%d-%m-%Y")

        #make a pandas index
        index = pd.DatetimeIndex( pddatetime)

        #replace index
        meteo_data.index = index     

        #load values for y
        tmp_y = np.loadtxt(args.y_regression[i], usecols=2)
        ydates_tmp = np.genfromtxt(args.y_regression[i],usecols=0, dtype=np.str )#mm/d
        ydates_tmp = pd.date_range(ydates_tmp[0], ydates_tmp[-1], freq='D') 
        
        #make pandas series
        y_series = pd.Series(tmp_y, index=ydates_tmp)        

        #determine overlapping dates
        dates_overlap = meteo_data.index.intersection(ydates_tmp)

        var = np.array([])
        for ivar in range(0, len(args.var)):
            if( args.var[ivar] == "Radn"):
                ind = 11
                var = np.array(meteo_data[:][ind])
            if( args.var[ivar] == "VPD"):
                ind = 13
                var = np.column_stack( (var, np.array(meteo_data[:][ind]) ))
            if( args.var[ivar] == "Temp"):
                ind = 3

        #make series
        x_series = pd.DataFrame(var, index=index) 

        #append the data
        if(i == 0):
            x = x_series.loc[dates_overlap]
        else:
            x = np.append(x, x_series.loc[dates_overlap], axis=0 )
      
        
        y = np.append(y, y_series[dates_overlap] )

        #append the dates as well
        x_dates.append(dates_overlap)
        y_dates.append(ydates_tmp)

        i = i + 1


    #get data to apply model flux (LE or GPP)
    x_val = np.array([])
    dates_val = np.array([])

    meteo_data = pd.read_csv(args.inputfile, skiprows = 43, delimiter=r"\s+", header=None )

    #make a pandas datetime series
    pddatetime = pd.to_datetime( meteo_data[2], format="%d-%m-%Y")

    #make a pandas index
    index = pd.DatetimeIndex( pddatetime)

    #replace index
    meteo_data.index = index

    var = np.array([])
    for ivar in range(0, len(args.var)):
        if( args.var[ivar] == "Radn"):
            if(ivar == 0):
                var = np.array(meteo_data[:][11])
            else:
                var = np.column_stack( (var, np.array(meteo_data[:][ind]) ))
        if( args.var[ivar] == "VPD"):
            if(ivar == 0):

                Tmean =np.array((meteo_data[:][5] + meteo_data[:][3])/2.0)

                Vsat = 0.6108*np.exp( 17.27*Tmean/(Tmean+237.3) ) #kPa
                Vact = meteo_data[:][13]*0.1 #kPa

                var = Vsat - Vact
            else:
                Tmean =np.array((meteo_data[:][5] + meteo_data[:][3])/2.0)

                Vsat = 0.6108*np.exp( 17.27*Tmean/(Tmean+237.3) ) #kPa
                Vact = meteo_data[:][13]*0.1 #kPa

                tmp = Vsat - Vact
                var = np.column_stack( (var, tmp) )
        if( args.var[ivar] == "Temp"):
            if(ivar == 0):
                var =np.array((meteo_data[:][5] + meteo_data[:][3])/2.0)
            else:
                tmp =np.array((meteo_data[:][5] + meteo_data[:][3])/2.0)
                var = np.column_stack( (var, tmp) )

    #make series
    x_val_series = pd.DataFrame(var, index=index) 

    #simple linear regression between RS and turbulent flux (emp1)
    model = sm.OLS(y, x).fit()

    #x_val = sm.add_constant(x_val)
    y_pred = model.predict(x_val_series)

    print(model.summary())

    ####################################
    #file for weather data, input VOM
    out_file = open(args.outputfile, mode = 'w')


    for i in range(0,len(y_pred)):
        out_file.write("%8.0f%8.0f%8.0f%8.0f%8.3f\n" % ( i, 
        x_val_series.index.day[i] , 
        x_val_series.index.month[i] ,
        x_val_series.index.year[i],
        y_pred[i]  ))



    out_file.close()

 
 
main()

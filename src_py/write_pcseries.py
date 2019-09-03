import numpy as np
import os
import sys
import argparse
from netCDF4 import Dataset
import pandas as pd
import csv
from datetime import datetime, timedelta, date
from scipy import optimize
import matplotlib.pyplot as plt

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
    parser.add_argument("-s", "--start", help="startdate")
    parser.add_argument("-e", "--end", help="enddate")
    parser.add_argument("-o", "--outputfile", help="outputfile")
    parser.add_argument("--plot", type=bool, help="outputfile", default=False)

    args = parser.parse_args()

    ####################################
    #read data

    fpar = pd.read_csv(args.input_fpar, usecols=[3],  header=None, na_values=-999, squeeze=True )
    fpar_dates = np.genfromtxt(args.input_fpardates, dtype='str', delimiter=',')

    #make a pandas datetime series
    datetime_fpar = pd.to_datetime(fpar_dates[:,1], format="%Y%m")

    #make a pandas index
    index = pd.DatetimeIndex( datetime_fpar)

    #replace index
    fpar.index = index

    #make daily series
    #fpar_daily = fpar.resample('D').ffill()

    #calculate means per month
    means=np.zeros((12))

    for i_month in np.arange(0,12):
        month = i_month + 1
        means[i_month] = np.nanmean(fpar[fpar.index.month == month] )


    #final months
    datetime_result = pd.DatetimeIndex(start=args.start, end=args.end, freq='D')
    fpar_result = pd.Series( np.nan ,index=datetime_result)

    fpar_result[fpar.index] = fpar

    for i in range(0,len(fpar_result)):
        if( np.isnan(fpar_result[ i ])):
            month = fpar_result.index.month[i]
            year = fpar_result.index.year[i]
            i_month = fpar_result.index.month[i]-1
            if(  any(~(np.isnan(fpar_result[ (fpar_result.index.month ==month) & (fpar_result.index.year == year)] )))):
                fpar_result[i] = np.nanmean(fpar_result[ (fpar_result.index.month ==month) & (fpar_result.index.year == year)])
            else:
                fpar_result[ i ] = means[ i_month ]

    ###################################
    #convert to projective cover
    pc_result = fpar_result/0.95

    ####################################
    #plot

    if(args.plot):
        fpar_result.plot()
        fpar.plot()
        #fpar_daily.plot()
        plt.show()


    ####################################
    #file for weather data, input VOM
    pc_file = open(args.outputfile, mode = 'w')


    for i in range(0,len(fpar_result)):
        pc_file.write("%8.0f%8.0f%8.0f%8.0f%8.3f\n" % ( i, 
        pc_result.index.day[i] , 
        pc_result.index.month[i] ,
        pc_result.index.year[i],
        pc_result[i]  ))



    pc_file.close()

    print("Script finished")



main()









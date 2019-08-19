import numpy as np
import os
from netCDF4 import Dataset
import pandas as pd
import sys
import argparse

#file to prepare data from the OzFlux tower sites for the 
#Vegetation Optimality Model (VOM)
#output: 
#dailyweather.prn: input file VOM
#ea.txt: timeseries of evaporation in mm/d
#co2up.txt: timeseries of CO2 uptake in mol/m2/d
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()


    parser.add_argument("--vpdfile", help="vpdfile")
    parser.add_argument("--tempfile", help="mean temperature file")
    parser.add_argument("-o", "--outputfile", help="outputfolder")

    args = parser.parse_args()


    ########################################################
    #open files for writing

    vpd = read_dingodata(args.vpdfile) #kPa
    temp = read_dingodata(args.tempfile) #oC

    vp = (0.61*np.exp(17.27*temp/(temp+237.3)) - vpd ) * 10 #hPa


    ##################################################
    #append to files
    #file for output data, for comparison output
    outfile_file = open(args.outputfile, mode = 'w')

    for i in range(0, len(vp.index)):
        outfile_file.write( "%20s%30s\n" % (vp.index[i], vp[i] ))



    print("Script finished")


def read_dingodata(dingofile ):

    ########################################################
    #read file

    data = pd.read_csv(dingofile, skiprows = 0, delimiter=r"\s+", header=None )

    #make a pandas datetime series
    pddatetime = pd.to_datetime( data[0], format="%Y-%m-%d")

    #make a pandas index
    index = pd.DatetimeIndex( pddatetime)

    #replace index
    data.index = index

    #extract series

    var_daily = data[:][2] 

    return var_daily

main()



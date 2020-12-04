#!/usr/bin/env python
# coding: utf-8

#***********************************************************************
#        plot_ensembleyears.py
#        Plots VOM-results and results of Whitley et al. (2016) as ensemble years. 
#        
#-----------------------------------------------------------------------
#        Authors: Remko Nijzink
#        Now at: LIST (Luxembourg Institute of Science and Technology)
#-----------------------------------------------------------------------
#
#  Copyright (C) 2020 LIST (Luxembourg Institute of Science and Technology), all right reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#***********************************************************************


import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date
from matplotlib.pyplot import imread
import matplotlib.cbook as cbook
from netCDF4 import Dataset,num2date
import argparse

def main():

    parser = argparse.ArgumentParser(description="Plots VOM-results and results of Whitley et al. (2016) as ensemble years.")

    parser.add_argument("-o", "--outfile", help="outputfile with plot")
    parser.add_argument("-i", "--inputfiles", help="VOM results", nargs='+')

    parser.set_defaults(tight_layout=False, plot_et = True,sharex = False)

    args = parser.parse_args()


    for i in range(0, len(args.inputfiles)):


            #read in data from CABLE, ET in kg/m^2/s, GPP in umol/m^2/s
            AP, west, east, south, north  = read_nc(args.inputfiles[i])

            if(i == 0):
                MAP = (1/len(args.inputfiles)) * AP 
            else:
                MAP = (1/len(args.inputfiles)) * AP + MAP
            
    #write ascii grid
    file = open(args.outfile,"w") 
    file.write("cols {0:d} \n".format( MAP.shape[1]))
    file.write("rows {0:d} \n".format( MAP.shape[0])  )
    file.write("east {0:.2f} \n".format( east)  )
    file.write("south {0:.2f} \n".format( south)  )
    file.write("north {0:.2f} \n".format( north)  )
    file.write("west {0:.2f} \n".format( west)  )
    file.write("NULL nan \n")
    np.savetxt(file, MAP)
    file.close



def read_nc(infile):
    ncfile = Dataset(infile)
    data = np.squeeze(ncfile.variables["monthly_rain"]) # extract variable
    lon = np.squeeze(ncfile.variables["lon"]) # extract variable
    lat = np.squeeze(ncfile.variables["lat"]) # extract variable
    #cellsize = lon[1]-lon[0]

    data[data<0]=np.nan

    AnnPrec = np.sum(data,0)

    return AnnPrec, lon[-1], lon[0], lat[-1],lat[0]


main()

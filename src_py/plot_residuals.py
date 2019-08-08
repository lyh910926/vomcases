import os
import sys
import argparse
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date

#Rsquared between observed and modelled data


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-ie", "--input_evap", help="number of parameters", nargs='+')             
    parser.add_argument("-iass", "--input_ass", help="number of parameters", nargs='+')
    parser.add_argument("-id", "--datesfile", help="inputfile with overlapping dates", nargs='+')             
    parser.add_argument("-l", "--labels", help="labels for timeseries", nargs='+')             
    parser.add_argument("-o", "--outputfile", help="outputfile")
    args = parser.parse_args()

    colors = [ 'black', 'darkblue', 'blue', 'lightblue', 'lavender'   ]

    fig=plt.figure(figsize=(16, 5), dpi= 80, facecolor='w', edgecolor='k', )
    fig, ((ax0, ax1))  = plt.subplots(nrows=2, ncols=1, figsize=(14, 10)) 

    #loop over input-files
    for ibasin in  range(0, len(args.input_evap) ):  

        #plot evaporation residuals        

        #load residuals
        res_tmp = np.loadtxt(args.input_evap[ibasin])

        #load dates
        dates_overlap = np.loadtxt( args.datesfile[ibasin] ) #mm/d
        tm_overlap = pd.date_range(datetime(int(dates_overlap[0,2]),int(dates_overlap[0,1]),int(dates_overlap[0,0])), 
                      datetime(int(dates_overlap[-1,2]),int(dates_overlap[-1,1]),int(dates_overlap[-1,0])), 
                      freq='D'  )
        for iday in range(0,366):
            tmp = res_tmp[0,0:len(tm_overlap.dayofyear)]
            ax0.plot(tm_overlap.dayofyear[iday], np.mean(tmp[tm_overlap.dayofyear == tm_overlap.dayofyear[iday]]), '+', color = colors[ibasin], markersize=10)
        ax0.set_ylim([ -3, 3 ])
        ax0.plot([0,366],[0,0], '--', color='black')
        ax0.set_xlim([ 0, 367 ])         
        ax0.set_ylabel(r'Residuals Et ( $\sigma_{ET} $  )', size=18  )
        ax0.set_xlabel('DOY' , size=18   )
        
        for tick in ax0.xaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        for tick in ax0.yaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        ax0.legend(prop={'size':15})        
        ax0.legend()

        #plot assimilation residuals

        #load residuals
        res_tmp = np.loadtxt(args.input_ass[ibasin])

        #load dates
        dates_overlap = np.loadtxt( args.datesfile[ibasin] ) #mm/d
        tm_overlap = pd.date_range(datetime(int(dates_overlap[0,2]),int(dates_overlap[0,1]),int(dates_overlap[0,0])), 
                      datetime(int(dates_overlap[-1,2]),int(dates_overlap[-1,1]),int(dates_overlap[-1,0])), 
                      freq='D'  )
        ax1.plot(tm_overlap.dayofyear[0], np.mean(tmp[tm_overlap.dayofyear == tm_overlap.dayofyear[0]]), '+', color = colors[ibasin], label=args.labels[ibasin], markersize=10)

        for iday in range(1,366):
            tmp = res_tmp[0,0:len(tm_overlap.dayofyear)]
            ax1.plot(tm_overlap.dayofyear[iday], np.mean(tmp[tm_overlap.dayofyear == tm_overlap.dayofyear[iday]]), '+', color = colors[ibasin], markersize=10)

        ax1.plot([0,367],[0,0], '--', color='black')
        ax1.set_ylim([ -3, 3 ])  
        ax1.set_xlim([ 0, 366 ])          
        ax1.set_ylabel(r'Residuals CO2 uptake ($\sigma_{GPP} $ )', size=18  )
        ax1.set_xlabel('DOY' , size=18   )
        
        for tick in ax1.xaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        for tick in ax1.yaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        ax1.legend(prop={'size':15})

    plt.tight_layout()
    plt.savefig(args.outputfile)


 
main()

import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date


#file to prepare data from the OzFlux tower sites for the 
#Vegetation Optimality Model (VOM)
#output: 
#dailyweather.prn: input file VOM
#ea.txt: timeseries of evaporation in mm/d
#co2up.txt: timeseries of CO2 uptake in mol/m2/d
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-m1", "--maxmod", help="outputfile max-values")
    parser.add_argument("-m2", "--minmod", help="outputfile min-values")
    parser.add_argument("-m3", "--modisdata", help="observations from modis")
    parser.add_argument("-d", "--modisdates", help="dates observations from modis")
    parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-w", "--weather", help="dailyweather.prn")
    parser.add_argument("-o", "--outputfile", help="outputfile")

    args = parser.parse_args()

    modisdata = np.loadtxt(args.modisdata)

    modis_dates = np.genfromtxt(args.modisdates, dtype='str')
    modis_dates = pd.to_datetime(modis_dates)

    pcmax = np.loadtxt( args.maxmod )
    pcmin = np.loadtxt( args.minmod )
    
    weatherdata = np.loadtxt(args.weather, skiprows=1 )
    tm = np.arange(datetime(int(weatherdata[0,3]),int(weatherdata[0,2]),int(weatherdata[0,1])), 
                  datetime(int(weatherdata[-1,3]),int(weatherdata[-1,2]),int(weatherdata[-1,1])), 
                  timedelta(days=1)).astype(datetime)

    fig=plt.figure(figsize=(16, 5), dpi= 80, facecolor='w', edgecolor='k')
    fig, ax0,   = plt.subplots(nrows=1, ncols=1, figsize=(16, 5))    
    
    ax0.fill_between(tm[0:len(pcmax)], pcmax*100,  pcmin*100, facecolor='red', color = 'red', label='mod') #basin-scale
    
    #replace missing data with the mean
    modisdata[modisdata < 0] = np.mean(modisdata)
    
    ax0.plot(modis_dates, 100* (modisdata - min(modisdata))/(max(modisdata)-min(modisdata)), color='green', label= 'MODIS EVI Norm.')

    ax0.set_xlim([datetime(args.yearstart,1, 1), datetime( args.yearend ,12, 31)])  
    ax0.set_ylim([0, 100])    
    ax0.legend()
    
    ax0.set_ylabel('Perc. Cov. (%)', size=24  )
    
    for tick in ax0.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax0.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    ax0.legend(prop={'size':15})
   

    plt.tight_layout()
    plt.savefig(args.outputfile)

    print("Script finished")


main()



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
    #parser.add_argument("-e1", "--emp1", help="empirical soultion 1")
    #parser.add_argument("-e2", "--emp2", help="empirical soultion 2")
    parser.add_argument("-ob", "--obs", help="observations")
    parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-w", "--weather", help="dailyweather.prn")
    parser.add_argument("-b", "--best", help="best results")
    parser.add_argument("-v", "--var", help="assimilation or evaporation")
    parser.add_argument("-o", "--outputfile", help="outputfile")

    args = parser.parse_args()

    #years to plot
    yearstart = args.yearstart
    yearend = args.yearend

    #get benchmark
    #emp1 = np.genfromtxt(args.emp1, usecols=1, dtype=np.float)
    #emp2 = np.genfromtxt(args.emp2, usecols=1, dtype=np.float)
    #t_emp = np.genfromtxt( args.emp1, usecols=0, dtype=np.str)
    #t_emp = pd.date_range(t_emp[0], t_emp[-1], freq='D')    

    #load max and min of model runs
    max_mod = np.loadtxt(args.maxmod)
    min_mod = np.loadtxt(args.minmod)

    #load best results
    best_data = np.genfromtxt(args.best, skip_header=1)

    #load observations
    obs = np.loadtxt(args.obs, usecols=2) #mm/d
    tflux = np.genfromtxt(args.obs,usecols=0, dtype=np.str )#mm/d
    tflux = pd.date_range(tflux[0], tflux[-1], freq='D')   

    #load weather data
    weather_data = np.loadtxt(args.weather, skiprows=1 )
    tmod = np.arange(datetime(int(weather_data[0,3]),int(weather_data[0,2]),int(weather_data[0,1])), 
                  datetime(int(weather_data[-1,3]),int(weather_data[-1,2]),int(weather_data[-1,1])), 
                  timedelta(days=1)).astype(datetime)
    prec = weather_data[:, 6] #mm/d

    #make plot
    fig=plt.figure(figsize=(16, 5), dpi= 80, facecolor='w', edgecolor='k' )
    fig, ((ax0 ))  = plt.subplots(nrows=1, ncols=1, figsize=(16, 5))        

    if( args.var == "evaporation"):
        best = best_data[:,10] + best_data[:,26] + best_data[:,27]
        ax0.fill_between(tmod[0:len(max_mod)], max_mod*1000,  min_mod*1000, 
                          color='red',facecolor='red', zorder=0, alpha = 0.2 )
        ax0.plot(tflux, obs, color='blue', label='Obs.', zorder=1)
        ax0.plot(tmod[0:len(best)], best*1000, color='red', label='VOM', zorder=1)           
        ax0.set_ylabel(r'E$_{t}$ (mm/d) ', size=24  )

    if( args.var == "assimilation"):
        best = best_data[:,19] + best_data[:,20]
        ax0.fill_between(tmod[0:len(max_mod)], max_mod,  min_mod, 
                          color='red',facecolor='red', zorder=0, alpha = 0.2 )
        ax0.plot(tflux, -obs, color='blue', label='Obs.', zorder=1)
        ax0.plot(tmod[0:len(best)], best, color='red', label='VOM', zorder=1)           
        ax0.set_ylabel(r'CO$_{2}$ uptake (mol/m$^2$/d) ', size=24  )

    #ax0.plot(t_emp, emp1, color='lightgray', label='emp1', zorder=1)
    #ax0.plot(t_emp, emp2, color='darkgray', label='emp2', zorder=1)


    #set axis and ticks
    ax0.set_xlabel('' , size=24   )
    ax0.set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    for tick in ax0.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax0.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    if( args.var == "evaporation"):
        ax0.set_ylim( [0,10] )
    if( args.var == "assimilation"):
        ax0.set_ylim( [0,1.5] )
    ax0.set_frame_on(True) # make it transparent
    
    #add rainfall on top
    ax1 = ax0.twinx()
    ax1.stem(tmod[0:len(max_mod)],-prec[0:len(max_mod)] ,markerfmt=" ", basefmt=" ")
    ax1.set_ylabel(r'Prec. (mm/d) ', size=24  )
    ax1.set_xlim([datetime(yearstart,1, 1), datetime( yearend, 12, 31)])
    
    #set labels
    max_pre = max(prec)
    y1_ticks = np.linspace(0, 250, 6)
    y1_ticklabels = [str(i) for i in y1_ticks]
    ax1.set_yticks(-1 * y1_ticks)
    ax1.set_yticklabels(y1_ticklabels, fontsize = 20)
    for tick in ax1.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    ax1.set_ylim( [-250, 0] )
    
    ax0.legend(prop={'size':15})

    ax0.set_zorder(ax1.get_zorder()+1) # put ax in front of ax2
    ax0.patch.set_visible(False)
    plt.tight_layout()

    #plt.show()
    plt.savefig(args.outputfile)

    print("Script finished")


main()



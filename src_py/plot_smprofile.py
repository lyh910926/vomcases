import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date


#file to prepare plot of VOM soil moisture - depth
#Vegetation Optimality Model (VOM)
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    #required input
    parser.add_argument("-i", "--input", help="results_hourly (can be multiple)", nargs='+')
    parser.add_argument("-v", "--var", help="variable in results_daily, or total assimilation (asstot) or evaporation(evaptot)")
    parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-w", "--weather", help="dailyweather.prn")

    #optional input
    parser.add_argument("--maxmod", help="results_daily max-values ")
    parser.add_argument("--minmod", help="results_daily min-values")
    parser.add_argument("--emp1", help="empirical solution 1")
    parser.add_argument("--emp2", help="empirical solution 2")
    parser.add_argument("--obs", help="observations")
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--mf", help="multiplication factor for unit conversion", type=float, default = 1.0)
    parser.add_argument("--mf_obs", help="multiplication factor for unit conversion observations", type=float, default = 1.0)
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,5] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")

    args = parser.parse_args()

    ##########################################
    #years to plot
    yearstart = args.yearstart
    yearend = args.yearend

    #get benchmark if defined
    if args.emp1 is not None:
        emp1 = np.genfromtxt(args.emp1, usecols=1, dtype=np.float)
    if args.emp2 is not None:
        emp2 = np.genfromtxt(args.emp2, usecols=1, dtype=np.float)
        t_emp = np.genfromtxt( args.emp2, usecols=0, dtype=np.str)
        t_emp = pd.date_range(t_emp[0], t_emp[-1], freq='D')    

    #load max model runs
    if args.maxmod is not None:
        max_mod = np.genfromtxt(args.maxmod, names=True)
        if( args.var == "evaptot"):
            maxvals = (max_mod["etmt"] + max_mod["etmg"] + max_mod["esoil"])*args.mf
        elif( args.var == "asstot"):
            maxvals = (max_mod["asst"] + max_mod["assg"])*args.mf
        else:
            minvals = max_mod[args.var]*args.mf 

    #load min model runs
    if args.minmod is not None:
        min_mod = np.genfromtxt(args.minmod, names=True)
        if( args.var == "evaptot"):
            minvals = (min_mod["etmt"] + min_mod["etmg"] + min_mod["esoil"])*args.mf
        elif( args.var == "asstot"):
            minvals = (min_mod["asst"] + min_mod["assg"])*args.mf
        else:
            minvals = min_mod[args.var]*args.mf 

    #load results
    vals = []
    tmod = []
    for i in range(0, len(args.input)):
        data = np.genfromtxt(args.input[i], names=True)
        if( args.var == "evaptot"):
            vals.append( (data["etmt"] + data["etmg"] + data["esoil"])*args.mf)
        elif( args.var == "asstot"):
            vals.append( (data["asst"] + data["assg"])*args.mf )
        else:
            vals.append( data[args.var]*args.mf )

        tmod.append(np.arange(datetime(int(data["fyear"][0]),int(data["fmonth"][0]),int(data["fday"][0])), 
                  datetime(int(data["fyear"][-1]),int(data["fmonth"][-1]),int(data["fday"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime))

    #load observations
    if args.obs is not None:
        #values observations
        obs = (np.loadtxt(args.obs, usecols=2) ) *args.mf_obs  #mm/d
        #date/times observations
        tobs = np.genfromtxt(args.obs,usecols=0, dtype=np.str )#mm/d
        tobs = pd.date_range(tobs[0], tobs[-1], freq='D')   

    #load weather data
    weather_data = np.genfromtxt(args.weather, names=True)
    tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                  datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot
    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    fig, ax0 = plt.subplots(nrows=1, ncols=1, figsize=(args.figsize[0], args.figsize[1]))        

    #plot envelope of max and min values
    if( (args.minmod is not None) and (args.maxmod is not None) ):
        ax0.fill_between(tmod[0], maxvals,  minvals, 
                          color='red',facecolor='red', zorder=0, alpha = 0.2 )
    #plot observations
    if args.obs is not None:
        ax0.plot(tobs, obs, color='blue', label='Obs.', zorder=1)

    #plot model results
    for i in range(0, len(args.input)):
        ax0.plot(tmod[i], vals[i], color='red', label=args.labels[i], zorder=1)           

    #plot emperical benchmarks
    if args.emp1 is not None:
        ax0.plot(t_emp1, emp1, color='lightgray', label='emp1', zorder=1)
    if args.emp2 is not None:
        ax0.plot(t_emp2, emp2, color='gray', label='emp2', zorder=1)

    #set labels
    ax0.set_ylabel(args.ylabel, size=24  )
    ax0.set_xlabel(args.xlabel, size=24  )

    #set axis and ticks
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
    ax1.stem(tweather,-prec ,markerfmt=" ", basefmt=" ")
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

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile)
    else:
        plt.show()

    print("Script finished")


main()



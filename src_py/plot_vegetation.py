import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date


#file to prepare timeseries plot of VOM-results
#Vegetation Optimality Model (VOM)
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    #required input
    parser.add_argument("-i", "--input", help="results_daily (can be multiple)", nargs='+')
    parser.add_argument("-v", "--var", help="variable in results_daily, or total assimilation (asstot) or evaporation(evaptot)")
    parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-w", "--weather", help="dailyweather.prn")

    #optional input
    parser.add_argument("--i2015", help="results_daily AoB2015 ")
    parser.add_argument("--var2015", help="variable in results_daily, or total assimilation (asstot) or evaporation(evaptot), 2015 format")
    parser.add_argument("--maxmod", help="results_daily max-values ")
    parser.add_argument("--minmod", help="results_daily min-values")
    parser.add_argument("--emp1", help="empirical solution 1")
    parser.add_argument("--emp2", help="empirical solution 2")
    parser.add_argument("--obs", help="observations of fpar")
    parser.add_argument("--obsdates", help="dates of fpar")
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--mf", help="multiplication factor for unit conversion", type=float, default = 1.0)
    parser.add_argument("--mf_obs", help="multiplication factor for unit conversion observations", type=float, default = 1.0)
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,5] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")
    parser.add_argument("--cblabel", help="label for colorbar", default=" ")
    parser.add_argument("--title", help="title", default=" ")
    parser.add_argument("--plot_prec", help="add precipation to figure", type=bool, default = False )
    parser.add_argument("--plot_cbar", help="add colorbar", type=bool, default = False )
    parser.add_argument("--cbar_min", help="min value for colorbar", type=float, default = 0.2)
    parser.add_argument("--cbar_max", help="max value for colorbar", type=float, default = 2.6 )
    parser.add_argument("--legend", help="show legend", type=bool, default = False )
    parser.add_argument("--palette", help="color-palette", default = 'OrRd' )


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

    if args.i2015 is not None:

        data2015 = np.genfromtxt(args.i2015, names=True)

        if( args.var2015 == "evaptot"):
            vals2015 =  (data2015["etm_t"] + data2015["etm_g"] + data2015["esoil"])*args.mf
        elif( args.var2015 == "asstot"):
            vals2015 = (data2015["ass_t"] + data2015["ass_g"])*args.mf 
        else:
            vals2015 = data2015[args.var2015]*args.mf 

        tmod2015 = np.arange(datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0])), 
                      datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0]))+timedelta(days=len(vals2015) ), 
                      timedelta(days=1)).astype(datetime)


    #load observations
    if args.obs is not None:
        #values observations
        obs = np.loadtxt(args.obs,delimiter=',', usecols=3 )
        obs = 100*obs/0.95 #from fPar to vegetative cover
        tobs = np.genfromtxt(args.obsdates, dtype='str', delimiter=',')
        tobs = pd.to_datetime(tobs[:,1], format="%Y%m")



    #load weather data
    weather_data = np.genfromtxt(args.weather, names=True)
    tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                  datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot
    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    #fig, ax0 = plt.subplots(nrows=1, ncols=1, figsize=(args.figsize[0], args.figsize[1]))        


    ax0  = fig.add_axes([0.10,0.10,0.75,0.85])
    #plot envelope of max and min values
    if( (args.minmod is not None) and (args.maxmod is not None) ):
        ax0.fill_between(tmod[0], maxvals,  minvals, 
                          color='red',facecolor='red', zorder=0, alpha = 0.2 )
    #plot observations
    if args.obs is not None:
        ax0.plot(tobs, obs, color='blue', label='Obs.', zorder=2)

    #plot observations
    if args.i2015 is not None:
        ax0.plot(tmod2015, vals2015, color='green', label='2015 data', zorder=2)

    palette = plt.get_cmap(args.palette, len(args.input))

    if(args.plot_cbar == True):
        ax2  = fig.add_axes([0.90,0.10,0.03,0.85])
        norm = mpl.colors.Normalize(vmin=args.cbar_min, vmax=args.cbar_max)
        cb  = mpl.colorbar.ColorbarBase(ax2,cmap=palette,norm=norm,orientation='vertical')
        cb.ax.tick_params(labelsize=14)
        cb.set_label(args.cblabel, labelpad=10, size=20)


    #plot model results
    for i in range(0, len(args.input)):
        try:
            ax0.plot(tmod[i], vals[i], color=palette(i), label=args.labels[i], zorder=1)           
        except IndexError:
            ax0.plot(tmod[i], vals[i], color=palette(i), label=str(i), zorder=1)           

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
        tick.label.set_rotation(90)
    for tick in ax0.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    if( args.var == "evaporation"):
        ax0.set_ylim( [0,10] )
    if( args.var == "assimilation"):
        ax0.set_ylim( [0,1.5] )
    if( args.var == "pc"):
        ax0.set_ylim( [0,100] )

    ax0.set_frame_on(True) # make it transparent
    

    if( args.plot_prec == True):
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
        ax0.set_zorder(ax1.get_zorder()+1) # put ax in front of ax2

    if(args.legend == True):
        ax0.legend(prop={'size':15})
 
   #add title
    if args.title is not None:
        ax0.text(0.01, 0.95, args.title, ha='left', va='center', transform=ax0.transAxes, fontsize=20)
    else:
        plt.show()

    ax0.patch.set_visible(False)
    plt.tight_layout()

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile)
    else:
        plt.show()



main()



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
    parser.add_argument("--eobs", help="observations evaporation")
    parser.add_argument("--eobs_qc", help="quality of observations evaporation")
    parser.add_argument("--assobs", help="observations evaporation")
    parser.add_argument("--assobs_qc", help="quality of observations evaporation")
    parser.add_argument("--pcobs", help="observations of fpar")
    parser.add_argument("--pcobsdates", help="dates of fpar")

    parser.add_argument("--stats_evap", help="statistics of evaporation timeseries", nargs='+')
    parser.add_argument("--stats_ass", help="statistics of assimilation timeseries", nargs='+')
    parser.add_argument("--stats_pc", help="statistics of projective cover timeseries", nargs='+')
    parser.add_argument("--stats_label", help="label for statistics", nargs='+')

    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,15] )
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
    parser.add_argument("--xloc_title", help="location x title", type=float, default = 0.01 )
    parser.add_argument("--yloc_title", help="location y title", type=float, default = 1.05 )
    parser.add_argument("--size_title", help="size of title", type=float, default = 20 )
    parser.add_argument("--locx_qctitle", help="x-location of qflag-label", type=float, default = 1.04 )
    parser.add_argument("--locy_qctitle", help="y-location of qflag-label", type=float, default = 0.92 )

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

    #load results
    jmax25t_vals = []
    jmax25g_vals = []
    pcvals = []
    tmod = []
    for i in range(0, len(args.input)):
        data = np.genfromtxt(args.input[i], names=True)
        jmax25t_vals.append( (data["jmax25t"] ) )
        jmax25g_vals.append( (data["jmax25g"] ) )
        pcvals.append( data["pc"] * 100.0 ) 

        tmod.append(np.arange(datetime(int(data["fyear"][0]),int(data["fmonth"][0]),int(data["fday"][0])), 
                      datetime(int(data["fyear"][-1]),int(data["fmonth"][-1]),int(data["fday"][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime))


    if args.i2015 is not None:

        data2015 = np.genfromtxt(args.i2015, names=True)

        jmax25t_vals2015 =  data2015["jmax25_t"] 
        jmax25g_2015 = data2015["jmax25_g"] 
        pcvals2015 = data2015["pc"]*100.0

        tmod2015 = np.arange(datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0])), 
                      datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0]))+timedelta(days=len(vals2015) ), 
                      timedelta(days=1)).astype(datetime)

    #load observations
    if args.pcobs is not None:
        #values observations
        pcobs = np.genfromtxt(args.pcobs,delimiter=',', usecols=3, missing_values=-999 )
        pcobs[pcobs <= 0] = np.nan
        pcobs = 100*pcobs/0.95 #from fPar to vegetative cover
        t_pcobs = np.genfromtxt(args.pcobsdates, dtype='str', delimiter=',')
        t_pcobs = pd.to_datetime(t_pcobs[:,1], format="%Y%m")

    if args.eobs_qc is not None:
        #values observations
        eobs_qc = (np.loadtxt(args.eobs_qc, usecols=2) )  #mm/d
        #date/times observations
        teobs_qc = np.genfromtxt(args.eobs_qc,usecols=0, dtype=np.str )
        teobs_qc2 = np.genfromtxt(args.eobs_qc,usecols=1, dtype=np.str )#mm/d
        teobs_qc = pd.date_range(teobs_qc[0]+" "+teobs_qc2[0], teobs_qc[-1]+" "+teobs_qc2[-1], freq='30Min') 
        qce_pd = pd.Series(eobs_qc, index=teobs_qc)
        qce_daily = qce_pd.resample("D").mean()

    if args.assobs_qc is not None:
        #values observations
        assobs_qc = (np.loadtxt(args.assobs_qc, usecols=2) )  #mm/d
        #date/times observations
        tassobs_qc = np.genfromtxt(args.assobs_qc,usecols=0, dtype=np.str )
        tassobs_qc2 = np.genfromtxt(args.assobs_qc,usecols=1, dtype=np.str )#mm/d
        tassobs_qc = pd.date_range(tassobs_qc[0]+" "+tassobs_qc2[0], tassobs_qc[-1]+" "+tassobs_qc2[-1], freq='30Min') 
        qcass_pd = pd.Series(assobs_qc, index=tassobs_qc)
        qcass_daily = qcass_pd.resample("D").mean()


    #load weather data
    weather_data = np.genfromtxt(args.weather, names=True)
    tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                  datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot
    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(args.figsize[0], args.figsize[1]))        
    ax = axes.flat

    if args.palette is not None:
        palette = plt.get_cmap(args.palette, len(args.input))

    if args.colors is not None:
        colors = args.colors

    #############################
    #plot observations
    if args.pcobs is not None:
        ax[2].plot(t_pcobs, pcobs, color='blue', label='Obs.', zorder=2)


    #############################
    #plot observations
    if args.i2015 is not None:
        ax[0].plot(tmod2015, jmax25t_vals2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[1].plot(tmod2015, jmax25g_2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[2].plot(tmod2015, pcvals2015, color='green', label='Schymanski et al. (2015)', zorder=2)

    #############################
    if(args.plot_cbar == True):
        #axcbar0  = fig.add_axes([1.01,0.80,0.03,0.20])
        axcbar0  = fig.add_axes([ax[0].get_position().x1+0.12, ax[0].get_position().y0 +0.105, 0.03, ax[0].get_position().height])
        axcbar1  = fig.add_axes([ax[1].get_position().x1+0.12, ax[1].get_position().y0 +0.032, 0.03, ax[1].get_position().height])
        axcbar2  = fig.add_axes([ax[2].get_position().x1+0.12, ax[2].get_position().y0 -0.03, 0.03, ax[2].get_position().height])

        norm = mpl.colors.Normalize(vmin=args.cbar_min, vmax=args.cbar_max)
        cb0  = mpl.colorbar.ColorbarBase(axcbar0,cmap=palette,norm=norm,orientation='vertical')
        cb1  = mpl.colorbar.ColorbarBase(axcbar1,cmap=palette,norm=norm,orientation='vertical')
        cb2  = mpl.colorbar.ColorbarBase(axcbar2,cmap=palette,norm=norm,orientation='vertical')
        cb0.ax.tick_params(labelsize=14)
        cb1.ax.tick_params(labelsize=14)
        cb2.ax.tick_params(labelsize=14)
        cb0.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb1.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb2.set_label(r'' + args.cblabel, labelpad=10, size=20)

    #############################
    #plot model results
    for i in range(0, len(args.input)):
        if(args.plot_cbar == True):
            try:
                ax[0].plot(tmod[i], jmax25t_vals[i], color=palette(i), zorder=1) 
                ax[1].plot(tmod[i], jmax25g_vals[i], color=palette(i), zorder=1)           
                ax[2].plot(tmod[i], pcvals[i], color=palette(i), zorder=1)                     
            except IndexError:
                ax[0].plot(tmod[i], jmax25t_vals[i], color=palette(i), zorder=1) 
                ax[1].plot(tmod[i], jmax25g_vals[i], color=palette(i), zorder=1) 
                ax[2].plot(tmod[i], pcvals[i], color=palette(i), zorder=1) 
        else:
            try:
                ax[0].plot(tmod[i], jmax25t_vals[i], color=colors[i], label=args.labels[i], zorder=1)  
                ax[1].plot(tmod[i], jmax25g_vals[i], color=colors[i], label=args.labels[i], zorder=1)           
                ax[2].plot(tmod[i], pcvals[i], color=colors[i], label=args.labels[i], zorder=1)                    
            except IndexError:
                ax[0].plot(tmod[i], jmax25t_vals[i], color=colors[i], label=str(i), zorder=1)           
                ax[1].plot(tmod[i], jmax25g_vals[i], color=colors[i], label=str(i), zorder=1)           
                ax[2].plot(tmod[i], pcvals[i], color=colors[i], label=str(i), zorder=1)           

    #set labels
    ax[0].set_ylabel(r"J$_{max25,t}$ (mol/m$^2$/s)" , size=24  )
    ax[1].set_ylabel(r"$J_{max25,g}$ (mol/m$^2$/s)", size=24  )
    ax[2].set_ylabel(r"Proj. Cover (%)", size=24  )

    #set axis and ticks
    ax[0].set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    ax[1].set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    ax[2].set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 

    for tick in ax[0].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
        tick.label.set_rotation(90)
    for tick in ax[0].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    for tick in ax[1].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
        tick.label.set_rotation(90)
    for tick in ax[1].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    for tick in ax[2].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
        tick.label.set_rotation(90)
    for tick in ax[2].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    #ax[0].set_ylim( [0,10] )
    #ax[1].set_ylim( [0,1.5] )
    ax[2].set_ylim( [0,100] )

    ax[0].set_frame_on(True) # make it transparent
    ax[1].set_frame_on(True) 
    ax[2].set_frame_on(True) 

    if(args.legend == True):
        ax[0].legend(prop={'size':15}, loc='upper right')
        ax[1].legend(prop={'size':15}, loc='upper right')
        ax[2].legend(prop={'size':15}, loc='upper right')
 
   #add title
    #if args.title is not None:
    ax[0].text(args.xloc_title, args.yloc_title, "a)", ha='left', va='center', transform=ax[0].transAxes, fontsize=args.size_title)
    ax[1].text(args.xloc_title, args.yloc_title, "b)", ha='left', va='center', transform=ax[1].transAxes, fontsize=args.size_title)
    ax[2].text(args.xloc_title, args.yloc_title, "c)", ha='left', va='center', transform=ax[2].transAxes, fontsize=args.size_title)
    #else:
    #    plt.show()



    ax[0].patch.set_visible(False)
    ax[1].patch.set_visible(False)
    ax[2].patch.set_visible(False)

    plt.tight_layout()

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile, bbox_inches = "tight")
    else:
        plt.show()



main()



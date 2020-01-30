import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
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

    parser.add_argument("--maxmod", help="results_daily max-values ")
    parser.add_argument("--minmod", help="results_daily min-values")
    parser.add_argument("--emp1", help="empirical solution 1")
    parser.add_argument("--emp2", help="empirical solution 2")
    parser.add_argument("--obs_gw", help="observations groundwater Howard Springs", nargs='+')
    parser.add_argument("--obs_sm", help="observations soil moisture all sites", nargs='+')
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--mf", help="multiplication factor for unit conversion", type=float, default = 1.0)
    parser.add_argument("--mf_obs", help="multiplication factor for unit conversion observations", type=float, default = 1.0)
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,5] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--i_cz", help="surface level, for groundwater plot", type=float )
    parser.add_argument("--i_zr", help="bottom level, for groundwater plot", type=float )
    parser.add_argument("--i_cz2015", help="surface level, for groundwater plot", type=float )
    parser.add_argument("--i_zr2015", help="bottom level, for groundwater plot", type=float )
    parser.add_argument("--pars", help="parameter file, for plotting rooting depths" )
    parser.add_argument("--depth", help="plot depth, default is water table" )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")
    parser.add_argument("--cblabel", help="label for colorbar", default=" ")
    parser.add_argument("--title", help="title", type=bool, default=False)
    parser.add_argument("--plot_prec", help="add precipation to figure", type=bool, default = False )
    parser.add_argument("--plot_cbar", help="add colorbar", type=bool, default = False )
    parser.add_argument("--cbar_min", help="min value for colorbar", type=float, default = 0.2)
    parser.add_argument("--cbar_max", help="max value for colorbar", type=float, default = 2.6 )
    parser.add_argument("--legend", help="show legend", type=bool, default = False )
    parser.add_argument("--palette", help="color-palette", default = 'OrRd' )
    parser.add_argument("--xloc_title", help="location x title", type=float, default = 0.01 )
    parser.add_argument("--yloc_title", help="location y title", type=float, default = 1.05 )
    parser.add_argument("--ylim", help="limits y-axist", type=float, nargs='+', default = [-50,0] )
    parser.add_argument("--size_title", help="size of title", type=float, default = 20 )


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
    zw_vals = []
    su_vals = []
    tmod = []
    for i in range(0, len(args.input)):
        data = np.genfromtxt(args.input[i], names=True)

        if( args.depth == "True"):
            zw_vals_tmp = -1.0*( args.i_cz - data["zw"])
        else:
            zw_vals_tmp = data["zw"]

        su_vals.append(data["su_1"])
        zw_vals.append(zw_vals_tmp)

        tmod.append(np.arange(datetime(int(data["fyear"][0]),int(data["fmonth"][0]),int(data["fday"][0])), 
                      datetime(int(data["fyear"][-1]),int(data["fmonth"][-1]),int(data["fday"][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime))

    if args.i2015 is not None:

        data2015 = np.genfromtxt(args.i2015, names=True)

        vals2015 = data2015["ws"]
        su_vals2015 = data2015["su_1"]

        if( args.depth == "True"):
            vals2015 = -1*(args.i_cz2015 - vals2015)

        tmod2015 = np.arange(datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0])), 
                      datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0]))+timedelta(days=len(vals2015) ), 
                      timedelta(days=1)).astype(datetime)

    #load parameters
    if args.pars is not None:
        params = np.loadtxt(args.pars)

    #load observations
    if args.obs_gw is not None:

        obs_gw = []
        tobs_gw = []
        for i in range(0, len(args.obs_gw)):


            #values observations
            obs_tmp = (np.genfromtxt(args.obs_gw[i], usecols=1, missing_values="", delimiter=",", skip_header=4) ) *args.mf_obs  #
            #date/times observations
            tobs_tmp = np.genfromtxt(args.obs_gw[i],usecols=0, missing_values="", delimiter=",", skip_header=4, dtype=np.str )#mm/d
            tobs_tmp = pd.date_range(tobs_tmp[0], tobs_tmp[-1], freq='D')   

            obs_gw.append(obs_tmp)
            tobs_gw.append(tobs_tmp)

    #observations of soil moisture
    obs_sm = []
    tobs_sm = []
    if args.obs_sm is not None:
        for i in range(0, len(args.obs_sm)):
            #values observations
            obs_sm.append((np.loadtxt(args.obs_sm[i], usecols=2) ) *args.mf_obs)  #mm/d
            #date/times observations
            tobs_tmp = np.genfromtxt(args.obs_sm[i],usecols=0, dtype=np.str )#mm/d
            tobs_sm.append(pd.date_range(tobs_tmp[0], tobs_tmp[-1], freq='D') )


    #load weather data
    if args.weather is not None:
        weather_data = np.genfromtxt(args.weather, names=True)
        tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                      datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime)
        prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot
    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    fig, axes = plt.subplots(nrows=len(args.input)+1, ncols=1, figsize=(args.figsize[0], args.figsize[1]))        
    ax = axes.flat

    #ax[0]  = fig.add_axes([0.10,0.10,0.75,0.85])

    #plot observations
    if args.obs_gw is not None:

        for i in range(0, len(args.obs_gw)):
            if(i == 0):
                ax[0].plot(tobs_gw[i], -obs_gw[i], color='blue', label='Obs.', zorder=2)
            else:
                ax[0].plot(tobs_gw[i], -obs_gw[i], color='blue', zorder=2)

    #plot 2015 data
    if args.i2015 is not None:
        ax[0].plot(tmod2015, vals2015, color='green', label='Schymanski et al. (2015)', zorder=2)


    if args.palette is not None:
        palette = plt.get_cmap(args.palette, len(args.input))

    if args.colors is not None:
        colors = args.colors



    if args.colors is not None:
        ax[0].plot(tmod[0], zw_vals[0], color=colors[0], label=args.labels[0], zorder=1)                
    else:
        ax[0].plot(tmod[0], zw_vals[0], color=palette(0), label=args.labels[0], zorder=1) 

 
 

    #plot rooting depths
    if args.pars is not None:
        if(args.depth == "True"):
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params[5], - params[5]], ":", lw=3, color='red', label='rtdepth trees')
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params[7],  -params[7]],":",lw=3,color='orange', label='rtdepth grasses')
        else:
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [args.i_cz- params[5], args.i_cz - params[5]], ":", lw=3, color='red', label='rtdepth trees')
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [args.i_cz - params[7], args.i_cz-params[7]],":",lw=3, color='orange', label='rtdepth grasses')


    if args.i_zr is not None:
        if(args.depth == "True"):
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)],[-args.i_cz + args.i_zr, -args.i_cz + args.i_zr], "--",color='black', label=r'$Z_{r}$')
        else:
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)],[args.i_zr,args.i_zr], "--",color='black', label='i_zr')

    if args.i_zr2015 is not None:
        if(args.depth == "True"):
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)],[-args.i_cz2015 + args.i_zr2015, -args.i_cz2015 + args.i_zr2015], "--",color='grey', label=r'$Z_{r}$ 2015')
        else:
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)],[args.i_zr2015,args.i_zr2015], "--",color='grey', label=r'$Z_{r}$')



    #set labels
    ax[0].set_ylabel("Water table [m]", size=24  )
    ax[0].set_xlabel(args.xlabel, size=24  )

    #set axis and ticks


    locator = mdate.YearLocator()
    ax[0].xaxis.set_major_locator(locator)
    ax[0].xaxis.set_major_formatter(mdate.DateFormatter('%Y'))


    ax[0].set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    for tick in ax[0].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
        #tick.label.set_rotation(90)
    for tick in ax[0].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    ax[0].set_ylim( args.ylim )

    ax[0].set_frame_on(True) # make it transparent
    
    if(args.legend == True):
        ax[0].legend(prop={'size':15}, framealpha=1  )


    ##############################################################
    #soil moisture plots



    #plot soil moisture results
    iplot = 1
    for i in range(0, len(args.input)):
        ax[iplot].plot(tmod[i], su_vals[i], color="red", label="VOM", zorder=1) 
    
        #plot 2015 data
        if args.i2015 is not None:
            if iplot ==1:
                ax[iplot].plot(tmod2015, su_vals2015, color='green', label='Schymanski et al. (2015)', zorder=2)

        ax[iplot].set_ylabel("Soil moisture [-]", size=24  )
        for tick in ax[iplot].xaxis.get_major_ticks():
            tick.label.set_fontsize(20)
            #tick.label.set_rotation(90)
        for tick in ax[iplot].yaxis.get_major_ticks():
            tick.label.set_fontsize(20)

        locator = mdate.YearLocator()
        ax[iplot].xaxis.set_major_locator(locator)
        ax[iplot].xaxis.set_major_formatter(mdate.DateFormatter('%Y'))


        iplot = iplot +1 

    #plot observations
    iplot = 1
    if args.obs_sm is not None:

        for i in range(0, len(args.obs_sm)):
            ax[iplot].plot(tobs_sm[i], obs_sm[i], color='blue', label='Obs.', zorder=2)

            ax[iplot].set_xlim([tobs_sm[i][0], tobs_sm[i][-1]]) 
            if(args.legend == True):
                ax[iplot].legend(prop={'size':15}, framealpha=1  )
            iplot = iplot +1 




 
   #add title
    if args.title is True:

        plot_label = ["a)","b)","c)","d)","e)","f)", "g)"]
        for i in range(0, iplot):
            ax[i].text(args.xloc_title, args.yloc_title, plot_label[i], ha='left', va='center', transform=ax[i].transAxes, fontsize=args.size_title)


    #ax[0].patch.set_visible(False)
    #plt.tight_layout()

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile, bbox_inches = "tight")
    else:
        plt.show()



main()



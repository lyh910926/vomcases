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
    parser.add_argument("--moving_average", help="days for moving average",  type=int )
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [14,35] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--labelsize", help="size of labels",  type=float, default = 24 )
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
    parser.add_argument("--yloc_title", help="location y title", type=float, default = 1.10 )
    parser.add_argument("--size_title", help="size of title", type=float, default = 20 )
    parser.add_argument("--locx_qctitle", help="x-location of qflag-label", type=float, default = 1.04 )
    parser.add_argument("--locy_qctitle", help="y-location of qflag-label", type=float, default = 0.92 )
    parser.add_argument("--hpad", help="h_pad tight_layout", type=float, default = 0 )
    parser.add_argument("--fig_lab", dest="fig_lab", action='store_true', help="plot labels of subplots")
    parser.add_argument("--no_fig_lab", dest="fig_lab", action='store_false', help="do not plot labels of subplots")
    parser.add_argument("--sharex", help="share x-axis", dest="sharex", action='store_true' )
    parser.add_argument("--no_sharex", help="share x-axis", dest="sharex", action='store_false')
    parser.add_argument("--tight_layout", help="tight layout", dest="tight_layout", action='store_true' )
    parser.add_argument("--no_tight_layout", help="no tight layout", dest="tight_layout", action='store_false')
    parser.set_defaults(fig_lab=True, sharex = False, tight_layout=True)

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
    evals = []
    etmt = []
    etmg = []
    esoil = []

    assvals = []
    asst = []
    assg = []

    pcvals = []
    tmod = []
    for i in range(0, len(args.input)):
        data = np.genfromtxt(args.input[i], names=True)
        evals.append( (data["etmt"] + data["etmg"] + data["esoil"])*1000.0)
        etmt.append( data["etmt"]*1000.0)
        etmg.append( data["etmg"] *1000.0)
        esoil.append( data["esoil"]*1000.0)

        assvals.append( (data["asst"] + data["assg"]) )
        assg.append( data["assg"]) 
        asst.append( data["asst"])

        pcvals.append( data["pc"] * 100.0 ) 

        tmod.append(np.arange(datetime(int(data["fyear"][0]),int(data["fmonth"][0]),int(data["fday"][0])), 
                      datetime(int(data["fyear"][-1]),int(data["fmonth"][-1]),int(data["fday"][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime))

        if args.moving_average is not None:

            evals_pd = pd.DataFrame(evals[i], index=tmod[i])
            etmt_pd = pd.DataFrame(etmt[i], index=tmod[i])
            etmg_pd = pd.DataFrame(etmg[i], index=tmod[i])
            esoil_pd = pd.DataFrame(esoil[i], index=tmod[i])

            evals_ma = evals_pd.rolling( window = args.moving_average ).mean()
            etmt_ma = etmt_pd.rolling( window = args.moving_average ).mean()
            etmg_ma = etmg_pd.rolling( window = args.moving_average ).mean()
            esoil_ma = esoil_pd.rolling( window = args.moving_average ).mean()

            assvals_pd = pd.DataFrame(assvals[i], index=tmod[i])
            assg_pd = pd.DataFrame(assg[i], index=tmod[i])
            asst_pd = pd.DataFrame(asst[i], index=tmod[i])

            assvals_ma = assvals_pd.rolling( window = args.moving_average ).mean()
            assg_ma = assg_pd.rolling( window = args.moving_average ).mean()
            asst_ma = asst_pd.rolling( window = args.moving_average ).mean()

            #replace values
            evals[i] = evals_ma
            etmt[i] = etmt_ma
            etmg[i] = etmg_ma
            esoil[i] = esoil_ma

            assvals[i] = assvals_ma
            assg[i] = assg_ma
            asst[i] = asst_ma

            tmod[i] = evals_ma.index

    if args.i2015 is not None:

        data2015 = np.genfromtxt(args.i2015, names=True)

        evals2015 =  (data2015["etm_t"] + data2015["etm_g"] + data2015["esoil"])*1000.0
        etmt2015 =  data2015["etm_t"]*1000.0
        etmg2015 =  data2015["etm_g"]*1000.0
        esoil2015 =  data2015["esoil"]*1000.0

        assvals2015 = (data2015["ass_t"] + data2015["ass_g"])
        asst2015 = data2015["ass_t"] 
        assg2015 = data2015["ass_g"]

        pcvals2015 = data2015["pc"]*100.0

        tmod2015 = np.arange(datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0])), 
                      datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0]))+timedelta(days=len(evals2015) ), 
                      timedelta(days=1)).astype(datetime)

        if args.moving_average is not None:
            evals2015_pd = pd.DataFrame(evals2015, index=tmod2015)
            etmt2015_pd = pd.DataFrame(etmt2015, index=tmod2015)
            etmg2015_pd = pd.DataFrame(etmg2015, index=tmod2015)
            esoil2015_pd = pd.DataFrame(esoil2015, index=tmod2015)

            evals2015_ma = evals2015_pd.rolling( window = args.moving_average ).mean()
            etmt2015_ma = etmt2015_pd.rolling( window = args.moving_average ).mean()
            etmg2015_ma = etmg2015_pd.rolling( window = args.moving_average ).mean()
            esoil2015_ma = esoil2015_pd.rolling( window = args.moving_average ).mean()

            assvals2015_pd = pd.DataFrame(assvals2015, index=tmod2015)
            assg2015_pd = pd.DataFrame(assg2015, index=tmod2015)
            asst2015_pd = pd.DataFrame(asst2015, index=tmod2015)

            assvals2015_ma = assvals2015_pd.rolling( window = args.moving_average ).mean()
            assg2015_ma = assg2015_pd.rolling( window = args.moving_average ).mean()
            asst2015_ma = asst2015_pd.rolling( window = args.moving_average ).mean()

            #replace values
            evals2015 = evals2015_ma
            etmt2015 = etmt2015_ma
            etmg2015 = etmg2015_ma
            esoil2015 = esoil2015_ma

            assvals2015 = assvals2015_ma
            assg2015 = assg2015_ma
            asst2015 = asst2015_ma

            tmod2015 = evals2015_ma.index



    #load observations
    if args.eobs is not None:
        #values observations
        eobs = (np.loadtxt(args.eobs, usecols=2) )  #mm/d
        #date/times observations
        t_eobs = np.genfromtxt(args.eobs,usecols=0, dtype=np.str )#mm/d
        t_eobs = pd.date_range(t_eobs[0], t_eobs[-1], freq='D')   

        if args.moving_average is not None:
            eobs_pd = pd.DataFrame(eobs, index=t_eobs)
            eobs_ma = eobs_pd.rolling( window = args.moving_average ).mean()

            #replace values
            eobs = eobs_ma
            t_eobs = eobs_ma.index

    if args.assobs is not None:
        #values observations
        assobs = (np.loadtxt(args.assobs, usecols=2) ) *-1.0  #mm/d
        #date/times observations
        t_assobs = np.genfromtxt(args.assobs,usecols=0, dtype=np.str )#mm/d
        t_assobs = pd.date_range(t_assobs[0], t_assobs[-1], freq='D')   

        if args.moving_average is not None:
            assobs_pd = pd.DataFrame(assobs, index=t_assobs)
            assobs_ma = assobs_pd.rolling( window = args.moving_average ).mean()

            #replace values
            assobs = assobs_ma
            t_assobs = assobs_ma.index

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

    #load statistics
    evap_stats = []
    ass_stats = []
    pc_stats = []
    if args.stats_evap is not None:
        for i in range(0, len(args.stats_evap)):
            evap_stats.append( np.genfromtxt(args.stats_evap[i] ) )

    if args.stats_ass is not None:
        for i in range(0, len(args.stats_ass)):
            ass_stats.append( np.genfromtxt(args.stats_ass[i] ) )

    if args.stats_pc is not None:
        for i in range(0, len(args.stats_pc)):
            pc_stats.append( np.genfromtxt(args.stats_pc[i] ) )

    #load weather data
    weather_data = np.genfromtxt(args.weather, names=True)
    tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                  datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot

    if args.fig_lab is True:
        plot_label = [ "a)","b)","c)","d)","e)","f)", "g)", "h)" ]
    else: 
        plot_label = [ " "," "," "," "," "," ", " ", " " ]

    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    fig, axes = plt.subplots(nrows=8, ncols=1, figsize=(args.figsize[0], args.figsize[1]), sharex=args.sharex)        
    ax = axes.flat

    if args.palette is not None:
        palette = plt.get_cmap(args.palette, len(args.input))

    if args.colors is not None:
        colors = args.colors

    #############################
    #plot observations
    if args.eobs is not None:
        ax[0].plot(t_eobs, eobs, color='blue', label='Obs.', zorder=2)

    if args.assobs is not None:
        ax[4].plot(t_assobs, assobs, color='blue', label='Obs.', zorder=2)

    if args.pcobs is not None:
        ax[7].plot(t_pcobs, pcobs, color='blue', label='Obs.', zorder=2)

    #############################
    #plot observations quality flux towers
    if args.eobs_qc is not None:

       #add quality flag on top
        ax0twin = ax[0].twinx()
        ax0twin.plot(qce_daily.index, -qce_daily,"--" ,color='black', label='Qflag', zorder=2)
        ax0twin.text(args.locx_qctitle, args.locy_qctitle, "Qflag (-)", ha='left', va='center', transform=ax0twin.transAxes, fontsize=16, rotation=90 )
        ax0twin.set_xlim([datetime(yearstart,1, 1), datetime( yearend, 12, 31)])
        
        #set labels
        #max_pre = max(prec)
        ax0twin_yticks = np.linspace(0, 100, 3)
        ax0twin_yticklabels = ["0", "50", "100"]
        ax0twin.set_yticks(-1 * ax0twin_yticks)
        ax0twin.set_yticklabels(ax0twin_yticklabels, fontsize = 14)
        for tick in ax0twin.yaxis.get_major_ticks():
            tick.label.set_fontsize(14)
        ax0twin.set_ylim( [-500, 0] )
        ax[0].set_zorder(ax0twin.get_zorder()+1) # put ax in front of ax2

    #plot observations quality assimilation
    if args.assobs_qc is not None:

       #add quality flag on top
        ax1twin = ax[4].twinx()
        ax1twin.plot(qcass_daily.index, -qcass_daily,"--" ,color='black', label='Qflag', zorder=2)
        ax1twin.text(args.locx_qctitle, args.locy_qctitle, "Qflag (-)", ha='left', va='center', transform=ax1twin.transAxes, fontsize=16, rotation=90 )
        ax1twin.set_xlim([datetime(yearstart,1, 1), datetime( yearend, 12, 31)])
        
        #set labels
        #max_pre = max(prec)
        ax1twin_yticks = np.linspace(0, 100, 3)
        ax1twin_yticklabels = ["0", "50", "100"]
        ax1twin.set_yticks(-1 * ax1twin_yticks)
        ax1twin.set_yticklabels(ax1twin_yticklabels, fontsize = 14)
        for tick in ax1twin.yaxis.get_major_ticks():
            tick.label.set_fontsize(14)
        ax1twin.set_ylim( [-500, 0] )
        ax[1].set_zorder(ax1twin.get_zorder()+1) # put ax in front of ax2

    #############################
    #plot observations
    if args.i2015 is not None:
        ax[0].plot(tmod2015, evals2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[1].plot(tmod2015, etmt2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[2].plot(tmod2015, etmg2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[4].plot(tmod2015, assvals2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[5].plot(tmod2015, asst2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[6].plot(tmod2015, assg2015, color='green', label='Schymanski et al. (2015)', zorder=2)
        ax[7].plot(tmod2015, pcvals2015, color='green', label='Schymanski et al. (2015)', zorder=2)

    #############################
    if(args.plot_cbar == True):
        #axcbar0  = fig.add_axes([1.01,0.80,0.03,0.20])
        axcbar0  = fig.add_axes([ax[0].get_position().x1+0.12, ax[0].get_position().y0 +0.105, 0.03, ax[0].get_position().height])
        axcbar1  = fig.add_axes([ax[1].get_position().x1+0.12, ax[1].get_position().y0 +0.032, 0.03, ax[1].get_position().height])
        axcbar2  = fig.add_axes([ax[2].get_position().x1+0.12, ax[2].get_position().y0 +0.032, 0.03, ax[2].get_position().height])
        axcbar3  = fig.add_axes([ax[3].get_position().x1+0.12, ax[3].get_position().y0 +0.032, 0.03, ax[3].get_position().height])
        axcbar4  = fig.add_axes([ax[4].get_position().x1+0.12, ax[4].get_position().y0 +0.032, 0.03, ax[3].get_position().height])
        axcbar5  = fig.add_axes([ax[5].get_position().x1+0.12, ax[5].get_position().y0 +0.032, 0.03, ax[3].get_position().height])
        axcbar6  = fig.add_axes([ax[6].get_position().x1+0.12, ax[6].get_position().y0 +0.032, 0.03, ax[3].get_position().height])
        axcbar7  = fig.add_axes([ax[7].get_position().x1+0.12, ax[7].get_position().y0 -0.03, 0.03, ax[4].get_position().height])

        norm = mpl.colors.Normalize(vmin=args.cbar_min, vmax=args.cbar_max)
        cb0  = mpl.colorbar.ColorbarBase(axcbar0,cmap=palette,norm=norm,orientation='vertical')
        cb1  = mpl.colorbar.ColorbarBase(axcbar1,cmap=palette,norm=norm,orientation='vertical')
        cb2  = mpl.colorbar.ColorbarBase(axcbar2,cmap=palette,norm=norm,orientation='vertical')
        cb3  = mpl.colorbar.ColorbarBase(axcbar3,cmap=palette,norm=norm,orientation='vertical')
        cb4  = mpl.colorbar.ColorbarBase(axcbar4,cmap=palette,norm=norm,orientation='vertical')
        cb5  = mpl.colorbar.ColorbarBase(axcbar5,cmap=palette,norm=norm,orientation='vertical')
        cb6  = mpl.colorbar.ColorbarBase(axcbar6,cmap=palette,norm=norm,orientation='vertical')
        cb7  = mpl.colorbar.ColorbarBase(axcbar7,cmap=palette,norm=norm,orientation='vertical')

        cb0.ax.tick_params(labelsize=14)
        cb1.ax.tick_params(labelsize=14)
        cb2.ax.tick_params(labelsize=14)
        cb3.ax.tick_params(labelsize=14)
        cb4.ax.tick_params(labelsize=14)
        cb4.ax.tick_params(labelsize=14)
        cb5.ax.tick_params(labelsize=14)
        cb6.ax.tick_params(labelsize=14)
        cb7.ax.tick_params(labelsize=14)

        cb0.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb1.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb2.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb3.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb4.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb5.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb6.set_label(r'' + args.cblabel, labelpad=10, size=20)
        cb7.set_label(r'' + args.cblabel, labelpad=10, size=20)

    #############################
    #plot model results
    for i in range(0, len(args.input)):
        if(args.plot_cbar == True):
            try:
                ax[0].plot(tmod[i], evals[i], color=palette(i), zorder=1) 
                ax[1].plot(tmod[i], etmt[i], color=palette(i), zorder=1) 
                ax[2].plot(tmod[i], etmg[i], color=palette(i), zorder=1) 
                ax[3].plot(tmod[i], esoil[i], color=palette(i), zorder=1) 

                ax[4].plot(tmod[i], assvals[i], color=palette(i), zorder=1)  
                ax[5].plot(tmod[i], asst[i], color=palette(i), zorder=1)  
                ax[6].plot(tmod[i], assg[i], color=palette(i), zorder=1)                    

                ax[7].plot(tmod[i], pcvals[i], color=palette(i), zorder=1)                     
            except IndexError:
                ax[0].plot(tmod[i], evals[i], color=palette(i), zorder=1) 
                ax[1].plot(tmod[i], etmt[i], color=palette(i), zorder=1) 
                ax[2].plot(tmod[i], etmg[i], color=palette(i), zorder=1) 
                ax[3].plot(tmod[i], esoil[i], color=palette(i), zorder=1) 

                ax[4].plot(tmod[i], assvals[i], color=palette(i), zorder=1)  
                ax[5].plot(tmod[i], asst[i], color=palette(i), zorder=1)  
                ax[6].plot(tmod[i], assg[i], color=palette(i), zorder=1)                    

                ax[7].plot(tmod[i], pcvals[i], color=palette(i), zorder=1)   
        else:
            try:
                ax[0].plot(tmod[i], evals[i], color=colors[i], label=args.labels[i], zorder=1)  
                ax[1].plot(tmod[i], etmt[i],  color=colors[i], label=args.labels[i], zorder=1)  
                ax[2].plot(tmod[i], etmg[i],  color=colors[i], label=args.labels[i], zorder=1)  
                ax[3].plot(tmod[i], esoil[i],  color=colors[i], label=args.labels[i], zorder=1)  

                ax[4].plot(tmod[i], assvals[i], color=colors[i], label=args.labels[i], zorder=1)   
                ax[5].plot(tmod[i], asst[i], color=colors[i], label=args.labels[i], zorder=1)     
                ax[6].plot(tmod[i], assg[i], color=colors[i], label=args.labels[i], zorder=1)    
        
                ax[7].plot(tmod[i], pcvals[i], color=colors[i], label=args.labels[i], zorder=1)   

                 
            except IndexError:
                ax[0].plot(tmod[i], evals[i], color=colors[i], label=str(i), zorder=1)   
                ax[1].plot(tmod[i], etmt[i],  color=colors[i], label=str(i), zorder=1)  
                ax[2].plot(tmod[i], etmg[i],  color=colors[i], label=str(i), zorder=1)  
                ax[3].plot(tmod[i], esoil[i],  color=colors[i], label=str(i), zorder=1)  
        
                ax[4].plot(tmod[i], assvals[i], color=colors[i], label=str(i), zorder=1) 
                ax[5].plot(tmod[i], asst[i], color=colors[i], label=str(i), zorder=1)     
                ax[6].plot(tmod[i], assg[i], color=colors[i], label=str(i), zorder=1)  
          
                ax[7].plot(tmod[i], pcvals[i], color=colors[i], label=str(i), zorder=1)           

    #set labels
    ax[0].set_ylabel("ET (mm d$^{-1}$)" , size=args.labelsize  )
    ax[1].set_ylabel("E$_{perennials}$ \n (mm d$^{-1}$)" , size=args.labelsize  )
    ax[2].set_ylabel("E$_{seasonals}$ \n (mm d$^{-1}$)" , size=args.labelsize  )
    ax[3].set_ylabel("E$_{soil}$ \n (mm d$^{-1}$)" , size=args.labelsize  )

    ax[4].set_ylabel('GPP \n (mol m$^{-2}$ d$^{-1}$)', size=args.labelsize  )
    ax[5].set_ylabel("GPP$_{perennials}$ \n (mol m$^{-2}$ d$^{-1}$)", size=args.labelsize  )
    ax[6].set_ylabel("GPP$_{seasonals}$ \n (mol m$^{-2}$ d$^{-1}$)", size=args.labelsize )

    ax[7].set_ylabel(r"Proj. Cover (%)", size=24  )

    #set axis and ticks
    for iplot in range(0, 8):
        ax[iplot].set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 

        for tick in ax[iplot].xaxis.get_major_ticks():
            tick.label.set_fontsize(20)
            tick.label.set_rotation(90)
        for tick in ax[iplot].yaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        ax[iplot].set_frame_on(True) 
 
        if(args.legend == True):
            ax[iplot].legend(prop={'size':15}, loc='upper right')

        ax[iplot].text(args.xloc_title, args.yloc_title, plot_label[iplot], ha='left', va='center', transform=ax[iplot].transAxes, fontsize=args.size_title)
        ax[iplot].patch.set_visible(False)

    ax[0].set_ylim( [0,10] )
    ax[1].set_ylim( [0,5] )
    ax[2].set_ylim( [0,5] )
    ax[3].set_ylim( [0,5] )

    ax[4].set_ylim( [0,1.5] )
    ax[5].set_ylim( [0,1.0] )
    ax[6].set_ylim( [0,1.0] )

    ax[7].set_ylim( [0,100] )


    #add statistics
    yloc = 0.93
    if args.stats_evap is not None:
        for i in range(0, len(args.stats_evap)):
            ax[0].text(0.01, yloc,  args.stats_label[i] + " = {0:.2f} mm/d".format(evap_stats[i][4])  , ha='left', va='center', transform=ax[0].transAxes, fontsize=14, bbox=dict(boxstyle="square", alpha=0.75, color='white'  ))
            yloc = yloc - 0.12

    yloc = 0.93
    if args.stats_ass is not None:
        for i in range(0, len(args.stats_ass)):
            ax[4].text(0.01, yloc,  args.stats_label[i] + " = {0:.2f} mol/m$^2$/d".format(ass_stats[i][4]) , ha='left', va='center', transform=ax[1].transAxes, fontsize=14, bbox=dict(boxstyle="square", alpha=0.75, color='white' ))
            yloc = yloc - 0.12

    yloc = 0.93
    if args.stats_pc is not None:
        for i in range(0, len(args.stats_pc)):
            ax[7].text(0.01, yloc,  args.stats_label[i] + " = {0:.2f}%".format(pc_stats[i][4]) , ha='left', va='center', transform=ax[2].transAxes, fontsize=14, bbox=dict(boxstyle="square", alpha=0.75, color='white' ))
            yloc = yloc - 0.12


    if(args.tight_layout == True):
        plt.tight_layout(h_pad=args.hpad)

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile, bbox_inches = "tight")
    else:
        plt.show()



main()



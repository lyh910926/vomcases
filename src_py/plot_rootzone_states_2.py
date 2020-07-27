import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.colors import LogNorm
import pandas as pd
from datetime import datetime, timedelta, date


#file to prepare timeseries plot of VOM-results
#Vegetation Optimality Model (VOM)
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    #required input
    parser.add_argument("-i", "--input", help="results_daily (can be multiple)")
    parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-w", "--weather", help="dailyweather.prn")

    #optional input
    parser.add_argument("--i2015", help="results_daily AoB2015 ")
    parser.add_argument("--su_hourly", help="su_hourly.txt from the VOM")
    parser.add_argument("--su_hourly2015", help="su_hourly.txt from the VOM")

    parser.add_argument("--maxmod", help="results_daily max-values ")
    parser.add_argument("--minmod", help="results_daily min-values")
    parser.add_argument("--emp1", help="empirical solution 1")
    parser.add_argument("--emp2", help="empirical solution 2")
    parser.add_argument("--obs_gw", help="observations groundwater Howard Springs", nargs='+')
    parser.add_argument("--obs_sm", help="observations soil moisture all sites")
    parser.add_argument("--obs_evap", help="observations evaporation")
    parser.add_argument("--obs_ass", help="observations evaporation")
    parser.add_argument("--obsass_qc", help="observations evaporation")
    parser.add_argument("--obsevap_qc", help="observations evaporation")
    parser.add_argument("--pcobs", help="observations projective cover")
    parser.add_argument("--pcobsdates", help="dates projective cover")
    parser.add_argument("--soildata", help="soildata used for the VOM")
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--mf", help="multiplication factor for unit conversion", type=float, default = 1.0)
    parser.add_argument("--mf_obs", help="multiplication factor for unit conversion observations", type=float, default = 1.0)
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,5] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--i_cz", help="surface level, for groundwater plot", type=float )
    parser.add_argument("--i_zr", help="bottom level, for groundwater plot", type=float )
    parser.add_argument("--i_delz", help="layer thickness", type=float )
    parser.add_argument("--i_thetar", help="Van genuchten thetar AoB2015", type=float )
    parser.add_argument("--i_thetas", help="Van genuchten thetas AoB2015", type=float )
    parser.add_argument("--i_avg", help="Van genuchten alpha AoB2015", type=float )
    parser.add_argument("--i_nvg", help="Van genuchten n AoB2015", type=float )

    parser.add_argument("--i_cz2015", help="surface level, for groundwater plot", type=float )
    parser.add_argument("--i_zr2015", help="bottom level, for groundwater plot", type=float )
    parser.add_argument("--i_delz2015", help="bottom level, for groundwater plot", type=float )
    parser.add_argument("--i_thetar2015", help="Van genuchten thetar AoB2015", type=float )
    parser.add_argument("--i_thetas2015", help="Van genuchten thetas AoB2015", type=float )
    parser.add_argument("--i_avg2015", help="Van genuchten alpha AoB2015", type=float )
    parser.add_argument("--i_nvg2015", help="Van genuchten n AoB2015", type=float )
    parser.add_argument("--pars", help="parameter file, for plotting rooting depths" )
    parser.add_argument("--pars2015", help="parameter file Aob2015, for plotting rooting depths" )
    parser.add_argument("--depth", help="plot depth, default is water table" )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")
    parser.add_argument("--cblabel", help="label for colorbar", default=" ")
    parser.add_argument("--title", help="title", type=bool, default=False)
    parser.add_argument("--plot_prec", help="add precipation to figure", type=bool, default = False )
    parser.add_argument("--plot_cbar", help="add colorbar", type=bool, default = False )
    parser.add_argument("--use_roots", help="use rooting depths for water storage", type=lambda x: bool(int(x)),  default = False )
    parser.add_argument("--cbar_min", help="min value for colorbar", type=float, default = 0.2)
    parser.add_argument("--cbar_max", help="max value for colorbar", type=float, default = 2.6 )
    parser.add_argument("--legend", help="show legend", type=bool, default = False )
    parser.add_argument("--palette", help="color-palette", default = 'OrRd' )
    parser.add_argument("--xloc_title", help="location x title", type=float, default = 0.00 )
    parser.add_argument("--yloc_title", help="location y title", type=float, default = 1.05 )
    parser.add_argument("--ylim", help="limits y-axist", type=float, nargs='+', default = [-50,0] )
    parser.add_argument("--size_title", help="size of title", type=float, default = 20 )
    parser.add_argument("--print_depths", help="print rooting depths", type=lambda x: bool(int(x)),  default = False )

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



    #---------------------------------
    #load parameters
    if args.pars2015 is not None:
        params2015 = np.loadtxt(args.pars2015)

    #---------------------------------
    #load parameters
    if args.pars is not None:
        params = np.loadtxt(args.pars)

    #---------------------------------
    #load results
    data = np.genfromtxt(args.input, names=True)

    if( args.depth == "True"):
        zw_vals_tmp = -1.0*( args.i_cz - data["zw"])
    else:
        zw_vals_tmp = data["zw"]

    su_vals = (data["su_1"])
    ws_vals = data["ws"]
    zw_vals = zw_vals_tmp

    tmod = np.arange(datetime(int(data["fyear"][0]),int(data["fmonth"][0]),int(data["fday"][0])), 
                  datetime(int(data["fyear"][-1]),int(data["fmonth"][-1]),int(data["fday"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)

    #---------------------------------
    #load soildata
    nlayers = np.int(np.ceil(args.i_cz / args.i_delz))

    if args.soildata is not None:
        #values observations
        soildata = np.loadtxt(args.soildata) 
        theta_s = soildata[0,5]
        theta_r = soildata[0,6]
        theta_tmp = (su_vals * (theta_s - theta_r)) + theta_r
        theta_vals = theta_tmp
        delz = soildata[:,1]

    else:
        theta_s = args.i_thetas
        theta_r = args.i_thetar
        theta_tmp = (su_vals * (theta_s - theta_r)) + theta_r
        theta_vals = theta_tmp
        delz = np.repeat(args.i_delz, nlayers)

    #---------------------------------
    #soil moisture results


    #open file, count lines
    file = open(args.su_hourly) #mm/d     
    nlines = 0
    for line in file: 
        nlines = nlines + 1
    file.close()


    time = []
    su_data = np.zeros((nlines-1,nlayers))
    t = 0

    file = open(args.su_hourly)     

    #read per line as lines have different lengths
    for line in file: 
        tmp_data = line.split()
        if(t>0):
            if(len(tmp_data)>5):
                time.append(tmp_data[0:4])
                su_data[t-1,0:len(tmp_data[5:-1])] = np.float_(tmp_data[5:-1])
            else:
                time.append(tmp_data[0:4])
                su_data[t-1,0:len(tmp_data[5:-1])] = 0.0
        t = t + 1
    file.close()


    delz_sum = np.cumsum(delz)

    if(args.use_roots == True):
        val5 = list(filter(lambda i: round(i,2) < params[8], delz_sum))[-1]
    else:
        val5 = list(filter(lambda i: round(i,2) <= 5.00, delz_sum))[-1]
    ind5 = list(delz_sum).index(val5) + 1

    if(args.print_depths == True):
        print("Tree rooting depth:")
        print(val5)
        print(params[8])
        print("Untill layer:")
        print(ind5)

    if args.soildata is not None:
        theta_r = soildata[0:ind5,6]
        theta_s = soildata[0:ind5,5]
        alpha_vg = soildata[0:ind5,4]
        n_vg = soildata[0:ind5,3]
        m_vg = 1.0 -(1.0/n_vg)

        su = su_data[:, 0:ind5]
    else:
        theta_r = args.i_thetar
        theta_s = args.i_thetas
        alpha_vg = args.i_avg
        n_vg = args.i_nvg
        m_vg = 1.0 -(1.0/n_vg)

        su = su_data[:, 0:ind5]


    #loop over time
    ws5_hourly = np.zeros((nlines-1))
    watpot_hourly = np.zeros((nlines-1, len(su[0,:])  ))

    for t in range(0, len(su[:,0])):
        ws5_hourly[t] = np.sum((-su[t,:] * theta_r + \
                                su[t,:] *theta_s + theta_r) * delz[0:ind5] )
        watpot_hourly[t,:] = (1.0/alpha_vg) *  ( su[t,:] ** (-1.0/m_vg) - 1.0) ** (1/n_vg)

        


    startdate = str(time[0][0]) + "-" + str(time[0][1]) + "-" + str(time[0][2] )
    time_su = pd.date_range(startdate, periods = len(su_data[:,0]), freq='H')

    ws5_pd = pd.Series(ws5_hourly, index=time_su)
    watpot_hourly_pd = pd.DataFrame(watpot_hourly, index=time_su)

    #---------------------------------
    #load 2015 results
    if args.i2015 is not None:

        data2015 = np.genfromtxt(args.i2015, names=True)

        vals2015 = data2015["ys"]
        su_vals2015 = data2015["su_1"]
        theta_vals2015 = (su_vals2015 * (args.i_thetas2015 - args.i_thetar2015)) + args.i_thetar2015
        wsvals2015 = data2015["ws"]
        if( args.depth == "True"):
            vals2015 = -1*(args.i_cz2015 - vals2015)

        tmod2015 = np.arange(datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0])), 
                      datetime(int(data2015["year"][0]),int(data2015["month"][0]),int(data2015["day"][0]))+timedelta(days=len(vals2015) ), 
                      timedelta(days=1)).astype(datetime)

   #---------------------------------
    #soil moisture results 2015
    nlayers = np.int(np.ceil(args.i_cz2015 / args.i_delz2015))

    #open file, count lines
    file = open(args.su_hourly2015) #mm/d     
    nlines = 0
    for line in file: 
        nlines = nlines + 1
    file.close()


    time2015 = []
    su_data2015 = np.zeros((nlines-1,nlayers))

    t = 0

    file = open(args.su_hourly2015)     

    #read per line as lines have different lengths
    for line in file: 
        tmp_data = line.split()
        if(t>0):
            if(len(tmp_data)>5):
                time2015.append(tmp_data[0:4])
                su_data2015[t-1,0:len(tmp_data[5:-1])] = np.float_(tmp_data[5:-1])
            else:
                time2015.append(tmp_data[0:4])
                su_data2015[t-1,0:len(tmp_data[5:-1])] = 0.0
        t = t + 1
    file.close()

    delz2015 =  np.repeat(args.i_delz2015, nlayers)
    delz2015_sum = np.cumsum(delz2015)

    if(args.use_roots == True):
        val5 = list(filter(lambda i: round(i,2) < params2015[8], delz2015_sum))[-1]
    else:
        val5 = list(filter(lambda i: round(i,2) <= 5.00, delz2015_sum))[-1]
    ind5_2015 = list(delz2015_sum).index(val5) + 1

    if(args.print_depths == True):
        print("---")
        print("Tree rooting depth:")
        print(val5)
        print(params2015[8])
        print("Untill layer:")
        print(ind5_2015)

    #thetar2015 = soildata[0:ind5,6]
    #theta_s = soildata[0:ind5,5]
    alpha_vg2015 = args.i_avg2015
    n_vg2015 = args.i_nvg2015
    m_vg2015 = 1.0 -(1.0/n_vg2015)

    su2015 = su_data2015[:, 0:ind5_2015]

    #loop over time
    ws5_hourly2015 = np.zeros((nlines-1))
    watpot_hourly2015 = np.zeros((nlines-1, len(su2015[0,:])  ))

    for t in range(0, len(su2015[:,0])):
        ws5_hourly2015[t] = np.sum((-su2015[t,:] * args.i_thetar2015 + \
                                su2015[t,:] * args.i_thetas2015 + args.i_thetar2015) * delz[0:ind5_2015] )
        watpot_hourly2015[t,:] = (1.0/alpha_vg2015) *  ( su2015[t,:] ** (-1.0/m_vg2015) - 1.0) ** (1.0/n_vg2015)


    startdate = str(time2015[0][0]) + "-" + str(time2015[0][1]) + "-" + str(time2015[0][2] )
    time_su2015 = pd.date_range(startdate, periods = len(su_data2015[:,0]), freq='H')

    ws5_2015_pd = pd.Series(ws5_hourly2015, index=time_su2015)
    watpot_hourly2015_pd = pd.DataFrame(watpot_hourly2015, index=time_su2015)

    #print(watpot_hourly2015_pd)


    #---------------------------------
    #load observations groundwater
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
    if args.obs_sm is not None:
        #values observations
        obs_sm = ((np.loadtxt(args.obs_sm, usecols=2) ) ) 

        #date/times observations
        tobs_tmp = np.genfromtxt(args.obs_sm,usecols=0, dtype=np.str )
        tobs_sm = (pd.date_range(tobs_tmp[0], tobs_tmp[-1], freq='D') )


    #load weather data
    if args.weather is not None:
        weather_data = np.genfromtxt(args.weather, names=True)
        tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                      datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime)
        prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot
    #fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(args.figsize[0], args.figsize[1]), gridspec_kw={"width_ratios":[1,0.05]})        
    ax = axes.flat
        
    fig.delaxes(ax[1]) #remove last plot
    fig.delaxes(ax[3]) #remove last plot
    fig.delaxes(ax[5]) #remove last plot

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
        ax[0].plot(tmod, zw_vals, color=colors[0], label=args.labels[0], zorder=1)                
    else:
        ax[0].plot(tmod, zw_vals, color=palette(0), label=args.labels[0], zorder=1) 

 
 

    #plot rooting depths
    if args.pars is not None:
        if(args.depth == "True"):
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params[5], - params[5]], ":", lw=3, color='red', label='root depth trees')
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params[7],  -params[7]],":",lw=3,color='orange', label='root depth grasses')
        else:
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [args.i_cz- params[5], args.i_cz - params[5]], ":", lw=3, color='red', label='root depth trees')
            ax[0].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [args.i_cz - params[7], args.i_cz-params[7]],":",lw=3, color='orange', label='root depth grasses')


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
    ax[0].set_ylabel("Water table (m)", size=24  )
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
    #other plots

    #plot soil moisture results
    plot_flux_obs(tmod, theta_vals, ax[2], tobs_sm, obs_sm, "Soil moisture (m)", "b)", args.labels[0] ,yearstart, yearend) 

 
    #plot 2015 data
    if args.i2015 is not None:
        ax[2].plot(tmod2015, theta_vals2015, color='green', label='Schymanski et al. (2015)', zorder=2)


    ##############################################################
    #plot storage results
    plot_flux(ax[4], "Water storage (m)", "c)", yearstart, yearend ) 
    ax[4].plot(time_su, ws5_pd, color="red", label=args.labels[0], zorder=1) 

    #plot 2015 data
    if args.i2015 is not None:
        ax[4].plot(time_su2015, ws5_2015_pd, color='green', label='Schymanski et al. (2015)', zorder=2)

    ax[4].legend(prop={'size':15}, framealpha=1  )


    for tick in ax[4].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax[4].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    ##############################################################
    #plot water potentials
    #new VOM-results
    y = np.insert(-delz_sum[0:ind5],0,0)
    c1 = ax[6].pcolor(watpot_hourly_pd.index, y ,watpot_hourly_pd.values.T,norm=LogNorm(vmin=0.01, vmax=250), vmin=0.01, vmax=250, cmap = 'RdYlGn')

    ax[6].plot( [datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params[5], - params[5]], ":", lw=3, color='red', label='root depth trees')
    ax[6].plot( [datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params[7],  -params[7]],":",lw=3,color='orange', label='root depth grasses')

    ax[6].legend(prop={'size':15}, framealpha=1  )

    ax[6].set_ylabel("Depth (m)", size=20)
    for tick in ax[6].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax[6].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    #set colorbar
    cb = fig.colorbar(c1,cax=ax[7])
    cb.ax.tick_params(labelsize=14)
    cb.set_label("Matrix potential (m)", size=20)

    #Aob2015 results
    y2015 = np.insert(-delz2015_sum[0:ind5_2015],0,0)
    c2 = ax[8].pcolor(watpot_hourly2015_pd.index, y2015, watpot_hourly2015_pd.values.T, norm=LogNorm(vmin=0.01, vmax=250), vmin=0.01, vmax=250, cmap='RdYlGn'   )
    ax[8].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params2015[5],- params2015[5]], ":", lw=3, color='red', label='root depth trees')
    ax[8].plot([datetime(yearstart,1, 1), datetime( yearend ,12, 31)], [- params2015[7],- params2015[7]],":",lw=3, color='orange', label='root depth grasses')

    #set colorbar
    cb = fig.colorbar(c2,cax=ax[9])
    cb.ax.tick_params(labelsize=14)
    cb.set_label("Matrix potential (m)", size=20)

    ax[8].set_ylabel("Depth (m)", size=20)
    for tick in ax[8].xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax[8].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    #set labels/titles of plots
    if args.title is True:

        plot_label = ["a)","b)","c)", "d)", "e)", "f)"]
        label_ax = [0,2,4,6,8]
        for i in range(0, 5):
            ax[label_ax[i]].text(args.xloc_title, args.yloc_title, plot_label[i], ha='left', va='center', transform=ax[label_ax[i]].transAxes, fontsize=args.size_title)


    ax[2].legend(prop={'size':15}, framealpha=1  )
    ax[4].legend(prop={'size':15}, framealpha=1  )
    ax[6].legend(prop={'size':15}, framealpha=1  )
    ax[8].legend(prop={'size':15}, framealpha=1  )

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile, bbox_inches = "tight")
    else:
        plt.show()




def plot_flux_layers(ax, ylabel, plot_label, yearstart, yearend):
 


    end = vals.shape[1]
    for i in range(0, end):
        ax.plot(time, vals.iloc[:,i], color="red", label=args.labels[0], zorder=1) 


    ax.set_ylabel(ylabel, size=24  )
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    locator = mdate.YearLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))


    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))
    ax.set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    #ax.text(args.xloc_title, args.yloc_title, plot_label, ha='left', va='center')

    return ax



def plot_flux(ax, ylabel, plot_label, yearstart, yearend):
    

    ax.set_ylabel(ylabel, size=24  )
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    locator = mdate.YearLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))


    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))
    ax.set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    #ax.text(args.xloc_title, args.yloc_title, plot_label, ha='left', va='center')

    return ax

def plot_flux_obs(time, vals, ax, time_obs, vals_obs, ylabel, plot_label, labels, yearstart, yearend):
    

    ax.plot(time, vals, color="red", label=labels, zorder=1) 


    ax.set_ylabel(ylabel, size=24  )
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    locator = mdate.YearLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))

    ax.plot(time_obs, vals_obs, color='blue', label='Obs.', zorder=2)


    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y'))
    ax.set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    #ax.text(args.xloc_title, args.yloc_title, plot_label, ha='left', va='center')

    return ax
    

main()



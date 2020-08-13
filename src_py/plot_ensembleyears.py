#!/usr/bin/env python
# coding: utf-8

# # Does maximisation of net carbon profit explain vegetation behaviour in savanna sites along a precipitation gradient?
# 
# It was shown by Whitley et al. (2016) that six models that expliticly included land surface exchange and vegetation dynamics (i.e. terrestial biosphere models, TBM's) were not able to represent, especially, the wet season dynamics in savanna regions. This reflects generally the simplicity used in the current generation TBM's with regard to modelling vegetation, which becomes especially apparent in the more complex ecosystems of savannas. The understanding of these more complex interactions between vegetation, water and climate in savanna-sites is therefore crucial in order to improve modelling with TBM's. 
# Similar to the model inter-comparison presented by Whitley et al. (2016), in this study a coupled water-vegetation model (VOM, Schymanski et al. 2009) is applied in several savanna sites. In this case, vegetation properties are optimized for net carbon profit, instead of prescribing these.
# 
# The hypotheses tested are:
# 
# - Observed vegetation dynamics in tropical savanna sites can be explained by the maximization of Net Carbon Profit. 
# 
# - Optimization of vegetation properties for the Net Carbon Profit leads to reduced data requirements for Land Surface Models
# 
# - Carbon cost functions for roots, water transport system and foliage are valid along a precipitation gradient
# 
# 
# 

# # Results



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

    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--outfile", help="outputfile with plot")
    parser.add_argument("--vom", help="VOM results", nargs='+')
    parser.add_argument("--startyear_mod", help="first year to calculate long term means", nargs='+', type=int)
    parser.add_argument("--endyear_mod", help="last year to calculate long term means", nargs='+', type=int)
    parser.add_argument("--bess", help="bess input files", nargs='+')
    parser.add_argument("--bios2", help="bios2 input files", nargs='+')
    parser.add_argument("--lpjguess", help="lpj-guess input files, first all files with et, second gpp", nargs='+')
    parser.add_argument("--maespa", help="maespa input files", nargs='+')
    parser.add_argument("--spa", help="spa input files", nargs='+')
    parser.add_argument("--cable", help="cable input files", nargs='+')
    parser.add_argument("--sites", help="study sites, should correspond to the number and order of inputfiles", nargs='+')
    parser.add_argument("--whitley_sites", help="mask the study sites that are also used in Whitley et al.",nargs='+', type=int )
    parser.add_argument("--dingo_et", help="DINGO files evaporation", nargs='+')
    parser.add_argument("--dingo_gpp", help="DINGO files assimilation", nargs='+')
    parser.add_argument("--i2015", help="results_daily AoB2015 ")
    parser.add_argument("--sharex", help="share x-axis", dest="sharex", action='store_true' )
    parser.add_argument("--no_sharex", help="share x-axis", dest="sharex", action='store_false')
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [15,23] )
    parser.add_argument("--loc_legend", help="bbox_to_anchor", nargs='+', type=float, default = [15,23] )
    parser.add_argument("--lab_size", help="label fontsize", type=float, default = 18)
    parser.add_argument("--lw_vom", help="linewidth VOM", type=float, default = 3 )
    parser.add_argument("--lw_obs", help="linewidth observations", type=float, default = 3 )
    parser.add_argument("--title_pad", help="linewidth observations", type=float, default = 0 )
    parser.add_argument("--tight_layout", dest="tight_layout", action='store_true', help="tight layout")
    parser.add_argument("--no_tight_layout", dest="tight_layout", action='store_false', help="tight layout")
    parser.add_argument('--no-stepwise', dest='stepwise', action='store_false')
    parser.add_argument('--plot_et', dest='plot_et', action='store_true')
    parser.add_argument('--plot_le', dest='plot_et', action='store_false')
    parser.add_argument("--startyear", help="startyears for BESS modelruns", nargs='+')
    parser.set_defaults(tight_layout=False, plot_et = True,sharex = False)

    args = parser.parse_args()

    ###################################
    #some constants for conversions
    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 997             #[kg/m3]

    ###################################
    #read in data from Whitley et al. 
    whitley_sites = np.array(args.sites)[np.array(args.whitley_sites)==1]

    bess = dict()
    bess_dates = dict()
    bios2 = dict()
    bios2_dates = dict()
    lpjguess = dict()
    lpjguess_dates = dict()
    maespa = dict()
    maespa_dates = dict()
    spa = dict()
    spa_dates = dict()
    cable = dict()
    cable_dates = dict()

    for i in range(0, len(whitley_sites)):

        if(args.bess is not None):
            #read in data from BESS
            data_tmp, time_tmp = read_bess(args.bess[i])
            bess[whitley_sites[i]] = data_tmp
            bess_dates[whitley_sites[i]] = time_tmp

        if(args.bios2 is not None):
            #read in data from BIOS2
            data_tmp, time_tmp = read_bios2(args.bios2[i])
            bios2[whitley_sites[i]] = data_tmp
            bios2_dates[whitley_sites[i]] = time_tmp

        if(args.lpjguess is not None):
            #read in data from LPJ-GUESS, ET in W/m2, GPP in umol/m2/s
            data_tmp, data_tmp2, time_tmp = read_lpjguess(args.lpjguess[i], args.lpjguess[i+len(whitley_sites)])
            lpjguess[whitley_sites[i]] = [data_tmp, data_tmp2]
            lpjguess_dates[whitley_sites[i]] = time_tmp
    
        if(args.maespa is not None):
            #read in data from MAESPA, ET in W m-2, GPP in umol m-2 s-1
            data_tmp, time_tmp = read_maespa(args.maespa[i])
            maespa[whitley_sites[i]] = data_tmp
            maespa_dates[whitley_sites[i]] = time_tmp

        if(args.spa is not None):
            #read in data from SPA, ET in W m-2, GPP in mmol m-2 s-1
            data_tmp, time_tmp = read_spa(args.spa[i])
            spa[whitley_sites[i]] = data_tmp
            spa_dates[whitley_sites[i]] = time_tmp

        if(args.cable is not None):
            #read in data from CABLE, ET in kg/m^2/s, GPP in umol/m^2/s
            data_tmp, data_tmp2, time_tmp = read_cable(args.cable[i])
            cable[whitley_sites[i]] = [data_tmp, data_tmp2]
            cable_dates[whitley_sites[i]] = time_tmp

    ####################################################
    #load other data 

    dingo_le = dict()
    dingo_et = dict()
    dingo_le_dates = dict()
    dingo_dates = dict()
    dingo_gpp = dict()
    dingo_gpp_dates = dict()
    vom = dict()
    vom_dates = dict()
    for i in range(0, len(args.sites)):
        ea_tmp = np.loadtxt(args.dingo_et[i], usecols=2) #mm/d
        le_tmp = ea_tmp *  lat_heat_vapor * rho_w * 1000/(3600*24) 
        le_time =  np.genfromtxt(args.dingo_et[i],usecols=0, dtype=np.str )#mm/d
        le_time = pd.date_range(le_time[0], le_time[-1], freq='D')   
         
        leobs_pd =pd.Series(le_tmp, index=le_time)

        gpp_tmp = np.loadtxt(args.dingo_gpp[i], usecols=2) #mm/d
        gpp_obs = -1000000*gpp_tmp/ (3600*24)
        gpp_time =  np.genfromtxt(args.dingo_gpp[i],usecols=0, dtype=np.str )#mm/d
        gpp_time= pd.date_range(gpp_time[0], gpp_time[-1], freq='D')  

        gppobs_pd =pd.Series(gpp_obs, index=le_time)

        if(args.vom is not None):
            vom_tmp = np.genfromtxt(args.vom[i], names=True)
            etot = vom_tmp["esoil"] + vom_tmp["etmt"] + vom_tmp["etmg"] #m/d
            letot= etot[:]* lat_heat_vapor * rho_w * 1000 * 1000/(3600*24)
            gpptot = 1000000*(vom_tmp["assg"] + vom_tmp["asst"] )/ (3600*24)
            gpptot = gpptot[:]

            time = pd.date_range(datetime(int(vom_tmp["fyear"][3]),int(vom_tmp["fmonth"][0]),int(vom_tmp["fday"][0])), 
                  datetime(int(vom_tmp["fyear"][-1]),int(vom_tmp["fmonth"][-1]),int(vom_tmp["fday"][-1])), 
                  freq='D')

            dingo_dates[args.sites[i]] = le_time
            #print(le_time)
            dates_overlap = time.intersection(gpp_time)

            dingo_le[args.sites[i]] = leobs_pd[dates_overlap]
            dingo_et[args.sites[i]] = 3600*24*dingo_le[args.sites[i]]/ ( lat_heat_vapor * rho_w * 1000   ) #mm/d
            dingo_le_dates[args.sites[i]] = dates_overlap
            dingo_gpp[args.sites[i]] = gppobs_pd[dates_overlap]
            dingo_gpp_dates[args.sites[i]] = dates_overlap

            letot_pd = pd.Series(letot, index=time)
            ettot_pd = pd.Series(etot, index=time)
            gpptot_pd = pd.Series(gpptot, index=time)

            letot2 = letot_pd[dates_overlap]
            ettot2 = ettot_pd[dates_overlap]*1000
            gpptot2 = gpptot_pd[dates_overlap]

            #vom[args.sites[i]] = [letot[(time.year>=args.startyear_mod) & (time.year<=args.endyear_mod)], gpptot[(time.year>=args.startyear_mod) & (time.year<=args.endyear_mod)]]
            vom[args.sites[i]] = [letot2, gpptot2, ettot2]

            vom_dates[args.sites[i]] = dates_overlap
    



    ####################################################
    #start plotting
    fig, axes   = plt.subplots(nrows=len(args.sites), ncols=2, figsize=(args.figsize[0], args.figsize[1]), sharex=args.sharex, )
    ax = axes.flat

    iplot = 0
    #loop over study sites
    for isite in range(0, len(args.sites)): 

        #ensemble years from Whitley
        try:
            if(args.bess is not None):
                bess_le =  bess[args.sites[isite]][:,0] #W/m2   
                bess_et = 3600*24* bess_le / ( lat_heat_vapor * rho_w * 1000   ) #mm/d
                #BESS statistics
                dates_overlap = bess_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                bess_le_pd = pd.Series(bess_le, bess_dates[args.sites[isite]])
                bess_et_pd = pd.Series(bess_et, bess_dates[args.sites[isite]])

                bess_le7d = ensemble_year(bess_le_pd[dates_overlap], dates_overlap) #W/m2
                bess_et7d = ensemble_year(bess_et_pd[dates_overlap], dates_overlap) #mm/d

                if(args.plot_et):
                    ax[iplot].plot(range(0,367), bess_et7d, '--' , color="purple", linewidth=2, label = "BESS" )
                else:
                    ax[iplot].plot(range(0,367), bess_le7d, '--' , color="purple", linewidth=2, label = "BESS" )

            if(args.bios2 is not None):
                bios2_le = bios2[args.sites[isite]][:,3] #W/m2 
                bios2_et = 3600*24* bios2_le / ( lat_heat_vapor * rho_w * 1000   ) #mm/d

                dates_overlap = bios2_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                bios2_le_pd = pd.Series(bios2_le, bios2_dates[args.sites[isite]])
                bios2_et_pd = pd.Series(bios2_et, bios2_dates[args.sites[isite]])

                bios2_le7d = ensemble_year(bios2_le_pd[dates_overlap], dates_overlap) #W/m2
                bios2_et7d = ensemble_year(bios2_et_pd[dates_overlap], dates_overlap) #mm/d

                if(args.plot_et):
                    ax[iplot].plot(range(0,367), bios2_et7d, '--' , color="green", linewidth=2, label = "BIOS2" )
                else:
                    ax[iplot].plot(range(0,367), bios2_le7d, '--' , color="green", linewidth=2, label = "BIOS2" )

            if(args.lpjguess is not None):
                lpj_le = lpjguess[args.sites[isite]][0] # W/m2
                lpj_et = 3600*24* lpj_le / ( lat_heat_vapor * rho_w * 1000   ) #mm/d

                dates_overlap = lpjguess_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                lpj_le_pd = pd.Series(lpj_le, lpjguess_dates[args.sites[isite]])
                lpj_et_pd = pd.Series(lpj_et, lpjguess_dates[args.sites[isite]])

                lpj_le7d = ensemble_year(lpj_le_pd[dates_overlap], dates_overlap) # W/m2
                lpj_et7d = ensemble_year(lpj_et_pd[dates_overlap], dates_overlap) #mm/d

                if(args.plot_et):
                    ax[iplot].plot(range(0,367), lpj_et7d, '--' , color="lightblue", linewidth=2, label = "LPJ-GUESS" )
                else:
                    ax[iplot].plot(range(0,367), lpj_le7d, '--' , color="lightblue", linewidth=2, label = "LPJ-GUESS" )

            if(args.spa is not None):
                spa_le = spa[args.sites[isite]][:,1] # W/m2
                spa_le_pd_tmp = pd.Series(spa_le, spa_dates[args.sites[isite]])
                spa_le_pd = spa_le_pd_tmp.resample("D").sum()*30*60 #J/m2/d

                spa_et_pd = spa_le_pd/ ( lat_heat_vapor * rho_w * 1000   ) #mm/d


                dates_overlap = spa_et_pd.index.intersection(dingo_dates[args.sites[isite]])

                spa_le7d = ensemble_year(spa_le_pd[dates_overlap], dates_overlap) # W/m2
                spa_et7d = ensemble_year(spa_et_pd[dates_overlap], dates_overlap) #mm/d

                if(args.plot_et):
                    ax[iplot].plot(range(0,367), spa_et7d, '--' , color="pink", linewidth=2, label = "SPA" )
                else:
                    ax[iplot].plot(range(0,367), spa_le7d, '--' , color="pink", linewidth=2, label = "SPA" )

            if(args.cable is not None):
                cable_tmp = cable[args.sites[isite]][0] #kg/m^2/s
                cable_le = cable_tmp * lat_heat_vapor * 1000 * 1000  #W/m2
                cable_et = 3600*24* cable_le / ( lat_heat_vapor * rho_w * 1000   ) #mm/d

                cable_le_pd_tmp = pd.Series(cable_le, cable_dates[args.sites[isite]])
                cable_et_pd_tmp = pd.Series(cable_et, cable_dates[args.sites[isite]])

                cable_le_pd = cable_le_pd_tmp.resample("D").sum()*30*60 #J/m2/d
                cable_et_pd = cable_le_pd / ( lat_heat_vapor * rho_w * 1000)  #mm/d

                dates_overlap = cable_et_pd.index.intersection(dingo_dates[args.sites[isite]])

                cable_le7d = ensemble_year(cable_le_pd[dates_overlap], dates_overlap) 
                cable_et7d = ensemble_year(cable_et_pd[dates_overlap], dates_overlap) 

                if(args.plot_et):
                    ax[iplot].plot(range(0,367), cable_et7d, '--' , color="red", linewidth=2, label = "CABLE" )    
                else:
                    ax[iplot].plot(range(0,367), cable_le7d, '--' , color="red", linewidth=2, label = "CABLE" )    

            if(args.maespa is not None): 
                maespa_le = maespa[args.sites[isite]][:,1]
                maespa_le_pd_tmp = pd.Series(maespa_le, maespa_dates[args.sites[isite]])
                maespa_le_pd = maespa_le_pd_tmp.resample("D").sum()*30*60 #J/m2/d

                maespa_et_pd = maespa_le_pd/ ( lat_heat_vapor * rho_w * 1000   ) #mm/d


                dates_overlap = maespa_et_pd.index.intersection(dingo_dates[args.sites[isite]])


                maespa_le7d = ensemble_year(maespa_le_pd[dates_overlap], dates_overlap) #W m-2
                maespa_et7d = ensemble_year(maespa_et_pd[dates_overlap], dates_overlap) #W m-2

                if(args.plot_et):
                    ax[iplot].plot(range(0,367), maespa_et7d, '--' , color="gold", linewidth=2, label = "MAESPA" )
                else:
                    ax[iplot].plot(range(0,367), maespa_le7d, '--' , color="gold", linewidth=2, label = "MAESPA" )

        except KeyError:
            pass

        #load the AoB2015-data for HowardSprings
        if(args.sites[isite] == "Howard Springs"):
            if(args.i2015 is not None): 
                data2015 = np.genfromtxt(args.i2015, names=True)
                tmod2015 = pd.date_range(datetime(int(data2015["year"][3]),int(data2015["month"][0]),int(data2015["day"][0])), 
                      datetime(int(data2015["year"][-1]),int(data2015["month"][-1]),int(data2015["day"][-1])), 
                      freq='D')
            
                date2015 = []
                for iday in range(0,len(data2015["day"])):
                    date_tmp = datetime(int(data2015["year"][iday]),int(data2015["month"][iday]),int(data2015["day"][iday]))
                    date2015.append(date_tmp)

                #calculate total evaporation and convert to latent energy
                best_e2015 = data2015["esoil"] + data2015["etm_t"] + data2015["etm_g"]
                le_mod2015= best_e2015* lat_heat_vapor * rho_w * 1000 * 1000/(3600*24)
            
                best_e2015_pd  =  pd.Series(best_e2015, date2015)
                best_le2015_pd  =  pd.Series(le_mod2015, date2015)

                dates_overlap = best_e2015_pd.index.intersection(dingo_dates[args.sites[isite]])
  

                et7d2015 = ensemble_year(best_e2015_pd[dates_overlap]*1000, dates_overlap)
                le7d2015 = ensemble_year(best_le2015_pd[dates_overlap], dates_overlap)

                #determine ensemble year
                #le7d2015 = ensemble_year(le_mod2015, tmod2015[-3650:])
                #t7d2015 = ensemble_year(best_e2015[-3650:]*1000, tmod2015[-3650:])

                #plot
                if(args.plot_et):
                    ax[iplot].plot(range(0,367), et7d2015, '-', color="lightgreen", linewidth=3,label = "Schymanski et al. (2015)"   )
                else:
                    ax[iplot].plot(range(0,367), le7d2015, '-', color="lightgreen", linewidth=3,label = "Schymanski et al. (2015)"   )


        #ensemble year dingo and vom
        leo7d = ensemble_year(dingo_le[args.sites[isite]], dingo_le_dates[args.sites[isite]])
        eto7d = ensemble_year(dingo_et[args.sites[isite]], dingo_le_dates[args.sites[isite]])

        if(args.plot_et):
            ax[iplot].plot(range(0,367), eto7d, linestyle="-", dash_capstyle='butt',color="black", linewidth=args.lw_obs,label = "Flux tower"   )
        else:
            ax[iplot].plot(range(0,367), leo7d, linestyle="-", dash_capstyle='butt',color="black", linewidth=args.lw_obs,label = "Flux tower"   )

        if(args.vom is not None): 
            le7d = ensemble_year(vom[args.sites[isite]][0], vom_dates[args.sites[isite]])
            et7d = ensemble_year(vom[args.sites[isite]][2], vom_dates[args.sites[isite]])

            if(args.plot_et):
                ax[iplot].plot(range(0,367), et7d, '-' , color="green", linewidth=args.lw_vom, label = "VOM" )
            else:
                ax[iplot].plot(range(0,367), le7d, '-' , color="green", linewidth=args.lw_vom, label = "VOM" )
        #plot data and customize plot 


            

        ax[iplot].set_xlim([ 0, 366 ])  
        #ax[iplot].set_aspect(0.8)
        if(args.plot_et):
            ax[iplot].set_ylabel(r'ET (mm d$^{-1}$) ', size=args.lab_size  )
            ax[iplot].set_ylim([ 0, 8 ])
        else:
            ax[iplot].set_ylabel(r'LE (W m$^{-2}$) ', size=args.lab_size  )
            ax[iplot].set_ylim([ 0, 180 ])

            ax[iplot].set_yticks(range(0,200,20))
            ax[iplot].set_yticklabels(range(0,200,20))
        
        for tick in ax[iplot].xaxis.get_major_ticks():
            tick.label.set_fontsize(args.lab_size)
        for tick in ax[iplot].yaxis.get_major_ticks():
            tick.label.set_fontsize(args.lab_size)
        
        #ax[iplot].text(args.sites[isite] ,x=0.03, size=18, loc="left", pad = args.title_pad   )
        ax[iplot].text(0.03, 0.9, args.sites[isite], transform=ax[iplot].transAxes,  size=18)

        if( iplot == 10):
            ax[iplot].set_xlabel( r'Day of year', size=args.lab_size  )

        #############################################################################
        #plot GPP    
        iplot = iplot + 1

        #ensemble years from Whitley
        try:
            if(args.bess is not None):
                bess_gpp = bess[args.sites[isite]][:,1] #umol/m2/s   
                dates_overlap = bess_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])


                bess_gpp_pd = pd.Series(bess_gpp, bess_dates[args.sites[isite]])
                bess_gpp7d = ensemble_year(bess_gpp_pd[dates_overlap], dates_overlap) #umol/m2/s 

                ax[iplot].plot(range(0,367), bess_gpp7d, '--' , color="purple", linewidth=2, label = "BESS" )

            if(args.bios2 is not None):
                bios2_gpp = bios2[args.sites[isite]][:,4] #umol/m2/s
                dates_overlap = bios2_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                bios2_gpp_pd = pd.Series(bios2_gpp, bios2_dates[args.sites[isite]])
                bios2_gpp7d = ensemble_year(bios2_gpp_pd[dates_overlap], dates_overlap) #umol/m2/s

                ax[iplot].plot(range(0,367), bios2_gpp7d, '--' , color="green", linewidth=2, label = "BIOS2" )

            if(args.lpjguess is not None):
                dates_overlap = lpjguess_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                lpjguess_gpp_pd = pd.Series(lpjguess[args.sites[isite]][1], lpjguess_dates[args.sites[isite]])

                lpj_gpp7d = ensemble_year(lpjguess_gpp_pd[dates_overlap], dates_overlap) # umol/m2/s
                ax[iplot].plot(range(0,367), lpj_gpp7d, '--' , color="lightblue", linewidth=2, label = "LPJ-GUESS" )

            if(args.spa is not None):
                spa_gpp_pd = pd.Series(spa[args.sites[isite]][:,0], spa_dates[args.sites[isite]]) #umol m-2 s-1
                spa_gpp_pd = spa_gpp_pd.resample("D").sum()*30*60/(60*60*24) #umol/m2/s

                dates_overlap = spa_gpp_pd.index.intersection(dingo_dates[args.sites[isite]])

                dates_overlap = spa_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                spa_gpp7d = ensemble_year(spa_gpp_pd[dates_overlap], dates_overlap) # umol/m2/s
                ax[iplot].plot(range(0,367), -spa_gpp7d, '--' , color="pink", linewidth=2, label = "SPA" )

            if(args.cable is not None):
                dates_overlap = cable_dates[args.sites[isite]].intersection(dingo_dates[args.sites[isite]])

                cable_gpp_pd_tmp = pd.Series(cable[args.sites[isite]][1], cable_dates[args.sites[isite]])

                cable_gpp_pd = cable_gpp_pd_tmp.resample("D").sum()*30*60/(60*60*24)  #umol/m2/d
                #cable_gpp = cable_gpp/1000000 #mol/m2/d

                dates_overlap = cable_gpp_pd.index.intersection(dingo_dates[args.sites[isite]])

                cable_gpp7d = ensemble_year(cable_gpp_pd[dates_overlap], dates_overlap) #umol/m^2/s
                ax[iplot].plot(range(0,367), cable_gpp7d, '--' , color="red", linewidth=2, label = "CABLE" )

            if(args.maespa is not None):

                maespa_gpp_pd = pd.Series(maespa[args.sites[isite]][:,0], maespa_dates[args.sites[isite]]) #umol m-2 s-1
                maespa_gpp_pd = maespa_gpp_pd.resample("D").sum()*30*60/(60*60*24) #umol/m2/s

                dates_overlap = maespa_gpp_pd.index.intersection(dingo_dates[args.sites[isite]])

                maespa_gpp7d = ensemble_year(maespa_gpp_pd[dates_overlap], dates_overlap) #umol m-2 s-1
                ax[iplot].plot(range(0,367), maespa_gpp7d, '--' , color="gold", linewidth=2, label = "MAESPA" )


        except KeyError:
            pass

        #load AoB2015-data for HowardSprings
        if(args.sites[isite] == "Howard Springs"):
            if(args.i2015 is not None): 
                #determine total assimilation and convert units
                best_ass2015 = 1000000*(data2015["ass_t"] + data2015["ass_g"])/ (3600*24)
        
                date2015 = []
                for iday in range(0,len(data2015["day"])):
                    date_tmp = datetime(int(data2015["year"][iday]),int(data2015["month"][iday]),int(data2015["day"][iday]))
                    date2015.append(date_tmp)

                #determine ensemble year
                best_ass2015_pd  =  pd.Series(best_ass2015, date2015)
                dates_overlap = best_ass2015_pd.index.intersection(dingo_dates[args.sites[isite]])


                ass7d2015 = ensemble_year(best_ass2015_pd[dates_overlap], dates_overlap)
                ax[iplot].plot(range(0,367), ass7d2015, '-', color="lightgreen", linewidth=3,label = "Schymanski et al. (2015)"   )

        #ensemble year dingo and vom
        asso7d = ensemble_year(dingo_gpp[args.sites[isite]], dingo_gpp_dates[args.sites[isite]])


        #plot data and customize
        ax[iplot].plot(range(0,367), asso7d, '-', color="black", linewidth=args.lw_obs,label = "Flux tower"   )
        if(args.vom is not None):
            ass7d = ensemble_year(vom[args.sites[isite]][1], vom_dates[args.sites[isite]])
            ax[iplot].plot(range(0,367), ass7d, '-', color="green", linewidth=args.lw_vom, label = "VOM" )            
            
        ax[iplot].set_ylim([0 , 10 ])  
        ax[iplot].set_xlim([ 0, 366 ])  
        #ax[iplot].set_aspect(15)
    
        ax[iplot].set_ylabel( r'GPP ($\mu$mol m$^{-2}$ s$^{-1}$)', size=args.lab_size, labelpad=-3   )

        if( iplot == 11):
            ax[iplot].set_xlabel( r'Day of year', size=args.lab_size  )
        
        for tick in ax[iplot].xaxis.get_major_ticks():
            tick.label.set_fontsize(18)
        for tick in ax[iplot].yaxis.get_major_ticks():
            tick.label.set_fontsize(18)
        
        iplot = iplot + 1
    
    lines_labels = [ax[0].get_legend_handles_labels() ]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]

    ax[iplot-1].legend(lines, labels, loc='upper right', bbox_to_anchor=(args.loc_legend[0], args.loc_legend[1]),prop={'size':16})
    
    if args.tight_layout == True:
        plt.tight_layout()

    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()




def ensemble_year(vals, time):    
    
    ens = np.zeros([366])
    ens7d = np.zeros([367])    
    
    DOY = time.dayofyear[0:len(vals)] 

    for iday in range(0,366):
        ens[iday] = np.nanmean( vals[DOY == (iday+1)]  ) 
        
    #7-day running mean
    N = 7
    for iday in range(0,367):
        if iday > (366-N):
            ens7d[iday]  = np.nanmean( np.concatenate( (ens[iday:366], ens[0:(N-(366-iday))] )) )

        else:    
            ens7d[iday] = np.nanmean(ens[iday:(iday+N)])
            
            
    return ens7d


def read_bess(infile):

    data = np.loadtxt(infile, delimiter=",") 
    time = pd.date_range("01-01-2000", periods = len(data[:,0]), freq='D')

    return data, time

def read_bios2(infile):

    data = np.loadtxt(infile, delimiter=",") 
    time = pd.date_range(datetime(int(data[0,0]),int(data[0,1]),int(data[0,2])), 
              datetime(int(data[-1,0]),int(data[-1,1]),int(data[-1,2])),freq='D')

    return data, time

def read_lpjguess(infile_et, infile_gpp):
    data_et = np.loadtxt(infile_et, skiprows=1, usecols=3)
    data_gpp = np.loadtxt(infile_gpp, skiprows=1, usecols=3)
    time_tmp = np.loadtxt(infile_gpp, skiprows=1)
    time = pd.date_range(datetime(int(time_tmp[0,0]),int(time_tmp[0,1]),int(time_tmp[0,2])), 
              datetime(int(time_tmp[-1,0]),int(time_tmp[-1,1]),int(time_tmp[-1,2])),freq='D')

    return data_et, data_gpp, time

def read_maespa(infile):

    data = np.loadtxt(infile, delimiter=",", skiprows=3, usecols=(3,6))
    data[data == -9999.9] = np.nan
    data[data == -999] = np.nan
    data[data == -1388055] = np.nan
    time_tmp = np.loadtxt(infile, delimiter=",", dtype=np.str, skiprows=3, usecols=0)
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    return data, time

def read_spa(infile):
    data = np.loadtxt(infile, delimiter=",", skiprows=1, usecols=(1,3))
    time_tmp = np.loadtxt(infile, delimiter=",", dtype=np.str, skiprows=1, usecols=0)
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    return data, time

def read_cable(infile):
    ncfile = Dataset(infile)
    data_gpp = np.squeeze(ncfile.variables["GPP"]) # extract variable
    data_et = np.squeeze(ncfile.variables["Evap"]) # extract variable
    time_tmp = np.squeeze(ncfile.variables["time"]) # extract variable
    time_unit = ncfile.variables["time"].units
    time_tmp2 = num2date(time_tmp,units = time_unit,calendar = 'gregorian')
    time = pd.date_range(time_tmp2[0], time_tmp2[-1],freq='30min')

    return data_et, data_gpp, time


main()

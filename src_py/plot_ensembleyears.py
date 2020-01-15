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
from netCDF4 import Dataset
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--outfile", help="outputfile with plot")
    parser.add_argument("--vom", help="VOM results", nargs='+')
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
        #read in data from BESS
        data_tmp, time_tmp = read_bess(args.bess[i])
        bess[whitley_sites[i]] = data_tmp
        bess_dates[whitley_sites[i]] = time_tmp

        #read in data from BIOS2
        data_tmp, time_tmp = read_bios2(args.bios2[i])
        bios2[whitley_sites[i]] = data_tmp
        bios2_dates[whitley_sites[i]] = time_tmp

        #read in data from LPJ-GUESS, ET in W/m2, GPP in umol/m2/s
        data_tmp, data_tmp2, time_tmp = read_lpjguess(args.lpjguess[i], args.lpjguess[i+len(whitley_sites)])
        lpjguess[whitley_sites[i]] = [data_tmp, data_tmp2]
        lpjguess_dates[whitley_sites[i]] = time_tmp
    
        #read in data from MAESPA, ET in W m-2, GPP in umol m-2 s-1
        data_tmp, time_tmp = read_maespa(args.maespa[i])
        maespa[whitley_sites[i]] = data_tmp
        maespa_dates[whitley_sites[i]] = time_tmp

        #read in data from SPA, ET in W m-2, GPP in mmol m-2 s-1
        data_tmp, time_tmp = read_spa(args.spa[i])
        spa[whitley_sites[i]] = data_tmp
        spa_dates[whitley_sites[i]] = time_tmp

        #read in data from CABLE, ET in kg/m^2/s, GPP in umol/m^2/s
        data_tmp, data_tmp2, time_tmp = read_cable(args.cable[i])
        cable[whitley_sites[i]] = [data_tmp, data_tmp2]
        cable_dates[whitley_sites[i]] = time_tmp

    ####################################################
    #load other data 

    dingo_le = dict()
    dingo_le_dates = dict()
    dingo_gpp = dict()
    dingo_gpp_dates = dict()
    vom = dict()
    vom_dates = dict()
    for i in range(0, len(args.sites)):
        ea_tmp = np.loadtxt(args.dingo_et[i], usecols=2) #mm/d
        le_tmp = ea_tmp *  lat_heat_vapor * rho_w * 1000/(3600*24) 
        le_time =  np.genfromtxt(args.dingo_et[i],usecols=0, dtype=np.str )#mm/d
        le_time = pd.date_range(le_time[0], le_time[-1], freq='D')   
         
        gpp_tmp = np.loadtxt(args.dingo_gpp[i], usecols=2) #mm/d
        gpp_obs = -1000000*gpp_tmp/ (3600*24)
        gpp_time =  np.genfromtxt(args.dingo_gpp[i],usecols=0, dtype=np.str )#mm/d
        gpp_time= pd.date_range(gpp_time[0], gpp_time[-1], freq='D')  

        dingo_le[args.sites[i]] = le_tmp
        dingo_le_dates[args.sites[i]] = le_time
        dingo_gpp[args.sites[i]] = gpp_obs
        dingo_gpp_dates[args.sites[i]] = gpp_time

        vom_tmp = np.genfromtxt(args.vom[i], names=True)
        etot = vom_tmp["esoil"] + vom_tmp["etmt"] + vom_tmp["etmg"]
        letot= etot[-3650:]* lat_heat_vapor * rho_w * 1000 * 1000/(3600*24)
        gpptot = 1000000*(vom_tmp["assg"] + vom_tmp["asst"] )/ (3600*24)
        gpptot = gpptot[-3650:]

        time = pd.date_range(datetime(int(vom_tmp["fyear"][3]),int(vom_tmp["fmonth"][0]),int(vom_tmp["fday"][0])), 
              datetime(int(vom_tmp["fyear"][-1]),int(vom_tmp["fmonth"][-1]),int(vom_tmp["fday"][-1])), 
              freq='D')

        vom[args.sites[i]] = [letot, gpptot]
        vom_dates[args.sites[i]] = time[-3650:]
    



    ####################################################
    #start plotting
    fig, axes   = plt.subplots(nrows=6, ncols=2, figsize=(15, 23), sharex=True,gridspec_kw = {'wspace':0.2, 'hspace':-0.3} )
    ax = axes.flat

    iplot = 0
    #loop over study sites
    for isite in range(0, len(args.sites)): 

        #ensemble years from Whitley
        try:
            bess_le =  bess[args.sites[isite]][:,0] #W/m2            
            bess_le7d = ensemble_year(bess_le, bess_dates[args.sites[isite]]) #W/m2

            bios2_le = bios2[args.sites[isite]][:,3] #W/m2 
            bios2_le7d = ensemble_year(bios2_le, bios2_dates[args.sites[isite]]) #W/m2

            lpj_le7d = ensemble_year(lpjguess[args.sites[isite]][0], lpjguess_dates[args.sites[isite]]) # W/m2

            spa_le7d = ensemble_year(spa[args.sites[isite]][:,1], spa_dates[args.sites[isite]]) # W/m2

            cable_tmp = cable[args.sites[isite]][0] #kg/m^2/s
            cable_le = cable_tmp * lat_heat_vapor * 1000 * 1000  #W/m2
            cable_le7d = ensemble_year(cable_le, cable_dates[args.sites[isite]]) 
            
            maespa_le7d = ensemble_year(maespa[args.sites[isite]][:,1], maespa_dates[args.sites[isite]]) #W m-2

            #plot ensemble years
            ax[iplot].plot(range(0,367), bess_le7d, '--' , color="purple", linewidth=2, label = "BESS" )
            ax[iplot].plot(range(0,367), bios2_le7d, '--' , color="green", linewidth=2, label = "BIOS2" )
            ax[iplot].plot(range(0,367), lpj_le7d, '--' , color="lightblue", linewidth=2, label = "LPJ-GUESS" )
            ax[iplot].plot(range(0,367), spa_le7d, '--' , color="pink", linewidth=2, label = "SPA" )
            ax[iplot].plot(range(0,367), cable_le7d, '--' , color="red", linewidth=2, label = "CABLE" )       
            ax[iplot].plot(range(0,367), maespa_le7d, '--' , color="gold", linewidth=2, label = "MAESPA" )
            
        except KeyError:
            print("Litchfield")


        #load the AoB2015-data for HowardSprings
        if(args.sites[isite] == "Howard Springs"):
            data2015 = np.genfromtxt(args.i2015, names=True)
            tmod2015 = pd.date_range(datetime(int(data2015["year"][3]),int(data2015["month"][0]),int(data2015["day"][0])), 
                  datetime(int(data2015["year"][-1]),int(data2015["month"][-1]),int(data2015["day"][-1])), 
                  freq='D')
        
            #calculate total evaporation and convert to latent energy
            best_e2015 = data2015["esoil"] + data2015["etm_t"] + data2015["etm_g"]
            le_mod2015= best_e2015[-3650:]* lat_heat_vapor * rho_w * 1000 * 1000/(3600*24)
        
            #determine ensemble year
            le7d2015 = ensemble_year(le_mod2015, tmod2015[-3650:])
            
            #plot
            ax[iplot].plot(range(0,367), le7d2015, '-', color="lightgreen", linewidth=3,label = "Schymanski et al. (2015)"   )

        #ensemble year dingo and vom
        leo7d = ensemble_year(dingo_le[args.sites[isite]], dingo_le_dates[args.sites[isite]])
        le7d = ensemble_year(vom[args.sites[isite]][0], vom_dates[args.sites[isite]])

        #plot data and customize plot 
        ax[iplot].plot(range(0,367), leo7d, '-', color="black", linewidth=2,label = "Flux tower"   )
        ax[iplot].plot(range(0,367), le7d, '-' , color="green", linewidth=3, label = "VOM" )
            
        ax[iplot].set_ylim([ 0, 180 ])
        ax[iplot].set_xlim([ 0, 366 ])  
        ax[iplot].set_aspect(0.8)
        ax[iplot].set_ylabel(r'LE (W/m$^2$) ', size=18  )
        
        ax[iplot].set_yticks(range(0,200,20))
        ax[iplot].set_yticklabels(range(0,200,20))
        
        for tick in ax[iplot].xaxis.get_major_ticks():
            tick.label.set_fontsize(18)
        for tick in ax[iplot].yaxis.get_major_ticks():
            tick.label.set_fontsize(18)
        
        ax[iplot].set_title(args.sites[isite] , size=18, loc="left"   )
        if( iplot == 10):
            ax[iplot].set_xlabel( r'Day of year', size=18  )

        #############################################################################
        #plot GPP    
        iplot = iplot + 1

        #ensemble years from Whitley
        try:
            bess_gpp = bess[args.sites[isite]][:,1] #umol/m2/s   
            bess_gpp7d = ensemble_year(bess_gpp, bess_dates[args.sites[isite]]) #umol/m2/s 

            bios2_gpp = bios2[args.sites[isite]][:,4] #umol/m2/s
            bios2_gpp7d = ensemble_year(bios2_gpp, bios2_dates[args.sites[isite]]) #umol/m2/s

            lpj_gpp7d = ensemble_year(lpjguess[args.sites[isite]][1], lpjguess_dates[args.sites[isite]]) # umol/m2/s
            
            spa_gpp7d = ensemble_year(spa[args.sites[isite]][:,0], spa_dates[args.sites[isite]]) # umol/m2/s
            
            cable_gpp7d = ensemble_year(cable[args.sites[isite]][1], cable_dates[args.sites[isite]]) #umol/m^2/s
            
            maespa_gpp7d = ensemble_year(maespa[args.sites[isite]][:,0], maespa_dates[args.sites[isite]]) #umol m-2 s-1

            #plot ensemble years
            ax[iplot].plot(range(0,367), bess_gpp7d, '--' , color="purple", linewidth=2, label = "BESS" )
            ax[iplot].plot(range(0,367), bios2_gpp7d, '--' , color="green", linewidth=2, label = "BIOS2" )
            ax[iplot].plot(range(0,367), lpj_gpp7d, '--' , color="lightblue", linewidth=2, label = "LPJ-GUESS" )
            ax[iplot].plot(range(0,367), -spa_gpp7d, '--' , color="pink", linewidth=2, label = "SPA" )
            ax[iplot].plot(range(0,367), cable_gpp7d, '--' , color="red", linewidth=2, label = "CABLE" )
            ax[iplot].plot(range(0,367), maespa_gpp7d, '--' , color="gold", linewidth=2, label = "MAESPA" )
        
        except KeyError:
            print("Litchfield")

        #load AoB2015-data for HowardSprings
        if(args.sites[isite] == "Howard Springs"):

            #determine total assimilation and convert units
            best_ass2015 = 1000000*(data2015["ass_t"] + data2015["ass_g"])/ (3600*24)
    
            #determine ensemble year
            ass7d2015 = ensemble_year(best_ass2015[-3650:], tmod2015[-3650:])
            ax[iplot].plot(range(0,367), ass7d2015, '-', color="lightgreen", linewidth=3,label = "Schymanski et al. (2015)"   )

        #ensemble year dingo and vom
        asso7d = ensemble_year(dingo_gpp[args.sites[isite]], dingo_gpp_dates[args.sites[isite]])
        ass7d = ensemble_year(vom[args.sites[isite]][1], vom_dates[args.sites[isite]])

        #plot data and customize
        ax[iplot].plot(range(0,367), asso7d, '-', color="black", linewidth=2,label = "Flux tower"   )
        ax[iplot].plot(range(0,367), ass7d, '-', color="green", linewidth=3, label = "VOM" )            
            
        ax[iplot].set_ylim([0 , 10 ])  
        ax[iplot].set_xlim([ 0, 366 ])  
        ax[iplot].set_aspect(15)
    
        ax[iplot].set_ylabel( r'GPP ($\mu mol/m^2/s$)', size=18, labelpad=-3   )

        if( iplot == 11):
            ax[iplot].set_xlabel( r'Day of year', size=18  )
        
        for tick in ax[iplot].xaxis.get_major_ticks():
            tick.label.set_fontsize(18)
        for tick in ax[iplot].yaxis.get_major_ticks():
            tick.label.set_fontsize(18)
        
        iplot = iplot + 1
    
    lines_labels = [ax[0].get_legend_handles_labels() ]
    lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
    ax[iplot-1].legend(lines, labels, loc='upper right')
    
    plt.savefig(args.outfile, bbox_inches = "tight")
    #plt.show()




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
    time_tmp = [pd.to_datetime("2007-01-01 00:01:00") + pd.Timedelta(seconds=i) for i in time_tmp]
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    return data_et, data_gpp, time


main()

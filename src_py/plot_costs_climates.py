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
    parser.add_argument("--in1", help="parameter-files with cpccf-values",  nargs='+')
    parser.add_argument("--in2", help="parameter-files with cpccf-values",  nargs='+')
    parser.add_argument("--in3", help="parameter-files with cpccf-values",  nargs='+')
    parser.add_argument("--in4", help="parameter-files with cpccf-values",  nargs='+')
    parser.add_argument("--in5", help="parameter-files with cpccf-values",  nargs='+')
    parser.add_argument("--in6", help="parameter-files with cpccf-values",  nargs='+')

    parser.add_argument("--fpar1", help="fpar-based projective cover")
    parser.add_argument("--fpar2", help="fpar-based projective cover")
    parser.add_argument("--fpar3", help="fpar-based projective cover")
    parser.add_argument("--fpar4", help="fpar-based projective cover")
    parser.add_argument("--fpar5", help="fpar-based projective cover")
    parser.add_argument("--fpar6", help="fpar-based projective cover")
    parser.add_argument("--fpar_dates", help="dates for fpar-based projective cover")

    parser.add_argument("--weather1", help="dailyweather.prn")
    parser.add_argument("--weather2", help="dailyweather.prn")
    parser.add_argument("--weather3", help="dailyweather.prn")
    parser.add_argument("--weather4", help="dailyweather.prn")
    parser.add_argument("--weather5", help="dailyweather.prn")
    parser.add_argument("--weather6", help="dailyweather.prn")


    parser.add_argument("--silo1", help="raw data silo datadrill")
    parser.add_argument("--silo2", help="raw data silo datadrill")
    parser.add_argument("--silo3", help="raw data silo datadrill")
    parser.add_argument("--silo4", help="raw data silo datadrill")
    parser.add_argument("--silo5", help="raw data silo datadrill")
    parser.add_argument("--silo6", help="raw data silo datadrill")

    parser.add_argument("--lat1", help="latitude inputs", type=float)
    parser.add_argument("--lat2", help="latitude inputs", type=float)
    parser.add_argument("--lat3", help="latitude inputs", type=float)
    parser.add_argument("--lat4", help="latitude inputs", type=float)
    parser.add_argument("--lat5", help="latitude inputs", type=float)
    parser.add_argument("--lat6", help="latitude inputs", type=float)

    parser.add_argument("--startyear", help="first year to calculate long term means", type=int)
    parser.add_argument("--endyear", help="last year to calculate long term means", type=int)

    parser.add_argument("--sites", help="study sites, should correspond to the number and order of inputfiles", nargs='+')
    parser.add_argument("--cpccf_min", help="minimum value for the costfactor for water transport", type=float)
    parser.add_argument("--cpccf_max", help="maximum value for the costfactor for water transport", type=float)
    parser.add_argument("--cpccf_step", help="increment between costfactors", type=float)
    parser.add_argument("--figlab", help="figure labels", nargs='+')

    args = parser.parse_args()

    #plot parameters
    cpcff_vals = np.arange(args.cpccf_min, args.cpccf_max + args.cpccf_step, args.cpccf_step)
    site_name = args.sites

    cpcff_str = map(str, np.round(cpcff_vals,1) ) 
    cpcff_str = list(cpcff_str)

    cai_fpar = np.zeros(6)

    rn_ma = []
    EP_fao = []
    prec_all = []
    tmax_all = []
    drydur = []
    seas = []

    if args.fpar1 is not None:
        cai_fpar[0] = get_pc(args.fpar1, args.fpar_dates)
        rn1 = calc_netrad(args.weather1, args.lat1, args.startyear, args.endyear)
        rn1_ma = np.mean(rn1[ (rn1.index.year>=args.startyear) & (rn1.index.year<=args.endyear)].resample('A').sum() ) 
        EPfao1 = mean_annual_silo(args.silo1,  17)
        prec1 = mean_annual_vom_input(args.weather1, "Rain", args.startyear, args.endyear, "sum")
        tmax1 = mean_annual_vom_input(args.weather1, "TMax", args.startyear, args.endyear, "max")
        drydur1 = dry_season(args.weather1, args.startyear, args.endyear)
        seas1 = rainfall_seasonality(args.weather1, args.startyear, args.endyear, "mean_annual")

        rn_ma.append(rn1_ma)
        EP_fao.append(EPfao1)
        prec_all.append(prec1)
        tmax_all.append(tmax1)
        drydur.append(drydur1)
        seas.append(seas1)

    if args.fpar2 is not None:
        cai_fpar[1] = get_pc(args.fpar2, args.fpar_dates)
        rn2 = calc_netrad(args.weather2, args.lat2, args.startyear, args.endyear)
        rn2_ma = np.mean(rn1[ (rn2.index.year>=args.startyear) & (rn2.index.year<=args.endyear)].resample('A').sum() ) 
        EPfao2 = mean_annual_silo(args.silo2,  17)
        prec2 = mean_annual_vom_input(args.weather2, "Rain", args.startyear, args.endyear, "sum")
        tmax2 = mean_annual_vom_input(args.weather2, "TMax", args.startyear, args.endyear, "max")
        drydur2 = dry_season(args.weather2, args.startyear, args.endyear)
        seas2 = rainfall_seasonality(args.weather2, args.startyear, args.endyear, "mean_annual")

        rn_ma.append(rn2_ma)
        EP_fao.append(EPfao2)
        prec_all.append(prec2)
        tmax_all.append(tmax2)
        drydur.append(drydur2)
        seas.append(seas2)

    if args.fpar3 is not None:
        cai_fpar[2] = get_pc(args.fpar3, args.fpar_dates)
        rn3 = calc_netrad(args.weather3, args.lat3, args.startyear, args.endyear)
        rn3_ma =  np.mean(rn3[ (rn3.index.year>=args.startyear) & (rn3.index.year<=args.endyear)].resample('A').sum() )  
        EPfao3 = mean_annual_silo(args.silo3,  17)
        prec3 = mean_annual_vom_input(args.weather3, "Rain", args.startyear, args.endyear, "sum")
        tmax3 = mean_annual_vom_input(args.weather3, "TMax", args.startyear, args.endyear, "max")
        drydur3 = dry_season(args.weather3, args.startyear, args.endyear)
        seas3 = rainfall_seasonality(args.weather3, args.startyear, args.endyear, "mean_annual")

        rn_ma.append(rn3_ma)
        EP_fao.append(EPfao3)
        prec_all.append(prec3)
        tmax_all.append(tmax3)
        drydur.append(drydur3)
        seas.append(seas3)

    if args.fpar4 is not None:
        cai_fpar[3] = get_pc(args.fpar4, args.fpar_dates)
        rn4 = calc_netrad(args.weather4, args.lat4, args.startyear, args.endyear)
        rn4_ma =  np.mean(rn4[ (rn4.index.year>=args.startyear) & (rn4.index.year<=args.endyear)].resample('A').sum() )  
        EPfao4 = mean_annual_silo(args.silo4,  17)
        prec4 = mean_annual_vom_input(args.weather4, "Rain", args.startyear, args.endyear, "sum")
        tmax4 = mean_annual_vom_input(args.weather4, "TMax", args.startyear, args.endyear, "max")
        drydur4 = dry_season(args.weather4, args.startyear, args.endyear)
        seas4 = rainfall_seasonality(args.weather4, args.startyear, args.endyear, "mean_annual")

        rn_ma.append(rn4_ma)
        EP_fao.append(EPfao4)
        prec_all.append(prec4)
        tmax_all.append(tmax4)
        drydur.append(drydur4)
        seas.append(seas4)

    if args.fpar5 is not None:
        cai_fpar[4] = get_pc(args.fpar5, args.fpar_dates)
        rn5 = calc_netrad(args.weather5, args.lat5, args.startyear, args.endyear)
        rn5_ma =  np.mean(rn5[ (rn5.index.year>=args.startyear) & (rn5.index.year<=args.endyear)].resample('A').sum() )  
        EPfao5 = mean_annual_silo(args.silo5,  17)
        prec5 = mean_annual_vom_input(args.weather5, "Rain", args.startyear, args.endyear, "sum")
        tmax5 = mean_annual_vom_input(args.weather5, "TMax", args.startyear, args.endyear, "max")
        drydur5 = dry_season(args.weather5, args.startyear, args.endyear)
        seas5 = rainfall_seasonality(args.weather5, args.startyear, args.endyear, "mean_annual")

        rn_ma.append(rn5_ma)
        EP_fao.append(EPfao5)
        prec_all.append(prec5)
        tmax_all.append(tmax5)
        drydur.append(drydur5)
        seas.append(seas5)

    if args.fpar6 is not None:
        cai_fpar[5] = get_pc(args.fpar6, args.fpar_dates)
        rn6 = calc_netrad(args.weather6, args.lat6, args.startyear, args.endyear)
        rn6_ma =  np.mean(rn6[ (rn6.index.year>=args.startyear) & (rn6.index.year<=args.endyear)].resample('A').sum() )  
        EPfao6 = mean_annual_silo(args.silo6,  17)
        prec6 = mean_annual_vom_input(args.weather6, "Rain", args.startyear, args.endyear, "sum")
        tmax6 = mean_annual_vom_input(args.weather6, "TMax", args.startyear, args.endyear, "max")
        drydur6 = dry_season(args.weather6, args.startyear, args.endyear)
        seas6 = rainfall_seasonality(args.weather6, args.startyear, args.endyear, "mean_annual")

        rn_ma.append(rn6_ma)
        EP_fao.append(EPfao6)
        prec_all.append(prec6)
        tmax_all.append(tmax6)
        drydur.append(drydur6)
        seas.append(seas6)


    ##################################################################
    #determine best cpcff-values
    cpcff_best = np.zeros(6)

    if args.in1 is not None:
        cpcff_best[0] = best_cpcff(args.in1, cpcff_vals, cai_fpar[0])
    if args.in2 is not None:
        cpcff_best[1] = best_cpcff(args.in2, cpcff_vals, cai_fpar[1])
    if args.in3 is not None:
        cpcff_best[2] = best_cpcff(args.in3, cpcff_vals, cai_fpar[2])
    if args.in4 is not None:
        cpcff_best[3] = best_cpcff(args.in4, cpcff_vals, cai_fpar[3])
    if args.in5 is not None:
        cpcff_best[4] = best_cpcff(args.in5, cpcff_vals, cai_fpar[4])
    if args.in6 is not None:
        cpcff_best[5] = best_cpcff(args.in6, cpcff_vals, cai_fpar[5])


    ##################################################################
    #make plot
    symbols = ['s', '.', '>', '8', 'P','*']
    colors = ['red', 'green', 'blue',  'gray', 'black', 'orange']

    if args.figlab is not None:
        fig_lab = args.figlab
    else:
        fig_lab = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)']


    xlabel = ["Mean Ann. Prec. (mm year$^{-1}$)",
              r"Mean Net rad. (MJ m$^{-2}$ year$^{-1}$)",
              "Pot. Evap. (mm year$^{-1})$",
              "Mean dry season length (days)",
              "Mean max. temp. ( $^o$C)",
              "Rain seasonality (-)"        
             ]

    fig=plt.figure(figsize=(16, 5), dpi= 80, facecolor='w', edgecolor='k')
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 16)) 
    ax = axes.flat

    isite = 0

    for site in args.sites:


        ax[0].scatter( prec_all[isite], cpcff_best[isite], marker=symbols[isite], color=colors[isite] , s=160, label=site, zorder=2 )     
        ax[1].plot(rn_ma[isite], cpcff_best[isite],  marker=symbols[isite], color=colors[isite] , markersize=14, label=site)     
        ax[2].plot(EP_fao[isite], cpcff_best[isite],  marker=symbols[isite], color=colors[isite] , markersize=14, label=site)     
        ax[3].plot(drydur[isite], cpcff_best[isite],  marker=symbols[isite], color=colors[isite] , markersize=14, label=site)     
        ax[4].plot(tmax_all[isite], cpcff_best[isite],  marker=symbols[isite], color=colors[isite] , markersize=14, label=site)     
        ax[5].plot( seas[isite], cpcff_best[isite], marker=symbols[isite], color=colors[isite] , markersize=14, label=site)     

        isite = isite + 1



    ax[0].legend(prop={'size':10})

    for i in range(0,6):

        ax[i].set_xlabel(xlabel[i], size=16 )  
        ax[i].tick_params(axis='both', which='major', labelsize=16)
        ax[i].set_yticks(cpcff_vals)
        ax[i].set_yticklabels(cpcff_str)
        ax[i].grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)
        ax[i].tick_params(axis='both', which='major', labelsize=16)

        ax[i].set_ylabel(r'c$_{rv}$  ($\mu$mol m$^3$ s$^{-1}$)', size=16 )  
        ax[i].text(-0.15, 1.07, fig_lab[i], transform=ax[i].transAxes,  size=20)

    plt.tight_layout()
        
    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()


def get_pc(fparfile, fpardates):

    fpar = pd.read_csv(fparfile, usecols=[3],  header=None, na_values=-999, squeeze=True )
    fpar_dates = np.genfromtxt(fpardates, dtype='str', delimiter=',')

    #make a pandas datetime series
    datetime_fpar = pd.to_datetime(fpar_dates[:,1], format="%Y%m")

    #make a pandas index
    index = pd.DatetimeIndex( datetime_fpar)

    #replace index
    fpar.index = index

    #make daily series
    #fpar_daily = fpar.resample('D').ffill()

    #calculate means per month
    means=np.zeros((12))

    for i_month in np.arange(0,12):
        month = i_month + 1
        means[i_month] = np.nanmean(fpar[fpar.index.month == month] )

    const_cov = np.min(means)
 

    ###################################
    #convert to projective cover

    return const_cov/0.95

def mean_annual(inputfile, var ,startyear, endyear, method):

    #load data
    data = np.genfromtxt(inputfile, names=True)

    #make numpy arrays in the right units
    vals = np.array(data[var]) #mm/d

    #create series of pandas time
    tmod = np.arange(datetime(int(data['fyear'][0]),int(data['fmonth'][0]),int(data['fday'][0])), 
                      datetime(int(data['fyear'][-1]),int(data['fmonth'][-1]),int(data['fday'][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime)
                    
    #make pandas series
    vals_pd = pd.Series(vals, index=tmod)
                    
    if(method == "sum"):
        vals_ma = np.mean(vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)].resample('A').sum() ) 
    if(method == "max"):
        vals_ma = np.mean(vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)].resample('A').max() ) 
    if(method == "min"):
        vals_ma = np.mean(vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)].resample('A').min() )

    
    return vals_ma      
                


def calc_netrad( weatherdata_file, lat, startyear, endyear ):
    
    #calculate net radiation, following FAO

    weatherdata = np.genfromtxt(weatherdata_file, names=True  )    
    
    #constants
    sigma = 4.903*10**-9 #Stefan-Boltzman constant [MJ K-4 m-2 day-1]
    Gsc = 0.0820 #solar constant [MJ m-2 hour-1]
    n = 10 #220/31 #sunshine hours
    N = 10 #maximum sunshine hours
    
    #get data from VOM-dailyweather
    Rs = weatherdata["Radn"]    # incoming solar radiation [MJ m-2 day-1]
    Tmax = weatherdata["TMax"]  # Celsius
    Tmin = weatherdata["TMin"]  # Celsius
    ea = weatherdata["VP"] /10  # kPa

    #define time and dates
    time = np.arange(datetime(int(weatherdata['Year'][0]),int(weatherdata['Month'][0]),int(weatherdata['Day'][0])), 
                  datetime(int(weatherdata['Year'][-1]),int(weatherdata['Month'][-1]),int(weatherdata['Day'][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    time_pd = pd.date_range(time[0],periods=len( time ), freq='D')

    #day of year
    J = time_pd.dayofyear
    
    #inverse relative distance Earth-Sun
    dr =  1 + 0.033*np.cos(2*np.pi*J/365)  # [m?]

    phi=  (np.pi/180) * lat   #latitude [rad]
    
    #solar declination
    delta= 0.409*np.sin( (2*J*np.pi/365)  - 1.39 ) #[rad]
    
    #sunset hour angle
    ws =  np.arccos(-np.tan(phi)*np.tan(delta))

    #extraterrestrial radiation
    part1 = (24*60/np.pi) * Gsc * dr 
    part2 = ws*np.sin(phi)*np.sin(delta)
    part3 = np.cos(phi)*np.cos(delta)*np.sin(ws) 

    Ra =  part1*(part2+part3)  #[MJ m-2 hr-1]


    #Rso = Ra*z*0.75*2*10**-5
    Rso = Ra*(0.25+0.5*(n/N)) #clear-sky solar radiation [MJ m-2 day-1]

    Rns = (1-0.23) * Rs # shortwave radiation

    part1 = sigma*((Tmax+273.16)**4 + (Tmin+273.16)**4)/2
    part2 = 0.34-0.14*np.sqrt(ea)
    part3 = 1.35*Rs/Rso -0.35

    Rnl = part1 * part2 * part3 #net longwave radiation [MJ m-2 day-1]

    Rn = Rns - Rnl
    
    Rn_pd = pd.Series(Rn, index = time_pd)
    Rn_pd = Rn_pd[ (Rn_pd.index.year>=startyear) & (Rn_pd.index.year<=endyear)]
    
    return Rn_pd

def aridity(rn, input_vom, startyear, endyear):
       
    
    #input: results vom
    #precipitation
    #potential evaporation
    #net radiation
    
    weatherdata = np.genfromtxt(input_vom, names=True  )

    #define time and dates
    time = np.arange(datetime(int(weatherdata['Year'][0]),int(weatherdata['Month'][0]),int(weatherdata['Day'][0])), 
                  datetime(int(weatherdata['Year'][-1]),int(weatherdata['Month'][-1]),int(weatherdata['Day'][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    time_pd = pd.date_range(time[0],periods=len( time ), freq='D')
    
    
    lat_heat_vapor = 2.45   #[MJ/kg] 
    rho_w = 1000             #[kg/m3]

    prec = pd.Series(weatherdata['Rain'], index=time_pd)
    prec = prec[ (prec.index.year>=startyear) & (prec.index.year<=endyear)]
    #rn = np.array(rn)  
    ep = 1000*rn/(lat_heat_vapor*rho_w) #mm/d
    Lp = prec * lat_heat_vapor 
    
    
    #in terms of water, prec as base
    EpP = np.sum(ep) / np.sum(prec) 
        
    #in terms of energy  
    RnLp = np.sum(rn) / np.sum(Lp) #same as Ep/P    

    return EpP, RnLp

def mean_annual_silo(meteofile, column):

    meteo_data = pd.read_csv(meteofile, skiprows = 43, delimiter=r"\s+", header=None )

   #make a pandas datetime series
    pddatetime = pd.to_datetime( meteo_data[2], format="%d-%m-%Y")

    #make a pandas index
    index = pd.DatetimeIndex( pddatetime)

    #replace index
    meteo_data.index = index
    
    #extract the variable of interest
    var = meteo_data[:][column]
    
    #print(var.resample("Y").sum())
    #calculate the mean annual value
    MA_var = np.mean(var.resample("Y").sum())
    
    return MA_var

def mean_annual_vom_input(dailyweatherfile, var, startyear, endyear, method):


    weatherdata = np.genfromtxt(dailyweatherfile, names=True  )

    #define time and dates
    time = np.arange(datetime(int(weatherdata['Year'][0]),int(weatherdata['Month'][0]),int(weatherdata['Day'][0])), 
                  datetime(int(weatherdata['Year'][-1]),int(weatherdata['Month'][-1]),int(weatherdata['Day'][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    time_pd = pd.date_range(time[0],periods=len( time ), freq='D')


    vals = pd.Series(weatherdata[var], index=time_pd)
    vals = vals[ (vals.index.year>=startyear) & (vals.index.year<=endyear)]

    if(method == "sum"):
        MA_val = np.mean(vals.resample("Y").sum())

    if(method == "max"):
        MA_val = np.mean(vals.resample("Y").max())

    return MA_val



def rainfall_seasonality(inputfile,startyear, endyear, method):

    #load data
    data = np.genfromtxt(inputfile, names=True)

    #make numpy arrays in the right units
    vals = np.array(data["Rain"]) #mm/d

    #create series of pandas time
    tmod = np.arange(datetime(int(data['Year'][0]),int(data['Month'][0]),int(data['Day'][0])), 
                      datetime(int(data['Year'][-1]),int(data['Month'][-1]),int(data['Day'][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime)
                    
    #make pandas series
    vals_pd = pd.Series(vals, index=tmod)
    vals_pd = vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)]

    
    if(method == "mean_annual"):
        Pma = np.mean(vals_pd.resample('A').sum() ) 
        Pmonth = vals_pd.resample('M').sum()
        Pmm = np.zeros(12) #mean monthly rainfall
        for i in range(1,13):
            Pmm_tmp = np.mean(Pmonth[Pmonth.index.month == i])
            Pmm[i-1] = Pmm_tmp


        seasonality =  (1/Pma) * np.sum( np.abs(Pmm - (Pma / 12)) )
        
    if(method == "annual_values"):
        Pma = vals_pd.resample('A').sum() 
        Pmonth = vals_pd.resample('M').sum()
        Pmm = np.zeros( (len(vals_pd.resample('A').sum()),12)) #mean monthly rainfall
        for i in range(1,13):
            Pmm_tmp = Pmonth[Pmonth.index.month == i]            
            Pmm[:, i-1] = Pmm_tmp

        seasonality = np.zeros(len(Pma))
        for i in range(0, len(Pma) ):
            seasonality[i] =  (1/Pma[i]) * np.sum( np.abs(Pmm[i,:] - (Pma[i] / 12)) )
        
    return seasonality      
                

def dry_season(inputfile,startyear, endyear):

    #load data
    data = np.genfromtxt(inputfile, names=True)

    #make numpy arrays in the right units
    vals = np.array(data["Rain"]) #mm/d

    #create series of pandas time
    tmod = np.arange(datetime(int(data['Year'][0]),int(data['Month'][0]),int(data['Day'][0])), 
                      datetime(int(data['Year'][-1]),int(data['Month'][-1]),int(data['Day'][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime)
                    
    #make pandas series
    vals_pd = pd.Series(vals, index=tmod)
    vals_pd = vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)]
    
    

    dry_period = np.zeros( len(np.arange(startyear,endyear+1))) #yearly dry periods
    i = 0
    for iyear in np.arange(startyear,endyear+1):
        tmp = vals_pd[vals_pd.index.year == iyear]
        dry_period[i] = tmp.value_counts().max()
        i = i + 1
    
        
    dryseason_duration =  np.mean(dry_period)
        
    return dryseason_duration      



def best_cpcff(parfiles, cpcff_vals, cai_fpar):
    

        i_cpcff = 0
        err = np.zeros((len(cpcff_vals)))

        #loop over values and calculate errors in pc-dry 
        for cpcff in  cpcff_vals: 
            try:
                params = np.loadtxt(parfiles[i_cpcff])

                cai = params[4]              
                err[i_cpcff] = np.abs(cai - cai_fpar)


            except OSError:
                print('file not found')
             
            i_cpcff = i_cpcff + 1
            
            
        cpcff_best = cpcff_vals[err[:] == min(err[:])]

        return cpcff_best











main()



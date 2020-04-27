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
    parser.add_argument("--evap_obs", help="observations of evaporation",  nargs='+')
    parser.add_argument("--ass_obs", help="observations of assimilation",  nargs='+')

    parser.add_argument("--pred_cover", help="results with predicted vegetation cover",  nargs='+')
    parser.add_argument("--pres_cover", help="results with prescribed vegetation cover",  nargs='+')


    parser.add_argument("--startyear_obs", help="first year to calculate long term means for the observations", nargs='+', type=int)
    parser.add_argument("--endyear_obs", help="last year to calculate long term means for the observations", nargs='+', type=int)

    parser.add_argument("--startyear_mod", help="first year to calculate long term means", nargs='+', type=int)
    parser.add_argument("--endyear_mod", help="last year to calculate long term means", nargs='+', type=int)

    parser.add_argument("--sites", help="study sites, should correspond to the number and order of inputfiles", nargs='+')
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [15,20] )
    parser.add_argument("--labsize", help="label size", type=float, default = 8)
    parser.add_argument("--label_pad", help="label pad", type=float, default = 50)
    parser.add_argument("--only_meanannual",dest="only_meanannual", action='store_true', help="only plot mean annual values")
    parser.add_argument("--fig_lab", dest="fig_lab", action='store_true', help="plot labels of subplots")
    parser.add_argument("--no_fig_lab", dest="fig_lab", action='store_false', help="do not plot labels of subplots")
    parser.set_defaults(fig_lab=True, only_meanannual=False)

    args = parser.parse_args()



    etot_dingo = np.zeros( (6)  )
    ewet_dingo = np.zeros( (6)  )
    edry_dingo = np.zeros( (6)  )
    edry2wet_dingo = np.zeros( (6)  )
    ewet2dry_dingo = np.zeros( (6)  )

    #mean annual evaporation
    for i in range(0,len(args.evap_obs) ):
        tmp = mean_annual_dingo(args.evap_obs[i], args.startyear_obs[i], args.endyear_obs[i], 12, 3, 5, 9 )
        etot_dingo[i] = tmp[0]
        ewet_dingo[i] = tmp[1]
        edry_dingo[i] = tmp[2]
        edry2wet_dingo[i] = tmp[3]
        ewet2dry_dingo[i] = tmp[4]

    gpptot_dingo = np.zeros( (6)  )
    gppwet_dingo = np.zeros( (6)  )
    gppdry_dingo = np.zeros( (6)  )
    gppwet2dry_dingo = np.zeros( (6)  )

    #mean annual assimilation
    for i in range(0,len(args.ass_obs)):
        tmp = mean_annual_dingo(args.ass_obs[i], args.startyear_obs[i], args.endyear_obs[i], 12, 3, 5, 9 )
        gpptot_dingo[i] = tmp[0]*-1.0
        gppwet_dingo[i] = tmp[1]*-1.0
        gppdry_dingo[i] = tmp[2]*-1.0
        gppwet2dry_dingo[i] = tmp[4]*-1.0

    #mean annual fluxes for predicted cover
    esoil_ma = np.zeros( (6)  )    
    etmt_ma = np.zeros( (6)  )
    etmg_ma = np.zeros( (6)  )
    assg_ma = np.zeros( (6)  )
    asst_ma = np.zeros( (6)  )

    esoil_wet = np.zeros( (6)  )
    etmt_wet = np.zeros( (6)  )
    etmg_wet = np.zeros( (6)  )
    assg_wet = np.zeros( (6)  )
    asst_wet = np.zeros( (6)  )

    esoil_dry = np.zeros( (6)  )
    etmt_dry = np.zeros( (6)  )
    etmg_dry = np.zeros( (6)  )
    assg_dry = np.zeros( (6)  )
    asst_dry = np.zeros( (6)  )

    esoil_wet2dry = np.zeros( (6)  )
    etmt_wet2dry = np.zeros( (6)  )
    etmg_wet2dry = np.zeros( (6)  )
    assg_wet2dry = np.zeros( (6)  )
    asst_wet2dry = np.zeros( (6)  )

    for i in range(0,len(args.pred_cover)):
        tmp = fluxpartitions(args.pred_cover[i], args.startyear_mod[i], args.endyear_mod[i], 12, 3, 5, 9 )

        esoil_ma[i] = tmp[0][0]
        etmt_ma[i] = tmp[0][1]
        etmg_ma[i] = tmp[0][2]
        assg_ma[i] = tmp[0][3]
        asst_ma[i] = tmp[0][4]

        esoil_wet[i] = tmp[1][0]
        etmt_wet[i] = tmp[1][1]
        etmg_wet[i] = tmp[1][2]
        assg_wet[i] = tmp[1][3]
        asst_wet[i] = tmp[1][4]

        esoil_dry[i] = tmp[2][0]
        etmt_dry[i] = tmp[2][1]
        etmg_dry[i] = tmp[2][2]
        assg_dry[i] = tmp[2][3]
        asst_dry[i] = tmp[2][4]

        esoil_wet2dry[i] = tmp[4][0]
        etmt_wet2dry[i] = tmp[4][1]
        etmg_wet2dry[i] = tmp[4][2]
        assg_wet2dry[i] = tmp[4][3]
        asst_wet2dry[i] = tmp[4][4]

    #mean annual fluxes for prescribed cover
    esoil_ma_pc = np.zeros( (6)  )
    etmt_ma_pc = np.zeros( (6)  )
    etmg_ma_pc = np.zeros( (6)  )
    assg_ma_pc = np.zeros( (6)  )
    asst_ma_pc = np.zeros( (6)  )

    esoil_wet_pc = np.zeros( (6)  )
    etmt_wet_pc = np.zeros( (6)  )
    etmg_wet_pc = np.zeros( (6)  )
    assg_wet_pc = np.zeros( (6)  )
    asst_wet_pc = np.zeros( (6)  )

    esoil_dry_pc = np.zeros( (6)  )
    etmt_dry_pc = np.zeros( (6)  )
    etmg_dry_pc = np.zeros( (6)  )
    assg_dry_pc = np.zeros( (6)  )
    asst_dry_pc = np.zeros( (6)  )

    esoil_wet2dry_pc = np.zeros( (6)  )
    etmt_wet2dry_pc = np.zeros( (6)  )
    etmg_wet2dry_pc = np.zeros( (6)  )
    assg_wet2dry_pc = np.zeros( (6)  )
    asst_wet2dry_pc = np.zeros( (6)  )

    for i in range(0,len(args.pres_cover)):
        tmp = fluxpartitions(args.pres_cover[i], args.startyear_mod[i], args.endyear_mod[i], 12, 3, 5, 9 )

        esoil_ma_pc[i] = tmp[0][0]
        etmt_ma_pc[i] = tmp[0][1]
        etmg_ma_pc[i] = tmp[0][2]
        assg_ma_pc[i] = tmp[0][3]
        asst_ma_pc[i] = tmp[0][4]

        esoil_wet_pc[i] = tmp[1][0]
        etmt_wet_pc[i] = tmp[1][1]
        etmg_wet_pc[i] = tmp[1][2]
        assg_wet_pc[i] = tmp[1][3]
        asst_wet_pc[i] = tmp[1][4]

        esoil_dry_pc[i] = tmp[2][0]
        etmt_dry_pc[i] = tmp[2][1]
        etmg_dry_pc[i] = tmp[2][2]
        assg_dry_pc[i] = tmp[2][3]
        asst_dry_pc[i] = tmp[2][4]

        esoil_wet2dry_pc[i] = tmp[4][0]
        etmt_wet2dry_pc[i] = tmp[4][1]
        etmg_wet2dry_pc[i] = tmp[4][2]
        assg_wet2dry_pc[i] = tmp[4][3]
        asst_wet2dry_pc[i] = tmp[4][4]



    ##################################################################
    #make plot
    if args.fig_lab is True:
        plot_label = [ "a)","b)","c)","d)","e)","f)", "g)", "h)" ]
    else: 
        plot_label = [ " "," "," "," "," "," ", " ", " " ]

    if( args.only_meanannual == True):
        fig, axes   = plt.subplots(nrows=1, ncols=2, figsize=(args.figsize[0], args.figsize[1]), sharex = True )
        ax = axes.flat

        evap_barplot(esoil_ma, etmt_ma, etmg_ma, esoil_ma_pc, etmt_ma_pc, etmg_ma_pc, etot_dingo, ax[0], plot_label[0], args.sites, args.label_pad, -40, args.labsize)
        ass_barplot(assg_ma, asst_ma, assg_ma_pc, asst_ma_pc, gpptot_dingo, ax[1], plot_label[1], args.sites, args.label_pad, -5,  args.labsize)

    else:
        fig, axes   = plt.subplots(nrows=4, ncols=2, figsize=(args.figsize[0], args.figsize[1]), sharex = True )
        ax = axes.flat

        evap_barplot(esoil_ma, etmt_ma, etmg_ma, esoil_ma_pc, etmt_ma_pc, etmg_ma_pc, etot_dingo, ax[0], plot_label[0], args.sites, args.label_pad, -40, args.labsize)
        ass_barplot(assg_ma, asst_ma, assg_ma_pc, asst_ma_pc, gpptot_dingo, ax[1], plot_label[1], args.sites, args.label_pad, -5, args.labsize)

        evap_barplot(esoil_wet, etmt_wet, etmg_wet, esoil_wet_pc, etmt_wet_pc, etmg_wet_pc, ewet_dingo, ax[2], plot_label[2], args.sites, args.label_pad, -20, args.labsize)
        ass_barplot(assg_wet, asst_wet, assg_wet_pc, asst_wet_pc, gppwet_dingo, ax[3], plot_label[3], args.sites, args.label_pad, -3, args.labsize)

        evap_barplot(esoil_dry, etmt_dry, etmg_dry, esoil_dry_pc, etmt_dry_pc, etmg_dry_pc, edry_dingo, ax[4], plot_label[4], args.sites, args.label_pad, -10, args.labsize)
        ass_barplot(assg_dry, asst_dry, assg_dry_pc, asst_dry_pc, gppdry_dingo, ax[5], plot_label[5], args.sites, args.label_pad, -2, args.labsize)

        evap_barplot(esoil_wet2dry, etmt_wet2dry, etmg_wet2dry, esoil_wet2dry_pc, etmt_wet2dry_pc, etmg_wet2dry_pc, ewet2dry_dingo, ax[6], plot_label[6], args.sites, args.label_pad, -5, args.labsize)
        ass_barplot(assg_wet2dry, asst_wet2dry, assg_wet2dry_pc, asst_wet2dry_pc,  gppwet2dry_dingo, ax[7], plot_label[7], args.sites, args.label_pad, -1, args.labsize)






        
    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()






def fluxpartitions(inputfile, startyear, endyear, startwet, endwet, startdry, enddry):

    #load data
    data = np.genfromtxt(inputfile, names=True)

    #make numpy arrays in the right units
    esoil = 1000*np.array(data["esoil"]) #mm/d
    etmt = 1000*np.array(data["etmt"])   #mm/d
    etmg = 1000*np.array(data["etmg"])   #mm/d
    assg = np.array(data["assg"])        #mol/m2/d
    asst = np.array(data["asst"])        #mol/m2/d

    #create series of pandas time
    tmod = np.arange(datetime(int(data['fyear'][0]),int(data['fmonth'][0]),int(data['fday'][0])), 
                      datetime(int(data['fyear'][-1]),int(data['fmonth'][-1]),int(data['fday'][-1]))+timedelta(days=1), 
                      timedelta(days=1)).astype(datetime)
                    
    #make pandas series
    esoil_pd = pd.Series(esoil, index=tmod)
    etmt_pd = pd.Series(etmt, index=tmod)
    etmg_pd = pd.Series(etmg, index=tmod)
    assg_pd = pd.Series(assg, index=tmod)
    asst_pd = pd.Series(asst, index=tmod)
                    
    esoil_ma = np.mean(esoil_pd[ (esoil_pd.index.year>=startyear) & (esoil_pd.index.year<=endyear)].resample('A').sum() ) 
    etmt_ma = np.mean(etmt_pd[(etmt_pd.index.year>=startyear) & (etmt_pd.index.year<=endyear)].resample('A').sum() ) 
    etmg_ma = np.mean(etmg_pd[(etmg_pd.index.year>=startyear) & (etmg_pd.index.year<=endyear)].resample('A').sum() ) 
    assg_ma = np.mean(assg_pd[(assg_pd.index.year>=startyear) & (assg_pd.index.year<=endyear)].resample('A').sum() ) 
    asst_ma = np.mean(asst_pd[(asst_pd.index.year>=startyear) & (asst_pd.index.year<=endyear)].resample('A').sum() ) 

    esoil_mm = esoil_pd.resample('M').sum()
    etmt_mm = etmt_pd.resample('M').sum()
    etmg_mm = etmg_pd.resample('M').sum()
    assg_mm = assg_pd.resample('M').sum()
    asst_mm = asst_pd.resample('M').sum()

    esoil_dry = 0.0
    etmt_dry = 0.0
    etmg_dry = 0.0
    asst_dry = 0.0
    assg_dry = 0.0
    
    esoil_wet = 0.0
    etmt_wet = 0.0
    etmg_wet = 0.0
    asst_wet = 0.0
    assg_wet = 0.0
    
    esoil_wet2dry = 0.0
    etmt_wet2dry = 0.0
    etmg_wet2dry = 0.0
    asst_wet2dry = 0.0
    assg_wet2dry = 0.0
    
    esoil_dry2wet = 0.0
    etmt_dry2wet = 0.0
    etmg_dry2wet = 0.0
    asst_dry2wet = 0.0
    assg_dry2wet = 0.0
    
    for i in range(1,13):
        
        if startwet < endwet:        
            if( (i >= startwet) &  (i <= endwet)  ):
                esoil_wet = esoil_wet + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_wet = etmt_wet + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_wet = etmg_wet + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_wet = assg_wet + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_wet = asst_wet + np.mean( asst_mm[asst_mm.index.month == i] )
                
        if startdry < enddry:        
            if( (i >= startdry) &  (i <= enddry)  ):                
                esoil_dry = esoil_dry + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_dry = etmt_dry + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_dry = etmg_dry + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_dry = assg_dry + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_dry = asst_dry + np.mean( asst_mm[asst_mm.index.month == i] )                    


        if startwet > endwet:        
            if( (i >= startwet) |  (i <= endwet)  ):
                esoil_wet = esoil_wet + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_wet = etmt_wet + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_wet = etmg_wet + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_wet = assg_wet + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_wet = asst_wet + np.mean( asst_mm[asst_mm.index.month == i] )        

        if startdry > enddry:        
            if( (i >= startdry) |  (i <= enddry)  ):                
                esoil_dry = esoil_dry + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_dry = etmt_dry + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_dry = etmg_dry + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_dry = assg_dry + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_dry = asst_dry + np.mean( asst_mm[asst_mm.index.month == i] ) 
  
        #dry2wet-period
        if enddry < startwet:        
            if( (i > enddry) &  (i < startwet)  ):
                esoil_dry2wet = esoil_dry2wet + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_dry2wet = etmt_dry2wet + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_dry2wet = etmg_dry2wet + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_dry2wet = assg_dry2wet + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_dry2wet = asst_dry2wet + np.mean( asst_mm[asst_mm.index.month == i] )
                
        if startwet < enddry:        
            if( (i > enddry) |  (i < startwet)  ):
                esoil_dry2wet = esoil_dry2wet + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_dry2wet = etmt_dry2wet + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_dry2wet = etmg_dry2wet + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_dry2wet = assg_dry2wet + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_dry2wet = asst_dry2wet + np.mean( asst_mm[asst_mm.index.month == i] )
    
        #wet2dry-period
        if endwet < startdry:
            if( (i > endwet) &  (i < startdry)  ):
                esoil_wet2dry = esoil_wet2dry + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_wet2dry = etmt_wet2dry + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_wet2dry = etmg_wet2dry + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_wet2dry = assg_wet2dry + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_wet2dry = asst_wet2dry + np.mean( asst_mm[asst_mm.index.month == i] )          
            
        if startdry < endwet:
            if( (i > endwet) |  (i < startdry)  ):
                esoil_wet2dry = esoil_wet2dry + np.mean( esoil_mm[esoil_mm.index.month == i] )
                etmt_wet2dry = etmt_wet2dry + np.mean( etmt_mm[etmt_mm.index.month == i] )
                etmg_wet2dry = etmg_wet2dry + np.mean( etmg_mm[etmg_mm.index.month == i] )
                assg_wet2dry = assg_wet2dry + np.mean( assg_mm[asst_mm.index.month == i] )
                asst_wet2dry = asst_wet2dry + np.mean( asst_mm[asst_mm.index.month == i] )
    
    
    
    result = [esoil_ma, etmt_ma, etmg_ma, assg_ma, asst_ma]
    result_wet = [esoil_wet, etmt_wet, etmg_wet, assg_wet, asst_wet]
    result_dry = [esoil_dry, etmt_dry, etmg_dry, assg_dry, asst_dry]
    result_dry2wet = [esoil_dry2wet, etmt_dry2wet, etmg_dry2wet, assg_dry2wet, asst_dry2wet]
    result_wet2dry = [esoil_wet2dry, etmt_wet2dry, etmg_wet2dry, assg_wet2dry, asst_wet2dry]
   
    return result, result_wet, result_dry, result_dry2wet, result_wet2dry      
                

def mean_annual_dingo(inputfile, startyear, endyear, startwet, endwet, startdry, enddry):

    #load data
    
    data = np.loadtxt(inputfile, usecols=2) #mm/d
    
    #create series of pandas time
    tflux_tmp = np.genfromtxt(inputfile, usecols=0, dtype=np.str )#mm/d
    tflux = pd.date_range(tflux_tmp[0], tflux_tmp[-1], freq='D')
                    
    #make pandas series
    vals_pd = pd.Series(data, index=tflux)                    
    vals_ma = np.mean(vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)].resample('A').sum() ) 

    vals_mm = vals_pd[ (vals_pd.index.year>=startyear) & (vals_pd.index.year<=endyear)].resample('M').sum()
    vals_dry = 0.0
    vals_wet = 0.0
    vals_wet2dry = 0.0
    vals_dry2wet = 0.0

    for i in range(1,13):
        
        if startwet < endwet:        
            if( (i >= startwet) &  (i <= endwet)  ):
                vals_wet = vals_wet + np.mean( vals_mm[vals_mm.index.month == i] )
                
        if startdry < enddry:        
            if( (i >= startdry) &  (i <= enddry)  ):
                vals_dry = vals_dry + np.mean( vals_mm[vals_mm.index.month == i] )          
               
    
        if startwet > endwet:        
            if( (i >= startwet) |  (i <= endwet)  ):
                vals_wet = vals_wet + np.mean( vals_mm[vals_mm.index.month == i] )
                
        if startdry > enddry:    
            if( (i >= startdry) |  (i <= enddry)  ):
                vals_dry = vals_dry + np.mean( vals_mm[vals_mm.index.month == i] )
                
        #dry2wet-period
        if enddry < startwet:        
            if( (i > enddry) &  (i < startwet)  ):
                vals_dry2wet = vals_dry2wet + np.mean( vals_mm[vals_mm.index.month == i] )
                
        if startwet < enddry:        
            if( (i > enddry) |  (i < startwet)  ):
                vals_dry2wet = vals_dry2wet + np.mean( vals_mm[vals_mm.index.month == i] )
    
        #wet2dry-period
        if endwet < startdry:
            if( (i > endwet) &  (i < startdry)  ):
                vals_wet2dry = vals_wet2dry + np.mean( vals_mm[vals_mm.index.month == i] )        
            
        if startdry < endwet:
            if( (i > endwet) |  (i < startdry)  ):
                vals_wet2dry = vals_wet2dry + np.mean( vals_mm[vals_mm.index.month == i] )                
    
    result = [vals_ma, vals_wet, vals_dry, vals_dry2wet, vals_wet2dry]
    
    return result      
                

def evap_barplot(esoil, etmt, etmg, esoil_pc, etmt_pc, etmg_pc, evap_dingo, ax, title, labels, label_pad, dist_lab, lab_size):

    ind = np.arange(0,24, 4)
    ind2 = ind + 1
    ind3 = ind2 + 1

    p1 = ax.bar(ind, esoil, color="green")
    p2 = ax.bar(ind, etmt, bottom=esoil, color="orange")
    p3 = ax.bar(ind, etmg, bottom=np.add(etmt,esoil),color="blue")

    p4 = ax.bar(ind2, esoil_pc, color="green")
    p5 = ax.bar(ind2, etmt_pc, bottom=esoil_pc, color="orange")
    p6 = ax.bar(ind2, etmg_pc, bottom=np.add(etmt_pc,esoil_pc), color="blue")

    p7 = ax.bar(ind3, evap_dingo, color="grey")


    ax.set_ylabel(r'Evaporation [mm/year]', fontsize=18)
    ax.set_xticks(ind+0.5) 
    ax.tick_params(axis="x", pad = label_pad)
    ax.set_xticklabels( labels, rotation=90, fontsize=18)
    ax.legend((p1[0], p2[0], p3[0]), ('Esoil', 'Etmt', 'Etmg'))

    ax.text(-0.15, 1.05, title, transform=ax.transAxes, 
                size=18)

    for loc in ind:
        ax.text(loc, dist_lab, "Predicted", size=lab_size, rotation=90, horizontalalignment='center')
        
    for loc in ind2:
        ax.text(loc, dist_lab, "Prescribed", size=lab_size, rotation=90, horizontalalignment='center')

    for loc in ind3:
        ax.text(loc, dist_lab, "Observed", size=lab_size, rotation=90, horizontalalignment='center')


    return ax


def ass_barplot(assg, asst, assg_pc, asst_pc, gpp_dingo, ax, title, labels, label_pad,dist_lab, lab_size):

    ind = np.arange(0,24, 4)
    ind2 = ind + 1
    ind3 = ind2 + 1

    p1 = ax.bar(ind, assg, color="red")
    p2 = ax.bar(ind, asst, bottom=assg, color="purple")

    p4 = ax.bar(ind2, assg_pc, color="red")
    p5 = ax.bar(ind2, asst_pc, bottom=assg_pc, color="purple")

    p6 = ax.bar(ind3, gpp_dingo, color="grey")

    for loc in ind:
        ax.text(loc, dist_lab, "Predicted", size=lab_size, rotation=90, horizontalalignment='center')
        
    for loc in ind2:
        ax.text(loc, dist_lab, "Prescribed", size=lab_size, rotation=90, horizontalalignment='center')

    for loc in ind3:
        ax.text(loc, dist_lab, "Observed", size=lab_size, rotation=90, horizontalalignment='center')
         
        
    ax.set_ylabel(r'Assimilation [mol/m$^2$/year]', fontsize=18)
    ax.set_xticks(ind+0.5) 
    ax.tick_params(axis="x",pad = label_pad)
    ax.set_xticklabels( labels,rotation=90, fontsize=18 )
    ax.legend((p1[0], p2[0]), ('Assg', 'Asst'))

    ax.text(-0.15, 1.05, title, transform=ax.transAxes, size=18)


    return ax


main()



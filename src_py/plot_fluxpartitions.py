#!/usr/bin/env python
# coding: utf-8

#***********************************************************************
#        plot_fluxpartitions.py
#        Calculates and plots the flux partitions of the VOM.  
#       
#-----------------------------------------------------------------------
#        Authors: Remko Nijzink
#        Now at: LIST (Luxembourg Institute of Science and Technology)
#-----------------------------------------------------------------------
#
#  Copyright (C) 2020 LIST (Luxembourg Institute of Science and Technology), all right reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#***********************************************************************



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

    parser = argparse.ArgumentParser(description="Calculates and plots the flux partitions of the VOM.")

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
    parser.add_argument("--loc_title", help="figure title location", nargs='+', type=float, default = [-0.15, 1.05] )
    parser.add_argument("--labsize", help="label size", type=float, default = 8)
    parser.add_argument("--label_pad", help="label pad", type=float, default = 50)
    parser.add_argument("--only_meanannual",dest="only_meanannual", action='store_true', help="only plot mean annual values")
    parser.add_argument("--fig_lab", dest="fig_lab", action='store_true', help="plot labels of subplots")
    parser.add_argument("--no_fig_lab", dest="fig_lab", action='store_false', help="do not plot labels of subplots")

    parser.add_argument("--startwet", help="start wet season", type=float, default = 12 )
    parser.add_argument("--endwet", help="end wet season", type=float, default = 3)
    parser.add_argument("--startdry", help="start dry season", type=float, default = 5 )
    parser.add_argument("--enddry", help="end dry season", type=float, default = 9)

    parser.set_defaults(fig_lab=True, only_meanannual=False)

    args = parser.parse_args()



    etot_dingo = np.zeros( (len(args.evap_obs))  )
    ewet_dingo = np.zeros( (len(args.evap_obs))  )
    edry_dingo = np.zeros( (len(args.evap_obs))  )
    edry2wet_dingo = np.zeros( (len(args.evap_obs))  )
    ewet2dry_dingo = np.zeros( (len(args.evap_obs))  )

    #mean annual evaporation
    for i in range(0,len(args.evap_obs) ):
        tmp = mean_annual_dingo(args.evap_obs[i], args.pred_cover[i], args.startyear_obs[i], args.endyear_obs[i], args.startwet, args.endwet, args.startdry, args.enddry )
        etot_dingo[i] = tmp[0]
        ewet_dingo[i] = tmp[1]
        edry_dingo[i] = tmp[2]
        edry2wet_dingo[i] = tmp[3]
        ewet2dry_dingo[i] = tmp[4]

    gpptot_dingo = np.zeros( (len(args.ass_obs))  )
    gppwet_dingo = np.zeros( (len(args.ass_obs))  )
    gppdry_dingo = np.zeros( (len(args.ass_obs))  )
    gppwet2dry_dingo = np.zeros( (len(args.ass_obs))  )
    gppdry2wet_dingo = np.zeros( (len(args.ass_obs))  )

    #mean annual assimilation
    for i in range(0,len(args.ass_obs)):
        tmp = mean_annual_dingo(args.ass_obs[i], args.pred_cover[i], args.startyear_obs[i], args.endyear_obs[i], args.startwet, args.endwet, args.startdry, args.enddry )
        gpptot_dingo[i] = tmp[0]*-1.0
        gppwet_dingo[i] = tmp[1]*-1.0
        gppdry_dingo[i] = tmp[2]*-1.0
        gppdry2wet_dingo[i] = tmp[3]*-1.0
        gppwet2dry_dingo[i] = tmp[4]*-1.0

    #mean annual fluxes for predicted cover
    esoil_ma = np.zeros( (len(args.pred_cover))  )    
    etmt_ma = np.zeros( (len(args.pred_cover))  )
    etmg_ma = np.zeros( (len(args.pred_cover))  )
    assg_ma = np.zeros( (len(args.pred_cover))  )
    asst_ma = np.zeros( (len(args.pred_cover))  )

    esoil_wet = np.zeros( (len(args.pred_cover))  )
    etmt_wet = np.zeros( (len(args.pred_cover))  )
    etmg_wet = np.zeros( (len(args.pred_cover))  )
    assg_wet = np.zeros( (len(args.pred_cover))  )
    asst_wet = np.zeros( (len(args.pred_cover))  )

    esoil_dry = np.zeros( (len(args.pred_cover))  )
    etmt_dry = np.zeros( (len(args.pred_cover))  )
    etmg_dry = np.zeros( (len(args.pred_cover))  )
    assg_dry = np.zeros( (len(args.pred_cover))  )
    asst_dry = np.zeros( (len(args.pred_cover))  )

    esoil_wet2dry = np.zeros( (len(args.pred_cover))  )
    etmt_wet2dry = np.zeros( (len(args.pred_cover))  )
    etmg_wet2dry = np.zeros( (len(args.pred_cover))  )
    assg_wet2dry = np.zeros( (len(args.pred_cover))  )
    asst_wet2dry = np.zeros( (len(args.pred_cover))  )

    esoil_dry2wet = np.zeros( (len(args.pred_cover))  )
    etmt_dry2wet = np.zeros( (len(args.pred_cover))  )
    etmg_dry2wet = np.zeros( (len(args.pred_cover))  )
    assg_dry2wet = np.zeros( (len(args.pred_cover))  )
    asst_dry2wet = np.zeros( (len(args.pred_cover))  )

    for i in range(0,len(args.pred_cover)):
        tmp = fluxpartitions(args.pred_cover[i], args.evap_obs[i], args.startyear_mod[i], args.endyear_mod[i], args.startwet, args.endwet, args.startdry, args.enddry )

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

        esoil_dry2wet[i] = tmp[3][0]
        etmt_dry2wet[i] = tmp[3][1]
        etmg_dry2wet[i] = tmp[3][2]
        assg_dry2wet[i] = tmp[3][3]
        asst_dry2wet[i] = tmp[3][4]

    #mean annual fluxes for prescribed cover
    esoil_ma_pc = np.zeros( (len(args.pres_cover))  )
    etmt_ma_pc = np.zeros( (len(args.pres_cover))  )
    etmg_ma_pc = np.zeros( (len(args.pres_cover))  )
    assg_ma_pc = np.zeros( (len(args.pres_cover))  )
    asst_ma_pc = np.zeros( (len(args.pres_cover))  )

    esoil_wet_pc = np.zeros( (len(args.pres_cover))  )
    etmt_wet_pc = np.zeros( (len(args.pres_cover))  )
    etmg_wet_pc = np.zeros( (len(args.pres_cover))  )
    assg_wet_pc = np.zeros( (len(args.pres_cover))  )
    asst_wet_pc = np.zeros( (len(args.pres_cover))  )

    esoil_dry_pc = np.zeros( (len(args.pres_cover))  )
    etmt_dry_pc = np.zeros( (len(args.pres_cover))  )
    etmg_dry_pc = np.zeros( (len(args.pres_cover))  )
    assg_dry_pc = np.zeros( (len(args.pres_cover))  )
    asst_dry_pc = np.zeros( (len(args.pres_cover))  )

    esoil_wet2dry_pc = np.zeros( (len(args.pres_cover))  )
    etmt_wet2dry_pc = np.zeros( (len(args.pres_cover))  )
    etmg_wet2dry_pc = np.zeros( (len(args.pres_cover))  )
    assg_wet2dry_pc = np.zeros( (len(args.pres_cover))  )
    asst_wet2dry_pc = np.zeros( (len(args.pres_cover))  )

    esoil_dry2wet_pc = np.zeros( (len(args.pres_cover))  )
    etmt_dry2wet_pc = np.zeros( (len(args.pres_cover))  )
    etmg_dry2wet_pc = np.zeros( (len(args.pres_cover))  )
    assg_dry2wet_pc = np.zeros( (len(args.pres_cover))  )
    asst_dry2wet_pc = np.zeros( (len(args.pres_cover))  )

    for i in range(0,len(args.pres_cover)):
        tmp = fluxpartitions(args.pres_cover[i], args.evap_obs[i], args.startyear_mod[i], args.endyear_mod[i], args.startwet, args.endwet, args.startdry, args.enddry )

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

        esoil_dry2wet_pc[i] = tmp[3][0]
        etmt_dry2wet_pc[i] = tmp[3][1]
        etmg_dry2wet_pc[i] = tmp[3][2]
        assg_dry2wet_pc[i] = tmp[3][3]
        asst_dry2wet_pc[i] = tmp[3][4]


    ##################################################################
    #make plot
    if args.fig_lab is True:
        plot_label = [ "a)","b)","c)","d)","e)","f)", "g)", "h)", "i)", "j)" ]
    else: 
        plot_label = [ " "," "," "," "," "," ", " ", " ", " ", " " ]

    if( args.only_meanannual == True):
        fig, axes   = plt.subplots(nrows=1, ncols=2, figsize=(args.figsize[0], args.figsize[1]), sharex = True )
        ax = axes.flat

        evap_barplot(esoil_ma, etmt_ma, etmg_ma, esoil_ma_pc, etmt_ma_pc, etmg_ma_pc, etot_dingo, ax[0], plot_label[0], args.sites, args.label_pad, -40, args.labsize, "ET \n (mm year$^{-1}$)")
        ass_barplot(assg_ma, asst_ma, assg_ma_pc, asst_ma_pc, gpptot_dingo, ax[1], plot_label[1], args.sites, args.label_pad, -5,  args.labsize, "GPP \n (mol m$^{-2}$ year$^{-1}$)")

    else:
        fig, axes   = plt.subplots(nrows=5, ncols=2, figsize=(args.figsize[0], args.figsize[1]), sharex = True )
        ax = axes.flat

        evap_barplot(esoil_ma, etmt_ma, etmg_ma, esoil_ma_pc, etmt_ma_pc, etmg_ma_pc, etot_dingo, ax[0], plot_label[0], args.sites, args.label_pad, -40, args.labsize,"Mean annual ET \n (mm year$^{-1}$)", args.loc_title[0], args.loc_title[1] )
        ass_barplot(assg_ma, asst_ma, assg_ma_pc, asst_ma_pc, gpptot_dingo, ax[1], plot_label[1], args.sites, args.label_pad, -5, args.labsize, "Mean annual GPP \n (mol m$^{-2}$ year$^{-1}$)", args.loc_title[0], args.loc_title[1])

        evap_barplot(esoil_wet, etmt_wet, etmg_wet, esoil_wet_pc, etmt_wet_pc, etmg_wet_pc, ewet_dingo, ax[2], plot_label[2], args.sites, args.label_pad, -20, args.labsize, "Mean ET Dec.-March \n (mm year$^{-1}$)", args.loc_title[0], args.loc_title[1])
        ass_barplot(assg_wet, asst_wet, assg_wet_pc, asst_wet_pc, gppwet_dingo, ax[3], plot_label[3], args.sites, args.label_pad, -3, args.labsize, "Mean GPP Dec.-March \n (mol m$^{-2}$)", args.loc_title[0], args.loc_title[1])

        evap_barplot(esoil_dry, etmt_dry, etmg_dry, esoil_dry_pc, etmt_dry_pc, etmg_dry_pc, edry_dingo, ax[4], plot_label[4], args.sites, args.label_pad, -10, args.labsize, "Mean ET June-Sept. \n (mm year$^{-1}$)", args.loc_title[0], args.loc_title[1])
        ass_barplot(assg_dry, asst_dry, assg_dry_pc, asst_dry_pc, gppdry_dingo, ax[5], plot_label[5], args.sites, args.label_pad, -2, args.labsize, "Mean GPP June-Sept. \n (mol m$^{-2}$)", args.loc_title[0], args.loc_title[1])

        evap_barplot(esoil_wet2dry, etmt_wet2dry, etmg_wet2dry, esoil_wet2dry_pc, etmt_wet2dry_pc, etmg_wet2dry_pc, ewet2dry_dingo, ax[6], plot_label[6], args.sites, args.label_pad, -5, args.labsize, "Mean ET April-May \n (mm)", args.loc_title[0], args.loc_title[1])
        ass_barplot(assg_wet2dry, asst_wet2dry, assg_wet2dry_pc, asst_wet2dry_pc,  gppwet2dry_dingo, ax[7], plot_label[7], args.sites, args.label_pad, -1, args.labsize, "Mean GPP April-May \n (mol m$^{-2}$)", args.loc_title[0], args.loc_title[1])

        evap_barplot(esoil_dry2wet, etmt_dry2wet, etmg_dry2wet, esoil_dry2wet_pc, etmt_dry2wet_pc, etmg_dry2wet_pc, edry2wet_dingo, ax[8], plot_label[8], args.sites, args.label_pad, -5, args.labsize, "Mean ET Oct.-Nov. \n (mm)", args.loc_title[0], args.loc_title[1])
        ass_barplot(assg_dry2wet, asst_dry2wet, assg_dry2wet_pc, asst_dry2wet_pc,  gppdry2wet_dingo, ax[9], plot_label[9], args.sites, args.label_pad, -1, args.labsize, "Mean GPP Oct.-Nov. \n (mol m$^{-2}$)", args.loc_title[0], args.loc_title[1])





        
    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()






def fluxpartitions(inputfile, inputfile_obs, startyear, endyear, startwet, endwet, startdry, enddry):

    #load data
    data = np.genfromtxt(inputfile, names=True)

    #make numpy arrays in the right units
    esoil = 1000*np.array(data["esoil"]) #mm/d
    etmt = 1000*np.array(data["etmt"])   #mm/d
    etmg = 1000*np.array(data["etmg"])   #mm/d
    assg = np.array(data["assg"])        #mol/m2/d
    asst = np.array(data["asst"])        #mol/m2/d

    #create series of pandas time
    tmod = pd.date_range(datetime(int(data["fyear"][3]),int(data["fmonth"][0]),int(data["fday"][0])), 
                  datetime(int(data["fyear"][-1]),int(data["fmonth"][-1]),int(data["fday"][-1])), 
                  freq='D')

    #load data -observions    
    data_obs = np.loadtxt(inputfile_obs, usecols=2) #mm/d
    
    #create series of pandas time
    tflux_tmp = np.genfromtxt(inputfile_obs, usecols=0, dtype=np.str )#mm/d
    tflux = pd.date_range(tflux_tmp[0], tflux_tmp[-1], freq='D')

    dates_overlap = tmod.intersection(tflux)
   
    #make pandas series
    esoil_pd = pd.Series(esoil, index=tmod)
    etmt_pd = pd.Series(etmt, index=tmod)
    etmg_pd = pd.Series(etmg, index=tmod)
    assg_pd = pd.Series(assg, index=tmod)
    asst_pd = pd.Series(asst, index=tmod)
                    
    esoil_ma = np.mean(esoil_pd[ dates_overlap].resample('A').sum() ) 
    etmt_ma = np.mean(etmt_pd[dates_overlap].resample('A').sum() ) 
    etmg_ma = np.mean(etmg_pd[dates_overlap].resample('A').sum() ) 
    assg_ma = np.mean(assg_pd[dates_overlap].resample('A').sum() ) 
    asst_ma = np.mean(asst_pd[dates_overlap].resample('A').sum() ) 

    esoil_mm = esoil_pd[ dates_overlap].resample('M').sum()
    etmt_mm = etmt_pd[ dates_overlap].resample('M').sum()
    etmg_mm = etmg_pd[ dates_overlap].resample('M').sum()
    assg_mm = assg_pd[ dates_overlap].resample('M').sum()
    asst_mm = asst_pd[ dates_overlap].resample('M').sum()

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
                

def mean_annual_dingo(inputfile, inputfile_mod, startyear, endyear, startwet, endwet, startdry, enddry):

    #load data
    
    data = np.loadtxt(inputfile, usecols=2) #mm/d
    
    #create series of pandas time
    tflux_tmp = np.genfromtxt(inputfile, usecols=0, dtype=np.str )#mm/d
    tflux = pd.date_range(tflux_tmp[0], tflux_tmp[-1], freq='D')
             
    #load data
    data_mod = np.genfromtxt(inputfile_mod, names=True)

    #create series of pandas time
    tmod = pd.date_range(datetime(int(data_mod["fyear"][3]),int(data_mod["fmonth"][0]),int(data_mod["fday"][0])), 
                  datetime(int(data_mod["fyear"][-1]),int(data_mod["fmonth"][-1]),int(data_mod["fday"][-1])), 
                  freq='D')


    dates_overlap = tmod.intersection(tflux)

    #make pandas series
    vals_pd = pd.Series(data, index=tflux)                    
    vals_ma = np.mean(vals_pd[ dates_overlap].resample('A').sum() ) 

    vals_mm = vals_pd[ dates_overlap].resample('M').sum()
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
                

def evap_barplot(esoil, etmt, etmg, esoil_pc, etmt_pc, etmg_pc, evap_dingo, ax, title, labels, label_pad, dist_lab, lab_size,ylabel, titlex, titley):

    ind = np.arange(0,(len(esoil))*4, 4)
    ind2 = ind + 1
    ind3 = ind2 + 1

    p1 = ax.bar(ind, esoil, color="green")
    p2 = ax.bar(ind, etmt, bottom=esoil, color="orange")
    p3 = ax.bar(ind, etmg, bottom=np.add(etmt,esoil),color="blue")

    p4 = ax.bar(ind2, esoil_pc, color="green")
    p5 = ax.bar(ind2, etmt_pc, bottom=esoil_pc, color="orange")
    p6 = ax.bar(ind2, etmg_pc, bottom=np.add(etmt_pc,esoil_pc), color="blue")

    p7 = ax.bar(ind3, evap_dingo, color="grey")


    ax.set_ylabel(r'' + ylabel, fontsize=14)
    ax.set_xticks(ind+0.5) 
    ax.tick_params(axis="x", pad = label_pad)
    ax.set_xticklabels( labels, rotation=90, fontsize=18)
    ax.legend((p1[0], p2[0], p3[0]), ('Esoil', 'Etmt', 'Etmg'))

    ax.text(titlex, titley, title, transform=ax.transAxes, 
                size=18)

    for loc in ind:
        ax.text(loc, dist_lab, "Predicted", size=lab_size, rotation=90, horizontalalignment='center')
        
    for loc in ind2:
        ax.text(loc, dist_lab, "Prescribed", size=lab_size, rotation=90, horizontalalignment='center')

    for loc in ind3:
        ax.text(loc, dist_lab, "Observed", size=lab_size, rotation=90, horizontalalignment='center')


    return ax


def ass_barplot(assg, asst, assg_pc, asst_pc, gpp_dingo, ax, title, labels, label_pad,dist_lab, lab_size, ylabel, titlex, titley):

    ind = np.arange(0,(len(assg))*4, 4)
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
         
    ax.set_ylabel(r'' + ylabel, fontsize=14)        
    #ax.set_ylabel(r'Assimilation [mol/m$^2$/year]', fontsize=18)
    ax.set_xticks(ind+0.5) 
    ax.tick_params(axis="x",pad = label_pad)
    ax.set_xticklabels( labels,rotation=90, fontsize=18 )
    ax.legend((p1[0], p2[0]), ('Assg', 'Asst'))

    ax.text(titlex, titley, title, transform=ax.transAxes, size=18)


    return ax


main()



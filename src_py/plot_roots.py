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
    parser.add_argument("--in1", help="parameter-files",  nargs='+')
    parser.add_argument("--in2", help="parameter-files",  nargs='+')
    parser.add_argument("--in3", help="parameter-files",  nargs='+')
    parser.add_argument("--in4", help="parameter-files",  nargs='+')
    parser.add_argument("--in5", help="parameter-files",  nargs='+')
    parser.add_argument("--in6", help="parameter-files",  nargs='+')

    parser.add_argument("--fpar1", help="fpar-based projective cover")
    parser.add_argument("--fpar2", help="fpar-based projective cover")
    parser.add_argument("--fpar3", help="fpar-based projective cover")
    parser.add_argument("--fpar4", help="fpar-based projective cover")
    parser.add_argument("--fpar5", help="fpar-based projective cover")
    parser.add_argument("--fpar6", help="fpar-based projective cover")
    parser.add_argument("--fpar_dates", help="dates for fpar-based projective cover")
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,10] )
    parser.add_argument("--sites", help="study sites, should correspond to the number and order of inputfiles", nargs='+')
    parser.add_argument("--spa_rtdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--spa_rgdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--maespa_rtdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--maespa_rgdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--cable_rtdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--cable_rgdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--bios2_rtdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--bios2_rgdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--lpj_rtdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--lpj_rgdepth", help="value use for plotting rooting depths", type=float)
    parser.add_argument("--figlab", help="figure labels", nargs='+')

    args = parser.parse_args()

    #plot parameters
    site_names = args.sites

    symbols = ['s', '>', '.','8', 'P','*']
    colors = ['red', 'blue', 'green', 'gray', 'black', 'orange']

    if args.figlab is not None:
        fig_lab = args.figlab
    else:
        fig_lab = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)']

    n_rows = len(args.sites)+1


    files=dict()
    if args.in1 is not None:
        files[args.sites[0]] = args.in1
    if args.in2 is not None:
        files[args.sites[1]] = args.in2
    if args.in3 is not None:
        files[args.sites[2]] = args.in3
    if args.in4 is not None:
        files[args.sites[3]] = args.in4
    if args.in5 is not None:
        files[args.sites[4]] = args.in5
    if args.in6 is not None:
        files[args.sites[5]] = args.in6



    site_names = args.sites


    symbols = ['s', '>', '.','8', 'P','*']
    colors = ['red', 'blue', 'green', 'gray', 'black', 'orange']
    fig_lab = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)', 'n)']

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(args.figsize[0], args.figsize[1])) 

    ax = axes.flat



    icount = 0
    for isite in  range(0,len(args.sites)):  
        
        params_tmp = []


            #loop over files and load
        params_tmp = np.loadtxt( files[site_names[isite]][0]  )
            
       
        ax[0].scatter(isite, params_tmp[5], marker=symbols[isite], color=colors[isite], s=140,label = site_names[isite])     
        ax[1].scatter(isite, params_tmp[7], marker=symbols[isite], color=colors[isite], s=140) 
        icount = icount + 1 
        
    ax[0].plot( [-1,6], [args.spa_rtdepth,args.spa_rtdepth])# , label='SPA'  )
    ax[0].plot( [-1,6], [args.maespa_rtdepth, args.maespa_rtdepth] )#, label='MAESPA'  )
    ax[0].plot( [-1,6], [args.cable_rtdepth,args.cable_rtdepth])# , label='CABLE'  )
    ax[0].plot( [-1,6], [args.bios2_rtdepth,args.bios2_rtdepth] )#, label='BIOS2'  )
    ax[0].plot( [-1,6], [args.lpj_rtdepth,args.lpj_rtdepth] )# , label='LPJGUESS'  )   
        
    ax[0].set_xlim( -1, 5  ) 
    ax[0].set_ylim( 10, 0  ) 
    ax[0].legend(prop={'size':15})

    ax[0].set_xticks( [0,1,2,3,4,5] )  
    ax[0].set_xticklabels( "", rotation=90, size=24  )  
    ax[0].set_ylabel("Root depth trees (m)", size=20 )  
    ax[0].set_xlabel("Study sites", size=16 )  

    ax[0].text( x=-2.0, y=-0.1, s="a)", fontsize = 20)

    for tick in ax[0].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

        
    ax[1].plot( [-1,6], [args.spa_rgdepth,args.spa_rgdepth] , label='SPA'  )
    ax[1].plot( [-1,6], [args.maespa_rgdepth, args.maespa_rgdepth] , label='MAESPA'  )
    ax[1].plot( [-1,6], [args.cable_rgdepth,args.cable_rgdepth] , label='CABLE'  )
    ax[1].plot( [-1,6], [args.bios2_rgdepth,args.bios2_rgdepth] , label='BIOS2'  )
    ax[1].plot( [-1,6], [args.lpj_rgdepth,args.lpj_rgdepth] , label='LPJ-GUESS'  )
        
    #ax2.set_ylim([0,1]) 

    ax[1].set_xlim( -1, 5  ) 
    ax[1].set_ylim( 10, 0  ) 

    ax[1].set_xticks( [0,1,2,3,4] )  
    ax[1].set_xticklabels( "", rotation=90, size=14  )  
    ax[1].set_ylabel("Root depth grass (m)", size=20 ) 
    ax[1].set_xlabel("Study sites", size=16 )  

    ax[1].legend(prop={'size':15})
    ax[1].text( x=-2.0, y=-0.1, s="b)",  fontsize = 20)

    for tick in ax[1].yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()


main()



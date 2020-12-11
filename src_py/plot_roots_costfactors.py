#!/usr/bin/env python
# coding: utf-8

#***********************************************************************
#        plot_roots_costfactors.py
#        Script to rooting depths of the VOM agains multiple 
#        costfactors for water transport
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

    parser = argparse.ArgumentParser(description="Script to rooting depths of the VOM agains multiple costfactors for water transport")

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
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,24] )
    parser.add_argument("--sites", help="study sites, should correspond to the number and order of inputfiles", nargs='+')
    parser.add_argument("--cpccf_min", help="minimum value for the costfactor for water transport", type=float)
    parser.add_argument("--cpccf_max", help="maximum value for the costfactor for water transport", type=float)
    parser.add_argument("--cpccf_step", help="increment between costfactors", type=float)
    parser.add_argument("--plot_cpccf", help="value use for plotting rooting depths", type=float)
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
    cpcff_vals = np.arange(args.cpccf_min, args.cpccf_max + args.cpccf_step, args.cpccf_step)
    site_names = args.sites

    cpcff_str = map(str, np.round(cpcff_vals,1) ) 
    cpcff_str = list(cpcff_str)


    symbols = ['s', '>', '.','8', 'P','*']
    colors = ['red', 'blue', 'green', 'gray', 'black', 'orange']

    if args.figlab is not None:
        fig_lab = args.figlab
    else:
        fig_lab = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)']

    n_rows = len(args.sites)


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

    cpcff_str = map(str, np.round(cpcff_vals,1) ) 
    cpcff_str = list(cpcff_str) 

    symbols = ['s', '>', '.','8', 'P','*']
    colors = ['red', 'blue', 'green', 'gray', 'black', 'orange']
    fig_lab = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)', 'j)', 'k)', 'l)', 'm)', 'n)']



    fig, axes = plt.subplots(nrows=int(n_rows), ncols=2, figsize=(args.figsize[0], args.figsize[1])) 

    ax = axes.flat



    icount = 0




    ibasin = 0
    iplot = 0

    for site in args.sites:
        i_cpcff = 0


        for cpcff in  cpcff_str:  

            try:
                params = np.loadtxt( files[site][i_cpcff]    )

                rtdepth = params[5]
                rgdepth = params[7]

                    
                              
                if(i_cpcff ==0):
                    ax[iplot].scatter(cpcff_vals[i_cpcff], rtdepth, marker=symbols[ibasin], color=colors[ibasin] , s=140, label=site_names[ibasin])     
                    ax[iplot+1].scatter(cpcff_vals[i_cpcff], rgdepth, marker=symbols[ibasin], color=colors[ibasin] , s=140, label=site_names[ibasin])     

                    #ax[ibasin].plot(0.02, cai_fpar[ibasin], marker=symbols[ibasin], color=colors[ibasin] , markersize=8)     
                    #ax7.text(-0.10, 1.05, fig_lab[ibasin], transform=ax[ibasin].transAxes, size=18)
                else:
                    ax[iplot].scatter(cpcff_vals[i_cpcff], rtdepth, marker=symbols[ibasin], color=colors[ibasin] , s=140)     
                    ax[iplot+1].scatter(cpcff_vals[i_cpcff], rgdepth, marker=symbols[ibasin], color=colors[ibasin] , s=140)     
            except OSError:
                print('file not found')       

            i_cpcff = i_cpcff + 1

                        
        ax[iplot].set_ylabel("Root depths trees (m)", size=14 )
        ax[iplot+1].set_ylabel("Root depths grass (m)", size=14 )  
        ax[iplot].set_ylim( 0, 10  ) 
        ax[iplot].set_xlim( 0, 3.2  ) 
        ax[iplot].legend(prop={'size':10})
        ax[iplot].tick_params(axis='both', which='major', labelsize=14)
        ax[iplot].set_xticks(cpcff_vals)
        ax[iplot].set_xticklabels(cpcff_str)
        ax[iplot].grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)
        ax[iplot].text( x=-0.65, y=10, s=fig_lab[iplot], fontsize = 20)

        ax[iplot+1].set_ylim( 0, 2  ) 
        ax[iplot+1].set_xlim( 0, 3.2  )  
        ax[iplot+1].legend(prop={'size':10})    
        ax[iplot+1].tick_params(axis='both', which='major', labelsize=14)
        ax[iplot+1].set_xticks(cpcff_vals)
        ax[iplot+1].set_xticklabels(cpcff_str)
        ax[iplot+1].grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)
        ax[iplot+1].text( x=-0.6, y=2, s=fig_lab[iplot+1], fontsize = 20)

        
        iplot = iplot + 2 
        ibasin = ibasin + 1
                
    ax[iplot-1].set_xlabel(r'$c_{rv}$ ($\mu$$mol$ $m^{-3}$ $s^{-1}$)', size=14 )  
    ax[iplot-2].set_xlabel(r'$c_{rv}$ ($\mu$$mol$ $m^{-3}$ $s^{-1}$)', size=14 ) 
     

    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()


main()



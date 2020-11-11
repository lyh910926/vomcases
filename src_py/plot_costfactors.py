#!/usr/bin/env python
# coding: utf-8
#***********************************************************************
#        plot_costfactors.py
#        Plots the modelled and observed dry season projective cover for  
#        different values of the cost factor of water transport.
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

    parser = argparse.ArgumentParser(description="Plots the modelled and observed dry season projective cover for different values of the cost factor of water transport.")

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
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [18,18] )
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

    cai_fpar = np.zeros(len(args.sites))
    if args.fpar1 is not None:
        cai_fpar[0] = get_pc(args.fpar1, args.fpar_dates)
    if args.fpar2 is not None:
        cai_fpar[1] = get_pc(args.fpar2, args.fpar_dates)
    if args.fpar3 is not None:
        cai_fpar[2] = get_pc(args.fpar3, args.fpar_dates)
    if args.fpar4 is not None:
        cai_fpar[3] = get_pc(args.fpar4, args.fpar_dates)
    if args.fpar5 is not None:
        cai_fpar[4] = get_pc(args.fpar5, args.fpar_dates)
    if args.fpar6 is not None:
        cai_fpar[5] = get_pc(args.fpar6, args.fpar_dates)

    err = np.zeros((len(cpcff_vals),len(args.sites)))
    ED = np.zeros((len(cpcff_vals)))

    symbols = ['s', '>', '.','8', 'P','*']
    colors = ['red', 'blue', 'green', 'gray', 'black', 'orange']

    if args.figlab is not None:
        fig_lab = args.figlab
    else:
        fig_lab = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)']

    n_rows = np.ceil((len(args.sites)+1)/2)

    fig, axes = plt.subplots(nrows=int(n_rows), ncols=2, figsize=(args.figsize[0], args.figsize[1])) 
    if( np.abs( ( (len(args.sites)+1)/2) - n_rows ) > 0):
        fig.delaxes(axes[n_rows,1]) #remove last plot
    ax = axes.flat

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

    i_cpcff = 0
    for cpcff in  cpcff_str:  
        ibasin = 0

        for site in args.sites:
            try:

                params = np.loadtxt( files[site][i_cpcff]    )

                cai = params[4]
                
                err[i_cpcff, ibasin] = cai - cai_fpar[ibasin]
                          
                if(i_cpcff ==0):
                    ax[ibasin].scatter(cpcff_vals[i_cpcff], cai, marker=symbols[ibasin], color=colors[ibasin] , s=140, label=site_name[ibasin])     
                    #ax[ibasin].plot(0.02, cai_fpar[ibasin], marker=symbols[ibasin], color=colors[ibasin] , markersize=8)

                    ax[ibasin].hlines( cai_fpar[ibasin], 0, 3.2, color = colors[ibasin],label = "Observations" )
                    ax[ibasin].text(-0.10, 1.05, fig_lab[ibasin], transform=ax[ibasin].transAxes, size=18)
                else:
                    ax[ibasin].scatter(cpcff_vals[i_cpcff], cai, marker=symbols[ibasin], color=colors[ibasin] , s=140)     
                
                ax[ibasin].set_ylabel("Cover fraction (-)", size=16 )  
                ax[ibasin].set_ylim( 0, 1  ) 
                ax[ibasin].set_xlim( 0, 3.2  )    

                ax[ibasin].legend(prop={'size':10})

                ax[ibasin].tick_params(axis='both', which='major', labelsize=14)
                ax[ibasin].set_xticks(cpcff_vals)
                ax[ibasin].set_xticklabels(cpcff_str)
                ax[ibasin].grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)               
                    
            except OSError:
                print('file not found')
            ibasin = ibasin + 1 
        i_cpcff = i_cpcff + 1
    
    #combining the errors
    for i_cpcff in range(len(cpcff_str)):
        ED[i_cpcff] = np.sqrt(np.sum(err[i_cpcff,:]**2))

    ax[len(args.sites)].plot(cpcff_vals, ED, "*", markersize=10)
    ax[len(args.sites)].set_ylabel("Euclidian distance (-)", size = 16 )  
    ax[len(args.sites)].set_ylim( 0, 1.2  )
    ax[len(args.sites)].set_xlim( 0, 3.2  )    

    ax[len(args.sites)].legend(prop={'size':10})
    ax[len(args.sites)].text(-0.10, 1.05, fig_lab[ibasin], transform=ax[len(args.sites)].transAxes, 
                size=18)
    ax[len(args.sites)].tick_params(axis='both', which='major', labelsize=14)
    ax[len(args.sites)].set_xticks(cpcff_vals)
    ax[len(args.sites)].set_xticklabels(cpcff_str)
    ax[len(args.sites)].grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax[len(args.sites)].set_xlabel(r'c$_{rv}$ ($\mu$mol m$^3$ s$^{-1}$)', size=14 )  
    ax[len(args.sites)-1].set_xlabel(r'$c_{rv}$ ($\mu$mol m$^3$ s$^{-1}$)', size=14 )  

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

    #print("Constant cover:" + str(const_cov/0.95) )

    return const_cov/0.95



main()



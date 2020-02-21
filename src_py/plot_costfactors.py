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
    cai_fpar[0] = get_pc(args.fpar1, args.fpar_dates)
    cai_fpar[1] = get_pc(args.fpar2, args.fpar_dates)
    cai_fpar[2] = get_pc(args.fpar3, args.fpar_dates)
    cai_fpar[3] = get_pc(args.fpar4, args.fpar_dates)
    cai_fpar[4] = get_pc(args.fpar5, args.fpar_dates)
    cai_fpar[5] = get_pc(args.fpar6, args.fpar_dates)

    err = np.zeros((len(cpcff_vals),6))
    ED = np.zeros((len(cpcff_vals)))

    symbols = ['s', '>', '.','8', 'P','*']
    colors = ['red', 'blue', 'green', 'gray', 'black', 'orange']

    if args.figlab is not None:
        fig_lab = args.figlab
    else:
        fig_lab = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)']

    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(16, 13)) 
    fig.delaxes(axes[3,1])
    ax = axes.flat

    files=dict()
    files[args.sites[0]] = args.in1
    files[args.sites[1]] = args.in2
    files[args.sites[2]] = args.in3
    files[args.sites[3]] = args.in4
    files[args.sites[4]] = args.in5
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
                
                ax[ibasin].set_ylabel("Cover fraction [-]", size=16 )  
                ax[ibasin].set_ylim( 0, 1  ) 
                ax[ibasin].set_xlim( 0, 3.2  )    

                ax[ibasin].legend(prop={'size':10})

                if( ibasin == 5):
                    ax[ibasin].set_xlabel(r'$c_{cpccf}$ ($\mu$$mol$ $m^3$ $s^{-1}$)', size=14 )  

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

    ax[6].plot(cpcff_vals, ED, "*", markersize=10)
    ax[6].set_ylabel("Euclidian distance [-]", size = 16 )  
    #ax[1].set_ylim( 1, 9  )
    ax[6].set_xlim( 0, 3.2  )    

    ax[6].legend(prop={'size':10})
    ax[6].text(-0.10, 1.05, fig_lab[ibasin], transform=ax[6].transAxes, 
                size=18)
    ax[6].tick_params(axis='both', which='major', labelsize=14)
    ax[6].set_xticks(cpcff_vals)
    ax[6].set_xticklabels(cpcff_str)
    ax[6].grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)
    ax[6].set_xlabel(r'$c_{cpccf}$ ($\mu$$mol$ $m^3$ $s^{-1}$)', size=14 )  

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

    print("Constant cover:" + str(const_cov/0.95) )

    return const_cov



main()



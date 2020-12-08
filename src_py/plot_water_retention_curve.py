#!/usr/bin/env python
# coding: utf-8
#***********************************************************************
#        plot_water_retention.py
#        Script to plot water retention curves of the VOM 
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

import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from matplotlib.colors import LogNorm
import pandas as pd
from datetime import datetime, timedelta, date



def main():

    parser = argparse.ArgumentParser(description="Script to plot water retention curves of the VOM")


    parser.add_argument("--soildata", help="soildata used for the VOM")
    parser.add_argument("--outputfile", help="outputfile")
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

    args = parser.parse_args()

    ##########################################
    #years to plot



    #---------------------------------
    #load parameters
    if args.pars2015 is not None:
        params2015 = np.loadtxt(args.pars2015)

    #---------------------------------
    #load parameters
    if args.pars is not None:
        params = np.loadtxt(args.pars)


    #---------------------------------
    #load soildata
    nlayers = np.int(np.ceil(args.i_cz / args.i_delz))

    if args.soildata is not None:
        #values observations
        soildata = np.loadtxt(args.soildata) 
        theta_s = soildata[0,5]
        theta_r = soildata[0,6]
        delz = soildata[:,1]

    else:
        theta_s = args.i_thetas
        theta_r = args.i_thetar
        delz = np.repeat(args.i_delz, nlayers)

    #---------------------------------
    #soil moisture results




    if args.soildata is not None:
        theta_r = soildata[:,6]
        theta_s = soildata[:,5]
        alpha_vg = soildata[:,4]
        n_vg = soildata[:,3]
        m_vg = 1.0 -(1.0/n_vg)

    else:
        theta_r = args.i_thetar
        theta_s = args.i_thetas
        alpha_vg = args.i_avg
        n_vg = args.i_nvg
        m_vg = 1.0 -(1.0/n_vg)


    psi = np.logspace( 0, 10  )

    #loop over layers
    WRC = np.zeros([nlayers, len(psi)])

    for i_lay in range(0, nlayers): 

        WRC[i_lay,:] = theta_r[i_lay] + (theta_s[i_lay] - theta_r[i_lay])/  (  ( 1+ (alpha_vg[i_lay] * np.abs(psi))**n_vg[i_lay] )**(1-1/n_vg[i_lay]) )


    #---------------------------------
    # results 2015
    nlayers2015 = np.int(np.ceil(args.i_cz2015 / args.i_delz2015))

    delz2015 =  np.repeat(args.i_delz2015, nlayers)
    delz2015_sum = np.cumsum(delz2015)

    alpha_vg2015 = args.i_avg2015
    n_vg2015 = args.i_nvg2015
    m_vg2015 = 1.0 -(1.0/n_vg2015)


    #loop over layers
    WRC2015 = np.zeros([nlayers2015, len(psi)])

    for i_lay in range(0, nlayers2015): 

        WRC2015[i_lay,:] = args.i_thetar2015 + (args.i_thetas2015 - args.i_thetar2015)/  (  ( 1+ (alpha_vg2015 * np.abs(psi))**n_vg2015 )**(1-1/n_vg2015) )



    #######################################################################################
    #make plot
    #fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )

    if args.palette is not None:
        palette = plt.get_cmap(args.palette, nlayers)

    if args.colors is not None:
        colors = args.colors

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(args.figsize[0], args.figsize[1]) )        
    #ax = axes.flat
        
    for i_lay in range(0, nlayers): 
        if(i_lay == 0):
            ax.plot(WRC[i_lay], psi, color='red', label='VOM', zorder=2)
        else:
            ax.plot(WRC[i_lay], psi, color='red', zorder=2)


    #plot 2015 data
    if args.i_zr2015 is not None:
        for i_lay in range(0, nlayers2015): 
            if(i_lay == 0):
                ax.plot( WRC2015[i_lay], psi, "--" , dashes=(5, 5), lw=2, color='green', label='Schymanski et al. (2015)', zorder=2)
            else:
                ax.plot(WRC2015[i_lay], psi, "--", dashes=(5, 5), lw=2, color='green', zorder=2)



    ax.grid()

    #set labels
    ax.set_xlabel(r'$\Theta$ (-)', size=24  )
    ax.set_ylabel(r" $\psi$ (m)", size=24  )
    plt.yscale('symlog')

    #set axis and ticks


    #ax[0].set_xlim([datetime(yearstart,1, 1), datetime( yearend ,12, 31)]) 
    #for tick in ax[0].xaxis.get_major_ticks():
    #    tick.label.set_fontsize(20)
        #tick.label.set_rotation(90)
    #for tick in ax[0].yaxis.get_major_ticks():
#        tick.label.set_fontsize(20)

    ax.set_ylim( args.ylim )
    ax.set_xlim( [0,0.3] )

    ax.set_frame_on(True) # make it transparent
    
    if(args.legend == True):
        ax.legend(prop={'size':15}, framealpha=1  )


    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile, bbox_inches = "tight")
    else:
        plt.show()




main()



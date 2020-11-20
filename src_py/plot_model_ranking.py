#!/usr/bin/env python
# coding: utf-8

#***********************************************************************
#        plot_model_stats.py
#        Plots the statistics obtained with model_stats.py   
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

    parser = argparse.ArgumentParser(description="Plots the statistics obtained with model_stats.py")

    parser.add_argument("-o", "--outfile", help="outputfile with plot")

    parser.add_argument("--vom_evap_stats", help="vom statistics evaporation", nargs='+')
    parser.add_argument("--vom_gpp_stats", help="vom statistics evaporation", nargs='+')

    parser.add_argument("--vom_pc_evap_stats", help="vom statistics evaporation", nargs='+')
    parser.add_argument("--vom_pc_gpp_stats", help="vom statistics evaporation", nargs='+')

    parser.add_argument("--vom_pc2_evap_stats", help="vom statistics evaporation", nargs='+')
    parser.add_argument("--vom_pc2_gpp_stats", help="vom statistics evaporation", nargs='+')

    parser.add_argument("--vom_zr_evap_stats", help="vom statistics evaporation", nargs='+')
    parser.add_argument("--vom_zr_gpp_stats", help="vom statistics evaporation", nargs='+')

    parser.add_argument("--bess_evap_stats", help="bess statistics evaporation", nargs='+')
    parser.add_argument("--bios2_evap_stats", help="bios2 statistics evaporation", nargs='+')
    parser.add_argument("--lpjguess_evap_stats", help="lpj-guess statistics evaporation", nargs='+')
    parser.add_argument("--maespa_evap_stats", help="maespa statistics evaporation", nargs='+')
    parser.add_argument("--spa_evap_stats", help="spa statistics evaporation", nargs='+')
    parser.add_argument("--cable_evap_stats", help="cable statistics evaporation", nargs='+')
    parser.add_argument("--emp1_evap_stats", help="emp1 statistics evaporation", nargs='+')
    parser.add_argument("--emp2_evap_stats", help="emp2 statistics evaporation", nargs='+')

    parser.add_argument("--bess_gpp_stats", help="bess statistics assimilation", nargs='+')
    parser.add_argument("--bios2_gpp_stats", help="bios2 statistics assimilation", nargs='+')
    parser.add_argument("--lpjguess_gpp_stats", help="lpj-guess statistics assimilation", nargs='+')
    parser.add_argument("--maespa_gpp_stats", help="maespa statistics assimilation", nargs='+')
    parser.add_argument("--spa_gpp_stats", help="spa statistics assimilation", nargs='+')
    parser.add_argument("--cable_gpp_stats", help="cable statistics assimilation", nargs='+')
    parser.add_argument("--emp1_gpp_stats", help="emp1 statistics evaporation", nargs='+')
    parser.add_argument("--emp2_gpp_stats", help="emp2 statistics evaporation", nargs='+')

    parser.add_argument("--sites", help="study sites, should correspond to the number and order of inputfiles", nargs='+')
    parser.add_argument("--whitley_sites", help="mask the study sites that are also used in Whitley et al.",nargs='+', type=int )
    parser.add_argument("--dingo_et", help="DINGO files evaporation", nargs='+')
    parser.add_argument("--dingo_gpp", help="DINGO files assimilation", nargs='+')
    parser.add_argument("--i2015", help="results_daily AoB2015 ")
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [18,18] )
    parser.add_argument("--fig_lab", dest="fig_lab", action='store_true', help="plot labels of subplots")
    parser.add_argument("--no_fig_lab", dest="fig_lab", action='store_false', help="do not plot labels of subplots")
    parser.add_argument("--sharex", help="share x-axis", dest="sharex", action='store_true' )
    parser.add_argument("--no_sharex", help="share x-axis", dest="sharex", action='store_false')
    parser.set_defaults(fig_lab=True, sharex = True, whitley_sites=[1, 1, 1, 1, 1])

    args = parser.parse_args()

    ###################################
    #some constants for conversions
    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 997             #[kg/m3]

    ###################################
    #read in data from Whitley et al. 
    whitley_sites = np.array(args.sites)[np.array(args.whitley_sites)==1]

    bess_evap_stats = dict()
    bess_ass_stats = dict()

    bios2_evap_stats = dict()
    bios2_ass_stats = dict()

    lpjguess_evap_stats = dict()
    lpjguess_ass_stats = dict()

    maespa_evap_stats = dict()
    maespa_ass_stats = dict()

    spa_evap_stats = dict()
    spa_ass_stats = dict()

    cable_evap_stats = dict()
    cable_ass_stats = dict()

    emp1_evap_stats = dict()
    emp1_ass_stats = dict()

    emp2_evap_stats = dict()
    emp2_ass_stats = dict()

    for i in range(0, len(whitley_sites)):
        #read in data from BESS
        bess_evap_stats[whitley_sites[i]] = np.genfromtxt( args.bess_evap_stats[i] , skip_header = 1 )
        bess_ass_stats[whitley_sites[i]] = np.genfromtxt( args.bess_gpp_stats[i] , skip_header = 1 )

        #read in data from BIOS2
        bios2_evap_stats[whitley_sites[i]] = np.genfromtxt( args.bios2_evap_stats[i]  , skip_header = 1)
        bios2_ass_stats[whitley_sites[i]] = np.genfromtxt( args.bios2_gpp_stats[i]  , skip_header = 1)

        #read in data from LPJ-GUESS, ET in W/m2, GPP in umol/m2/s
        lpjguess_evap_stats[whitley_sites[i]] = np.genfromtxt( args.lpjguess_evap_stats[i], skip_header = 1  )
        lpjguess_ass_stats[whitley_sites[i]] = np.genfromtxt( args.lpjguess_gpp_stats[i], skip_header = 1  )

        #read in data from MAESPA, ET in W m-2, GPP in umol m-2 s-1
        maespa_evap_stats[whitley_sites[i]] = np.genfromtxt( args.maespa_evap_stats[i], skip_header = 1  )
        maespa_ass_stats[whitley_sites[i]] = np.genfromtxt( args.maespa_gpp_stats[i], skip_header = 1  )

 
        #read in data from SPA, ET in W m-2, GPP in mmol m-2 s-1
        spa_evap_stats[whitley_sites[i]] = np.genfromtxt( args.spa_evap_stats[i], skip_header = 1  )
        spa_ass_stats[whitley_sites[i]] = np.genfromtxt( args.spa_gpp_stats[i], skip_header = 1  )
 
        #read in data from CABLE, ET in kg/m^2/s, GPP in umol/m^2/s
        cable_evap_stats[whitley_sites[i]] = np.genfromtxt( args.cable_evap_stats[i], skip_header = 1  )
        cable_ass_stats[whitley_sites[i]] = np.genfromtxt( args.cable_gpp_stats[i], skip_header = 1  )

        #read in data from emp1, ET in kg/m^2/s, GPP in umol/m^2/s
        emp1_evap_stats[whitley_sites[i]] = np.genfromtxt( args.emp1_evap_stats[i], skip_header = 1  )
        emp1_ass_stats[whitley_sites[i]] = np.genfromtxt( args.emp1_gpp_stats[i], skip_header = 1  )

        #read in data from emp2, ET in kg/m^2/s, GPP in umol/m^2/s
        emp2_evap_stats[whitley_sites[i]] = np.genfromtxt( args.emp2_evap_stats[i], skip_header = 1  )
        emp2_ass_stats[whitley_sites[i]] = np.genfromtxt( args.emp2_gpp_stats[i], skip_header = 1  )
 
    ####################################################
    #load other data 

    dingo_evap = dict()
    dingo_gpp = dict()
    vom_evap = dict()
    vom_pc_evap = dict()
    vom_pc2_evap = dict()
    vom_zr_evap = dict()
    vom_evap_stats = dict()
    vom_pc_evap_stats = dict()
    vom_pc2_evap_stats = dict()
    vom_zr_evap_stats = dict()
    vom_gpp = dict()
    vom_pc_gpp = dict()
    vom_pc2_gpp = dict()
    vom_zr_gpp = dict()
    vom_gpp_stats = dict()
    vom_pc_gpp_stats = dict()
    vom_pc2_gpp_stats = dict()
    vom_zr_gpp_stats = dict()

    for i in range(0, len(args.sites)):

        vom_evap_stats[args.sites[i]] = np.genfromtxt( args.vom_evap_stats[i], skip_header = 1  )
        vom_gpp_stats[args.sites[i]] = np.genfromtxt( args.vom_gpp_stats[i], skip_header = 1  )

        if(args.vom_pc_evap_stats is not None):
            vom_pc_evap_stats[args.sites[i]] = np.genfromtxt( args.vom_pc_evap_stats[i], skip_header = 1  )
            vom_pc_gpp_stats[args.sites[i]] = np.genfromtxt( args.vom_pc_gpp_stats[i], skip_header = 1  )

        if(args.vom_pc2_evap_stats is not None):
            vom_pc2_evap_stats[args.sites[i]] = np.genfromtxt( args.vom_pc2_evap_stats[i], skip_header = 1  )
            vom_pc2_gpp_stats[args.sites[i]] = np.genfromtxt( args.vom_pc2_gpp_stats[i], skip_header = 1  )

        if(args.vom_zr_evap_stats is not None):
            vom_zr_evap_stats[args.sites[i]] = np.genfromtxt( args.vom_zr_evap_stats[i], skip_header = 1  )
            vom_zr_gpp_stats[args.sites[i]] = np.genfromtxt( args.vom_zr_gpp_stats[i], skip_header = 1  )

 
    ####################################################
    #start plotting

    #parameters for plotting
    if args.fig_lab is True:
        plot_label = [ "(a)","(b)","(c)","(d)","(e)","(f)", "(g)", "(h)" ]
    else: 
        plot_label = [ " "," "," "," "," "," ", " ", " " ]

    loc = np.arange(5,len(args.sites)*10+5,10) 
    loc_vom =  np.arange(0.5, len(args.sites)*10+0.5, 10)  
    loc_vom2 =  np.arange(1.5, len(args.sites)*10+1.5, 10)  
    loc_vom3 =  np.arange(2.5, len(args.sites)*10+2.5, 10)  
    loc_vom4 =  np.arange(3.5, len(args.sites)*10+3.5, 10)  

    loc_bess = np.arange(4.5, len(args.sites)*10+4.5, 10)
    loc_bios2 = np.arange(5.5, len(args.sites)*10+5.5, 10)
    loc_cable = np.arange(6.5, len(args.sites)*10+6.5, 10)
    loc_lpjguess = np.arange(7.5, len(args.sites)*10+7.5, 10)
    loc_maespa = np.arange(8.5, len(args.sites)*10+8.5, 10)
    loc_spa = np.arange(9.5, len(args.sites)*10+9.5, 10)


    ylabels = [ r"ET (mm year$^{-1}$)",
                r'GPP (mol m$^{-2}$ year$^{-1}$)',
                "Rel.Err. ET (-)",  
                "Rel.Err. GPP (-)", 
                "Rel.Err. amplitude ET (-)", 
                "Rel.Err. amplitude GPP (-)", 
                "Err. Min. Annual (-)", 
                "Err. Min. Annual (-)", 
                "Mean Wet Season Rel. Err. (-)", 
                "Mean Wet Season Rel. Err. (-)", 
              ]


    maxy= [1500, 200, 1,1, 1.0, 1.0, 1.0 , 2.0, 1.5,1.5]
    miny= [0, 0 , -1,-1, -1.0,-1.0, -1.5,-2.5, -1.5,-1.5]

    stats_order = [ 6,10,11,12]
    methods = ["best_null", "best_max", "best_max", "best_null"]

    iplot = 0

    #determine average ranks
    vom_erank = dict()
    vom_assrank = dict()

    bess_erank = dict()
    bess_assrank = dict()

    bios2_erank = dict()
    bios2_assrank = dict()

    cable_erank = dict()
    cable_assrank = dict()

    lpj_erank = dict()
    lpj_assrank = dict()

    maespa_erank = dict()
    maespa_assrank = dict()

    spa_erank = dict()
    spa_assrank = dict()

    emp1_erank = dict()
    emp1_assrank = dict()

    emp2_erank = dict()
    emp2_assrank = dict()

    #loop over sites and rank
    for isite in range(0, len(args.sites)): 

        #VOM
        vom_erank_arr = get_rank( vom_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        vom_erank[args.sites[isite]] = np.mean(vom_erank_arr, axis=0 )

        vom_assrank_arr = get_rank( vom_gpp_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        vom_assrank[args.sites[isite]] = np.mean(vom_assrank_arr, axis=0 )

        #bess
        bess_erank_arr = get_rank( bess_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        bess_erank[args.sites[isite]] = np.mean(bess_erank_arr, axis=0 )

        bess_assrank_arr = get_rank( bess_ass_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        bess_assrank[args.sites[isite]] = np.mean(bess_assrank_arr, axis=0 )

        #bios2
        bios2_erank_arr = get_rank( bios2_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        bios2_erank[args.sites[isite]] = np.mean(bios2_erank_arr, axis=0 )

        bios2_assrank_arr = get_rank( bios2_ass_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        bios2_assrank[args.sites[isite]] = np.mean(bios2_assrank_arr, axis=0 )

        #cable
        cable_erank_arr = get_rank( cable_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        cable_erank[args.sites[isite]] = np.mean(cable_erank_arr, axis=0 )

        cable_assrank_arr = get_rank( cable_ass_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        cable_assrank[args.sites[isite]] = np.mean(cable_assrank_arr, axis=0 )

        #lpj-guess
        lpj_erank_arr = get_rank( lpjguess_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        lpj_erank[args.sites[isite]] = np.mean(lpj_erank_arr, axis=0 )

        lpj_assrank_arr = get_rank( lpjguess_ass_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        lpj_assrank[args.sites[isite]] = np.mean(lpj_assrank_arr, axis=0 )

        #maespa
        maespa_erank_arr = get_rank( maespa_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        maespa_erank[args.sites[isite]] = np.mean(maespa_erank_arr, axis=0 )

        maespa_assrank_arr = get_rank( maespa_ass_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        maespa_assrank[args.sites[isite]] = np.mean(maespa_assrank_arr, axis=0 )


        #spa
        spa_erank_arr = get_rank( spa_evap_stats[args.sites[isite]], 
                                  emp1_evap_stats[args.sites[isite]],
                                  emp2_evap_stats[args.sites[isite]], stats_order, methods )
        spa_erank[args.sites[isite]] = np.mean(spa_erank_arr, axis=0 )

        spa_assrank_arr = get_rank( spa_ass_stats[args.sites[isite]], 
                                  emp1_ass_stats[args.sites[isite]],
                                  emp2_ass_stats[args.sites[isite]], stats_order, methods )
        spa_assrank[args.sites[isite]] = np.mean(spa_assrank_arr, axis=0 )


  
    #start plotting
    fig, ax   = plt.subplots(nrows=2, ncols=7, figsize=(args.figsize[0], args.figsize[1]), sharex=args.sharex, sharey=True) 

    ax[0,0].text(0.2, 1.02, "VOM", transform=ax[0,0].transAxes,  size=20)
    plot_vals = [vals[0] for vals in vom_erank.values()]
    ax[0,0].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="VOM")
    plot_vals2 = [vals[1] for vals in vom_erank.values()]
    ax[0,0].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in vom_erank.values()]
    ax[0,0].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,0].grid(color='gray', linestyle='dashed')
    ax[0,0].set_ylabel( "Avg. rank ET", fontsize=20   )

    plot_vals = [vals[0] for vals in vom_assrank.values()]
    ax[1,0].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="VOM")
    plot_vals2 = [vals[1] for vals in vom_assrank.values()]
    ax[1,0].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in vom_assrank.values()]
    ax[1,0].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,0].grid(color='gray', linestyle='dashed')
    ax[1,0].set_xticks( range(0,5)  )
    ax[1,0].set_xticklabels( args.sites, rotation=90, fontsize=20  ) 
    ax[1,0].set_ylabel( "Avg. rank GPP", fontsize=20   )

    #bess
    ax[0,1].text(0.2, 1.02, "BESS", transform=ax[0,1].transAxes,  size=20)
    plot_vals = [vals[0] for vals in bess_erank.values()]
    ax[0,1].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="BESS")
    plot_vals2 = [vals[1] for vals in bess_erank.values()]
    ax[0,1].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in bess_erank.values()]
    ax[0,1].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,1].grid(color='gray', linestyle='dashed')

    plot_vals = [vals[0] for vals in bess_assrank.values()]
    ax[1,1].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="BESS")
    plot_vals2 = [vals[1] for vals in bess_assrank.values()]
    ax[1,1].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in bess_assrank.values()]
    ax[1,1].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,1].grid(color='gray', linestyle='dashed')
    ax[1,1].set_xticks( range(0,5)  )
    ax[1,1].set_xticklabels( args.sites, rotation=90, fontsize=20  ) 


    #bios2
    ax[0,2].text(0.2, 1.02, "BIOS2", transform=ax[0,2].transAxes,  size=20)
    plot_vals = [vals[0] for vals in bios2_erank.values()]
    ax[0,2].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="BIOS2")
    plot_vals2 = [vals[1] for vals in bios2_erank.values()]
    ax[0,2].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in bios2_erank.values()]
    ax[0,2].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,2].grid(color='gray', linestyle='dashed')

    plot_vals = [vals[0] for vals in bios2_assrank.values()]
    ax[1,2].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="BIOS2")
    plot_vals2 = [vals[1] for vals in bios2_assrank.values()]
    ax[1,2].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in bios2_assrank.values()]
    ax[1,2].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,2].grid(color='gray', linestyle='dashed')
    ax[1,2].set_xticks( range(0,5)  )
    ax[1,2].set_xticklabels( args.sites, rotation=90, fontsize=20  ) 

    #cable
    ax[0,3].text(0.2, 1.02, "CABLE", transform=ax[0,3].transAxes,  size=20)
    plot_vals = [vals[0] for vals in cable_erank.values()]
    ax[0,3].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="CABLE")
    plot_vals2 = [vals[1] for vals in cable_erank.values()]
    ax[0,3].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in cable_erank.values()]
    ax[0,3].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,3].grid(color='gray', linestyle='dashed')

    plot_vals = [vals[0] for vals in cable_assrank.values()]
    ax[1,3].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="CABLE")
    plot_vals2 = [vals[1] for vals in cable_assrank.values()]
    ax[1,3].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in cable_assrank.values()]
    ax[1,3].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,3].grid(color='gray', linestyle='dashed')
    ax[1,3].set_xticks( range(0,5)  )
    ax[1,3].set_xticklabels( args.sites, rotation=90, fontsize=20  ) 

    #lpjguess
    ax[0,4].text(0.2, 1.02, "LPJ-GUESS", transform=ax[0,4].transAxes,  size=20)
    plot_vals = [vals[0] for vals in lpj_erank.values()]
    ax[0,4].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="LPJ-GUESS")
    plot_vals2 = [vals[1] for vals in lpj_erank.values()]
    ax[0,4].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in lpj_erank.values()]
    ax[0,4].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,4].grid(color='gray', linestyle='dashed')

    plot_vals = [vals[0] for vals in lpj_assrank.values()]
    ax[1,4].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="LPJ-GUESS")
    plot_vals2 = [vals[1] for vals in lpj_assrank.values()]
    ax[1,4].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in lpj_assrank.values()]
    ax[1,4].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,4].grid(color='gray', linestyle='dashed')
    ax[1,4].set_xticks( range(0,5)  )
    ax[1,4].set_xticklabels( args.sites, rotation=90, fontsize=20  )

    #MAESPA
    ax[0,5].text(0.2, 1.02, "MAESPA", transform=ax[0,5].transAxes,  size=20)
    plot_vals = [vals[0] for vals in maespa_erank.values()]
    ax[0,5].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="MAESPA")
    plot_vals2 = [vals[1] for vals in maespa_erank.values()]
    ax[0,5].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in maespa_erank.values()]
    ax[0,5].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,5].grid(color='gray', linestyle='dashed')

    plot_vals = [vals[0] for vals in maespa_assrank.values()]
    ax[1,5].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="MAESPA")
    plot_vals2 = [vals[1] for vals in maespa_assrank.values()]
    ax[1,5].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in maespa_assrank.values()]
    ax[1,5].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,5].grid(color='gray', linestyle='dashed')
    ax[1,5].set_xticks( range(0,5)  )
    ax[1,5].set_xticklabels( args.sites, rotation=90, fontsize=20  )

    #SPA
    ax[0,6].text(0.2, 1.02, "SPA", transform=ax[0,6].transAxes,  size=20)
    plot_vals = [vals[0] for vals in spa_erank.values()]
    ax[0,6].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="SPA")
    plot_vals2 = [vals[1] for vals in spa_erank.values()]
    ax[0,6].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in spa_erank.values()]
    ax[0,6].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[0,6].grid(color='gray', linestyle='dashed')

    plot_vals = [vals[0] for vals in spa_assrank.values()]
    ax[1,6].plot(range(0,5), plot_vals,  "-*", color="red" , zorder=1, label="MAESPA")
    plot_vals2 = [vals[1] for vals in spa_assrank.values()]
    ax[1,6].plot(range(0,5), plot_vals2,  "-*", color="gray" , zorder=1, label="emp1")
    plot_vals3 = [vals[2] for vals in spa_assrank.values()]
    ax[1,6].plot(range(0,5), plot_vals3,  "-*", color="darkgray" , zorder=1, label="emp2")
    ax[1,6].grid(color='gray', linestyle='dashed')
    ax[1,6].set_xticks( range(0,5)  )
    ax[1,6].set_xticklabels( args.sites, rotation=90, fontsize=20  )





    #ax[0].set_xlim([0,len(args.sites)*10])
    #ax[0].set_ylim([ miny[0], maxy[0]])
    #ax[0].set_xticks( np.arange(5,65,10)  )
    #ax[0].set_xticklabels( args.sites, rotation=90, fontsize=20  ) 
    #ax[0].set_ylabel( ylabels[0], fontsize=20   )
    #ax[0].text(-0.2, 1.02, plot_label[0], transform=ax[0].transAxes,  size=20)
    #for tick in ax[0].yaxis.get_major_ticks():
    #    tick.label.set_fontsize(16)

    #ax[1].set_xlim([0,len(args.sites)*10])
    #ax[1].set_ylim([ miny[1], maxy[1]])
    #ax[1].set_xticks( np.arange(5,65,10)  )
    #ax[1].set_xticklabels( args.sites, rotation=90, fontsize=20  ) 
    #ax[1].set_ylabel( ylabels[1], fontsize=20   )    
    #ax[1].text(-0.2, 1.02, plot_label[1], transform=ax[1].transAxes,  size=20)
    #for tick in ax[1].yaxis.get_major_ticks():
#        tick.label.set_fontsize(16)

    #plot statistics
    #iplot = 2

 
    plt.tight_layout()

    if args.outfile is not None:
        plt.savefig(args.outfile, bbox_inches = "tight")
    else:
        plt.show()


def get_rank(stats1, stats2, stats3, ind_stats, method):

    rank_arr = np.zeros([len(ind_stats), 3  ])
    for istat in range(0, len(ind_stats)):
        vals = np.array([stats1[ind_stats[istat]], stats2[ind_stats[istat]], stats3[ind_stats[istat]] ])



        if( method[istat] == "best_max"):
            #in case the highest number is best
            order = (-vals).argsort()        

        if( method[istat] == "best_null"):
            #in case the highest number is best
            order = (np.abs(vals)).argsort()   
        

        rank_arr[istat,:] = order.argsort()+1

    return rank_arr





def read_bess(infile, startyear):

    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 1000             #[kg/m3]

    data = np.loadtxt(infile, delimiter=",") 
    time = pd.date_range("01-01-" + startyear, periods = len(data[:,0]), freq='D')

    tmp = 24*60*60*data[:,0] /( lat_heat_vapor * rho_w * 1000 )

    #make pandas series and return daily values
    evap_pd = pd.Series(tmp, index = time ) #mm/day
    ass_pd = pd.Series(data[:,1]*24*60*60*10**-6, index = time ) #mol/m2/d

    return evap_pd, ass_pd

def read_bios2(infile):

    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 1000             #[kg/m3]

    data = np.loadtxt(infile, delimiter=",") 
    time = pd.date_range(datetime(int(data[0,0]),int(data[0,1]),int(data[0,2])), 
              datetime(int(data[-1,0]),int(data[-1,1]),int(data[-1,2])),freq='D')

    tmp = 24*60*60*data[:,3] /( lat_heat_vapor * rho_w * 1000 )

    #make pandas series and return daily values
    ass_pd = pd.Series(data[:,4]*24*60*60*10**-6, index = time ) #mol/m2/d
    evap_pd = pd.Series(tmp, index = time ) 

    return evap_pd, ass_pd

def read_lpjguess(infile_et, infile_gpp):

    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 1000             #[kg/m3]

    data_et = np.loadtxt(infile_et, skiprows=1, usecols=3)
    data_gpp = np.loadtxt(infile_gpp, skiprows=1, usecols=3)
    time_tmp = np.loadtxt(infile_gpp, skiprows=1)
    time = pd.date_range(datetime(int(time_tmp[0,0]),int(time_tmp[0,1]),int(time_tmp[0,2])), 
              datetime(int(time_tmp[-1,0]),int(time_tmp[-1,1]),int(time_tmp[-1,2])),freq='D')

    tmp = 24*60*60*data_et /( lat_heat_vapor * rho_w * 1000 )

    #make pandas series and return daily values
    evap_pd = pd.Series(tmp, index = time ) #mm/day
    ass_pd = pd.Series(data_gpp*24*60*60*10**-6, index = time ) 

    return evap_pd, ass_pd

def read_maespa(infile):

    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 1000             #[kg/m3]

    data = np.loadtxt(infile, delimiter=",", skiprows=3, usecols=(3,6))
    data[data == -9999.9] = np.nan
    data[data == -999] = np.nan
    time_tmp = np.loadtxt(infile, delimiter=",", dtype=np.str, skiprows=3, usecols=0)
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    tmp = 30*60*data[:,1] /( lat_heat_vapor * rho_w * 1000 )

    evap_pd = pd.Series(tmp, index = time ) #mm/30min
    ass_pd = pd.Series(data[:,0]*30*60*10**-6, index = time ) 

    return evap_pd, ass_pd

def read_spa(infile):

    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 1000             #[kg/m3]

    data = np.loadtxt(infile, delimiter=",", skiprows=1, usecols=(1,3))
    time_tmp = np.loadtxt(infile, delimiter=",", dtype=np.str, skiprows=1, usecols=0)
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    tmp = 30*60*data[:,1] /( lat_heat_vapor * rho_w * 1000 )

    evap_pd = pd.Series(tmp, index = time ) #mm/30min
    ass_pd = pd.Series(-1.0*data[:,0]*30*60*10**-6, index = time ) #mol/m2/s

    return evap_pd, ass_pd

def read_cable(infile):

    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 1000             #[kg/m3]

    ncfile = Dataset(infile)
    data_gpp = np.squeeze(ncfile.variables["GPP"]) # extract variable
    data_et = np.squeeze(ncfile.variables["Evap"]) # extract variable
    time_tmp = np.squeeze(ncfile.variables["time"]) # extract variable
    time_tmp = [pd.to_datetime("2007-01-01 00:01:00") + pd.Timedelta(seconds=i) for i in time_tmp]
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    ass_pd = pd.Series(data_gpp*30*60*10**-6, index = time ) 
    evap_pd = 30*60*pd.Series(data_et, index = time )  #mm/30min

    return evap_pd, ass_pd


main()

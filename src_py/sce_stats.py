#!/usr/bin/env python
# coding: utf-8
#***********************************************************************
#        sce_stats.py
#        Script to calculate some metrics of fit of a range of VOM-results 
#        based on SCE
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
import sys
import argparse
import numpy as np
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt


def main():

    parser = argparse.ArgumentParser(description="Script to calculate some metrics of fit of a range of VOM-results based on SCE")

    parser.add_argument("-i", "--inputfile", help="SCE_out from VOM")
    parser.add_argument("-o", "--outputfolder", help="outputfolder")    
    parser.add_argument("-w", "--workfolder", help="outputfolder")    
    parser.add_argument("-d", "--dailyweather", help="dailyweather.prn")    
    parser.add_argument("-p", "--percentage", help="percentage to keep", type=np.float) 
    parser.add_argument("-op", "--optpar", help="number of parameters", type=int, nargs='+')
    parser.add_argument("-eo", "--evap_obs", help="inputfile with observations evaporation")
    parser.add_argument("-ao", "--ass_obs", help="inputfile with observations assimilation")
    parser.add_argument("-c", "--code", help="code of VOM", nargs='+')                          
    args = parser.parse_args()

       
    try:
        if(len(args.optpar) != 8):
            raise ValueError
    except ValueError:
        print("Error: optpar must be of length 8")
        #exit the program
        sys.exit(1)


    ###########################################
    #load observed evaporation
    evap_obs = np.array([])
    dates_obs = np.array([])
    with open(args.evap_obs) as file1:
        for line in file1:
            tmp = line.split()
            evap_obs = np.append(evap_obs, float(tmp[2]) )
            dates_obs = np.append(dates_obs, tmp[0] )
    #make pandas series
    dates_obs = pd.date_range(dates_obs[0],periods=len( dates_obs ), freq='D')
    eobs_pd = pd.Series(evap_obs, index = dates_obs )

    #load observed assimilation
    ass_obs = np.array([])
    dates_obs = np.array([])
    with open(args.ass_obs) as file1:
        for line in file1:
            tmp = line.split()
            ass_obs = np.append(ass_obs, -float(tmp[2]) )
            dates_obs = np.append(dates_obs, tmp[0] )
    #make pandas series
    dates_obs = pd.date_range(dates_obs[0],periods=len( dates_obs ), freq='D')
    assobs_pd = pd.Series(ass_obs, index = dates_obs )

    #############################
    #select 10% best runs from sce
    params = np.loadtxt(args.inputfile) 

    par_default = [779.827, -1.32889, 1601.81, -0.564496, 0.300, 3.0, 100.0, 1.0]

    #sorts ascending and returns indices
    indsort = np.argsort(params[:, np.sum(args.optpar)])

    #make a new array
    indend = int(np.ceil(len(indsort)*args.percentage/100)-1)
    params_sorted = params[indsort[-indend:],:]

    print("keeping " + str(args.percentage) + "% of " + str(len(indsort)) + " solutions:")
    print(str(indend))

    #create temporary directory for VOM-input
    os.mkdir(args.workfolder + "/input")
    os.system('cp ' + args.dailyweather + ' ' + args.workfolder + "/input" )  

    #mkdir args.workfolder/output
    os.mkdir(args.workfolder + "/out")
    os.mkdir(args.workfolder + "/out_tot")

    #compile code
    os.system( "make --directory src/VOM/VOM_Fortran" )  

    #copy exe to workdir
    os.system( "cp src/VOM/VOM_Fortran/model.x " + args.workfolder + "/model.x" )  
    os.system( "rm src/VOM/VOM_Fortran/model.x " )  

    currdir = os.getcwd()
    os.chdir( args.workfolder)

    for j in range(0,indend):
        filenum = str(j + 1)
        param_tmp = par_default

        shiftpar = 0
        for ipar in range(0,8):
            #print(ipar)
            if(args.optpar[ipar] == 1):
                param_tmp[ipar] = params_sorted[j, shiftpar]
                shiftpar = shiftpar + 1


        param_tmp = np.asarray(param_tmp)
        param_tmp = param_tmp.reshape(1,len(param_tmp))

        #write pars.txt
        np.savetxt("input/pars.txt", param_tmp , delimiter=" " )

        #run model
        os.system( "./model.x" )
  
        #remove files, copy results_daily to temporary folder
        os.system( "rm " + "out/su_hourly.txt" )
        os.system( "rm "  + "out/delz_hourly.txt" )
        os.system( "rm " + "out/results_hourly.txt" )
        os.system( "rm "  + "out/ruptkt_hourly.txt" )
        os.system( "rm "  + "out/results_yearly.txt" )
        os.system( "rm "  + "out/rsurf*" )
        os.system( "cp " + "out/results_daily.txt " + "out_tot/results_daily" + filenum )
        os.system( "rm "  + "out/results_daily.txt" )

    #derive uncertainties
    #read data
    tmp = pd.read_csv( "out_tot/results_daily1", delim_whitespace=True)


    eKGE = np.zeros(( indend ))
    assKGE = np.zeros(( indend ))


    for j in range(0,indend):
        filenum = str(j + 1)

        tmp = pd.read_csv( "out_tot/results_daily" + filenum, delim_whitespace=True)
        e_tmp = 1000*(np.array(tmp[tmp.columns[26]]) + np.array(tmp[tmp.columns[27]]) + np.array(tmp[tmp.columns[10]]))
        ass_tmp = (np.array(tmp[tmp.columns[19]]) +  np.array(tmp[tmp.columns[20]] ))

        #make array of dates

        if j==0:
            #determine which dates overlap       
            dates_mod = pd.date_range(str(tmp[tmp.columns[2]][0]) + "/" +
                                      str(tmp[tmp.columns[1]][0]) + "/" +
                                      str(tmp[tmp.columns[0]][0]) ,periods=len( tmp[tmp.columns[0]] ), freq='D')

            dates_overlap = dates_mod.intersection(eobs_pd.index)
            print("Evaluating for:")
            print(dates_overlap[0])
            print(dates_overlap[-1])
            eRes = np.zeros((len(dates_overlap), indend ))
            assRes = np.zeros((len(dates_overlap), indend ))

        #calc KGE
        emod_pd = pd.Series(e_tmp, index = dates_mod )
        assmod_pd = pd.Series(ass_tmp, index = dates_mod )

        eKGE[j]  = calcKGE(emod_pd[dates_overlap], eobs_pd[dates_overlap])
        assKGE[j]  = calcKGE(assmod_pd[dates_overlap], assobs_pd[dates_overlap])
        #calc residuals
        eRes[:,j]  = calcResiduals(emod_pd[dates_overlap], eobs_pd[dates_overlap])
        assRes[:,j]  = calcResiduals(assmod_pd[dates_overlap], assobs_pd[dates_overlap])

    os.chdir( currdir )

 
    #write output files
    np.savetxt( args.outputfolder + "/KGE_evap.txt", eKGE, comments='', delimiter=" " )
    np.savetxt( args.outputfolder + "/KGE_ass.txt", assKGE, comments='', delimiter=" " )
    np.savetxt( args.outputfolder + "/Res_evap.txt", eRes, comments='', delimiter=" " )
    np.savetxt( args.outputfolder + "/Res_ass.txt", assRes, comments='', delimiter=" " )

    #clean up
    os.system( "rm -r " + args.workfolder + "/out")
    os.system( "rm -r " + args.workfolder + "/out_tot")
    os.system( "rm -r " + args.workfolder + "/input")
    os.system( "rm " + args.workfolder + "/model.x")

    print("finished!")

def calcKGE(sim, obs ):

        #mean value    
        mu_s = np.mean( sim )
        mu_o = np.mean( obs )

        #standard deviations
        sigma_s = np.std( sim )
        sigma_o = np.std( obs )

        #correlation coefficient
        r = np.corrcoef( sim, obs )[0,1]

        #variability term alpha = sigma_s / sigma_o
        alpha = sigma_s / sigma_o

        # bias term (mu_s / mu_o)
        beta = mu_s / mu_o

        #print(np.min(sim))
        KGE = 1- ((r-1)**2 + (alpha-1)**2 + (beta-1)**2)**0.5
        return(KGE)

def calcResiduals(sim, obs):

        residuals= (abs(sim) - abs(obs)) / np.std( abs(obs) )
        return(residuals)
main()






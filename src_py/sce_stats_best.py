import os
import sys
import argparse
import numpy as np
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt

#selects the best solutions of sce and makes pars.txt for re-running the VOM


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--inputfile", help="results_daily.txt")
    parser.add_argument("-o", "--outputfolder", help="outputfolder")    
    parser.add_argument("-eo", "--evap_obs", help="inputfile with observations evaporation")
    parser.add_argument("-ao", "--ass_obs", help="inputfile with observations assimilation")
    parser.add_argument("-s", "--startdry", help="months to start", type=int)     
    parser.add_argument("-e", "--enddry", help="months to end", type=int)  
    parser.add_argument("-sw", "--startwet", help="months to start", type=int)     
    parser.add_argument("-ew", "--endwet", help="months to end", type=int)  

    args = parser.parse_args()

       
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


    tmp = pd.read_csv( args.inputfile, delim_whitespace=True, header = 0)
    e_tmp = 1000*(np.array(tmp["esoil"]) + np.array(tmp["etmg"]) + np.array(tmp["etmt"]))
    ass_tmp = (np.array(tmp["assg"]) +  np.array(tmp["asst"] ))

    #make array of dates


    #determine which dates overlap       
    dates_mod = pd.date_range(str(tmp[tmp.columns[2]][0]) + "/" +
                              str(tmp[tmp.columns[1]][0]) + "/" +
                              str(tmp[tmp.columns[0]][0]) ,periods=len( tmp[tmp.columns[0]] ), freq='D')

    dates_overlap = dates_mod.intersection(eobs_pd.index)
    print("Evaluating for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    emod_pd = pd.Series(e_tmp, index = dates_mod )
    assmod_pd = pd.Series(ass_tmp, index = dates_mod )

    eKGE  = calcKGE(emod_pd[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(assmod_pd[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(emod_pd[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(assmod_pd[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(emod_pd[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(assmod_pd[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(emod_pd[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(assmod_pd[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)


    #calc residuals
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE ]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE ]

 
    #write output files
    np.savetxt( args.outputfolder + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.outputfolder + "/ass_beststats.txt", assresult, comments='', delimiter=" " )


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

def calcREmean(sim, obs ):

        #mean value    

        sim_annmean = sim.resample("A").mean()
        obs_annmean = obs.resample("A").mean()

        #remove first and last value to avoid incomplete series
        mu_s = np.mean( sim_annmean )
        mu_o = np.mean( obs_annmean )  

        #print(np.min(sim))
        RE = (mu_s-mu_o)/mu_o

        return(RE)


def calcREmean_seasonal(sim, obs, start, end ):

        if start < end:
            obs_sel =obs.loc[ (obs.index.month >= start) &  (obs.index.month <= end)]
            sim_sel =sim.loc[ (sim.index.month >= start) &  (sim.index.month <= end)]
        if start > end: 
            obs_sel =obs.loc[ (obs.index.month >= start) |  (obs.index.month <= end)]
            sim_sel =sim.loc[ (sim.index.month >= start) |  (sim.index.month <= end)]

        #residual errors
        mu_s = np.mean( sim_sel )
        mu_o = np.mean( obs_sel )  

        RE = (mu_s-mu_o)/mu_o
        return(RE)

main()






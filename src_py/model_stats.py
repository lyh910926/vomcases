import os
import sys
import argparse
import numpy as np
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
from netCDF4 import Dataset, num2date

#selects the best solutions of sce and makes pars.txt for re-running the VOM


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--bess", help="bess input files")
    parser.add_argument("--bios2", help="bios2 input files")
    parser.add_argument("--lpjguess", help="lpj-guess input files, first all files with et, second gpp", nargs="+")
    parser.add_argument("--maespa", help="maespa input files")
    parser.add_argument("--spa", help="spa input files")
    parser.add_argument("--cable", help="cable input files")

    parser.add_argument("--out_bess", help="outputfolder")
    parser.add_argument("--out_bios2", help="outputfolder")    
    parser.add_argument("--out_lpjguess", help="outputfolder")    
    parser.add_argument("--out_maespa", help="outputfolder")    
    parser.add_argument("--out_spa", help="outputfolder")    
    parser.add_argument("--out_cable", help="outputfolder")    
    
    parser.add_argument("-eo", "--evap_obs", help="inputfile with observations evaporation")
    parser.add_argument("-ao", "--ass_obs", help="inputfile with observations assimilation")
    parser.add_argument("-po", "--pc_obs", help="inputfile with observations projective cover")
    parser.add_argument("-pd", "--pc_obsdates", help="dates of fpar")
    parser.add_argument("-s", "--startdry", help="months to start", type=int)     
    parser.add_argument("-e", "--enddry", help="months to end", type=int)  
    parser.add_argument("-sw", "--startwet", help="months to start", type=int)     
    parser.add_argument("-ew", "--endwet", help="months to end", type=int)  

    args = parser.parse_args()

    ###################################
    #some constants for conversions
    lat_heat_vapor = 2.26   #[MJ/kg]
    rho_w = 997             #[kg/m3]
       
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
    eobs_pd = pd.Series(evap_obs, index = dates_obs ) #* lat_heat_vapor * rho_w * 1000/(3600*24) 

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
    #ass_obs = -1000000*ass_obs/ (3600*24)
    assobs_pd = pd.Series(ass_obs, index = dates_obs )


    #############################
    #read in data from BESS
    bess, bess_dates = read_bess(args.bess)
    bess_le = pd.Series(bess[:,0], index = bess_dates) #W/m2
    bess_et = 60*60*24* bess_le / ( lat_heat_vapor * rho_w * 1000)  #mm/d
    bess_gpp = pd.Series(bess[:,1], index = bess_dates) #umol/m2/s
    bess_gpp = 60*60*24*bess_gpp/1000000 #mol/m2/d

    #read in data from BIOS2
    bios2, bios2_dates = read_bios2(args.bios2)
    bios2_le = pd.Series(bios2[:,3], index = bios2_dates) #W/m2
    bios2_et = 60*60*24* bios2_le / ( lat_heat_vapor * rho_w * 1000)  #mm/d
    bios2_gpp = pd.Series(bios2[:,4], index = bios2_dates) #umol/m2/s
    bios2_gpp = 60*60*24*bios2_gpp/1000000 #mol/m2/d

    #read in data from LPJ-GUESS, ET in W/m2, GPP in umol/m2/s
    lpjguess, lpjguess2, lpjguess_dates = read_lpjguess(args.lpjguess[0], args.lpjguess[1])
    lpjguess_le = pd.Series(lpjguess, index = lpjguess_dates) #W/m2
    lpjguess_et = 60*60*24* lpjguess_le / ( lat_heat_vapor * rho_w * 1000)  #mm/d
    lpjguess_gpp = pd.Series(lpjguess2, index = lpjguess_dates) #umol/m2/s
    lpjguess_gpp = 60*60*24*lpjguess_gpp/1000000 #mol/m2/d

    #read in data from MAESPA, ET in W m-2, GPP in umol m-2 s-1
    maespa, maespa_dates = read_maespa(args.maespa)
    maespa_le = pd.Series(maespa[:,1], index = maespa_dates) #W/m2
    maespa_le = maespa_le.resample("D").sum()*30*60 #J/m2/d
    maespa_et = maespa_le / ( lat_heat_vapor * rho_w * 1000)  #mm/d
    maespa_gpp = pd.Series(maespa[:,0], index = maespa_dates) #umol/m2/s
    maespa_gpp = maespa_gpp.resample("D").sum()*30*60 #umol/m2/d
    maespa_gpp = maespa_gpp/1000000 #mol/m2/d
    maespa_dates = maespa_gpp.index

    #read in data from SPA, ET in W m-2, GPP in mmol m-2 s-1
    spa, spa_dates = read_spa(args.spa)
    spa_le = pd.Series(spa[:,1], index = spa_dates) #W/m2
    spa_le = spa_le.resample("D").sum()*30*60 #J/m2/d
    spa_et = spa_le / ( lat_heat_vapor * rho_w * 1000)  #mm/d
    spa_gpp = pd.Series(spa[:,0], index = spa_dates) #umol/m2/s
    spa_gpp = spa_gpp.resample("D").sum()*30*60 #umol/m2/d
    spa_gpp = -1.0*spa_gpp/1000000 #mol/m2/d

    #read in data from CABLE, ET in kg/m^2/s, GPP in umol/m^2/s
    cable, cable2, cable_dates = read_cable(args.cable)
    cable_le = pd.Series(cable * lat_heat_vapor * 1000 * 1000 , index = cable_dates) #W/m2
    cable_le = cable_le.resample("D").sum()*30*60 #J/m2/d
    cable_et = cable_le / ( lat_heat_vapor * rho_w * 1000)  #mm/d
    cable_gpp = pd.Series(cable2, index = cable_dates) #umol/m2/s
    cable_gpp = cable_gpp.resample("D").sum()*30*60 #umol/m2/d
    cable_gpp = cable_gpp/1000000 #mol/m2/d
    cable_dates = cable_gpp.index

    #############################
    #BESS statistics
    dates_overlap = bess_dates.intersection(eobs_pd.index)
    print("Evaluating BESS fluxes for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    eKGE  = calcKGE(bess_et[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(bess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(bess_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(bess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnn_mod, eMeanAnn_obs = calc_meanann(bess_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnn_mod, assMeanAnn_obs = calc_meanann(bess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMAE  = calcMAE(bess_et[dates_overlap], eobs_pd[dates_overlap])
    assMAE = calcMAE(bess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(bess_et[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(bess_gpp[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(bess_et[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(bess_gpp[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)

    eAmpRE = calcAmpRE(bess_et, bess_et.index, evap_obs, dates_obs )
    assAmpRE = calcAmpRE(bess_gpp, bess_gpp.index, ass_obs, dates_obs )

    eBIAS = calcBIAS(bess_et[dates_overlap], eobs_pd[dates_overlap])
    assBIAS = calcBIAS(bess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMinAnnRE  = calcREmin(bess_et[dates_overlap], eobs_pd[dates_overlap])
    assMinAnnRE  = calcREmin(bess_gpp[dates_overlap], assobs_pd[dates_overlap])

    #put results together
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE, eMAE, eAmpRE, eBIAS, eMinAnnRE, eMeanAnn_mod, eMeanAnn_obs ]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE, assMAE, assAmpRE, assBIAS, assMinAnnRE, assMeanAnn_mod, assMeanAnn_obs ]
 
    #write output files
    np.savetxt( args.out_bess + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.out_bess + "/ass_beststats.txt", assresult, comments='', delimiter=" " )

    #############################
    #BIOS2 statistics
    dates_overlap = bios2_dates.intersection(eobs_pd.index)
    print("Evaluating BIOS2 fluxes for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    eKGE  = calcKGE(bios2_et[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(bios2_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(bios2_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(bios2_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnn_mod, eMeanAnn_obs = calc_meanann(bios2_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnn_mod, assMeanAnn_obs = calc_meanann(bios2_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMAE  = calcMAE(bios2_et[dates_overlap], eobs_pd[dates_overlap])
    assMAE = calcMAE(bios2_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(bios2_et[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(bios2_gpp[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(bios2_et[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(bios2_gpp[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)

    eAmpRE = calcAmpRE(bios2_et, bios2_et.index, evap_obs, dates_obs )
    assAmpRE = calcAmpRE(bios2_gpp, bios2_gpp.index, ass_obs, dates_obs )

    eBIAS = calcBIAS(bios2_et[dates_overlap], eobs_pd[dates_overlap])
    assBIAS = calcBIAS(bios2_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMinAnnRE  = calcREmin(bios2_et[dates_overlap], eobs_pd[dates_overlap])
    assMinAnnRE  = calcREmin(bios2_gpp[dates_overlap], assobs_pd[dates_overlap])

    #put results together
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE, eMAE, eAmpRE, eBIAS, eMinAnnRE, eMeanAnn_mod, eMeanAnn_obs]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE, assMAE, assAmpRE, assBIAS, assMinAnnRE, assMeanAnn_mod, assMeanAnn_obs]
 
    #write output files
    np.savetxt( args.out_bios2 + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.out_bios2 + "/ass_beststats.txt", assresult, comments='', delimiter=" " )

   #############################
    #LPJ-GUESS statistics
    dates_overlap = lpjguess_dates.intersection(eobs_pd.index)
    print("Evaluating LPJ-GUESS fluxes for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    eKGE  = calcKGE(lpjguess_et[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(lpjguess_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnn_mod, eMeanAnn_obs = calc_meanann(lpjguess_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnn_mod, assMeanAnn_obs = calc_meanann(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMAE  = calcMAE(lpjguess_et[dates_overlap], eobs_pd[dates_overlap])
    assMAE = calcMAE(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(lpjguess_et[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(lpjguess_et[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)

    eAmpRE = calcAmpRE(lpjguess_et, lpjguess_et.index, evap_obs, dates_obs )
    assAmpRE = calcAmpRE(lpjguess_gpp, lpjguess_gpp.index, ass_obs, dates_obs )

    eBIAS = calcBIAS(lpjguess_et[dates_overlap], eobs_pd[dates_overlap])
    assBIAS = calcBIAS(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMinAnnRE  = calcREmin(lpjguess_et[dates_overlap], eobs_pd[dates_overlap])
    assMinAnnRE  = calcREmin(lpjguess_gpp[dates_overlap], assobs_pd[dates_overlap])

    #put results together
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE, eMAE, eAmpRE, eBIAS, eMinAnnRE, eMeanAnn_mod, eMeanAnn_obs ]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE, assMAE, assAmpRE, assBIAS, assMinAnnRE, assMeanAnn_mod, assMeanAnn_obs]
 
    #write output files
    np.savetxt( args.out_lpjguess + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.out_lpjguess + "/ass_beststats.txt", assresult, comments='', delimiter=" " )

    #############################
    #maespa statistics
    dates_overlap = maespa_dates.intersection(eobs_pd.index)
    print("Evaluating MAESPA fluxes for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    eKGE  = calcKGE(maespa_et[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(maespa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(maespa_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(maespa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnn_mod, eMeanAnn_obs = calc_meanann(maespa_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnn_mod, assMeanAnn_obs = calc_meanann(maespa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMAE  = calcMAE(maespa_et[dates_overlap], eobs_pd[dates_overlap])
    assMAE = calcMAE(maespa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(maespa_et[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(maespa_gpp[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(maespa_et[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(maespa_gpp[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)

    eAmpRE = calcAmpRE(maespa_et, maespa_et.index, evap_obs, dates_obs )
    assAmpRE = calcAmpRE(maespa_gpp, maespa_gpp.index, ass_obs, dates_obs )

    eBIAS = calcBIAS(maespa_et[dates_overlap], eobs_pd[dates_overlap])
    assBIAS = calcBIAS(maespa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMinAnnRE  = calcREmin(maespa_et[dates_overlap], eobs_pd[dates_overlap])
    assMinAnnRE  = calcREmin(maespa_gpp[dates_overlap], assobs_pd[dates_overlap])

    #put results together
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE, eMAE, eAmpRE, eBIAS, eMinAnnRE, eMeanAnn_mod, eMeanAnn_obs ]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE, assMAE, assAmpRE, assBIAS, assMinAnnRE, assMeanAnn_mod, assMeanAnn_obs]
 
    #write output files
    np.savetxt( args.out_maespa + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.out_maespa + "/ass_beststats.txt", assresult, comments='', delimiter=" " )

    #############################
    #spa statistics
    dates_overlap = spa_dates.intersection(eobs_pd.index)
    print("Evaluating SPA fluxes for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    eKGE  = calcKGE(spa_et[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(spa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(spa_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(spa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnn_mod, eMeanAnn_obs = calc_meanann(spa_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnn_mod, assMeanAnn_obs = calc_meanann(spa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMAE  = calcMAE(spa_et[dates_overlap], eobs_pd[dates_overlap])
    assMAE = calcMAE(spa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(spa_et[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(spa_gpp[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(spa_et[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(spa_gpp[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)

    eAmpRE = calcAmpRE(spa_et, spa_et.index, evap_obs, dates_obs )
    assAmpRE = calcAmpRE(spa_gpp, spa_gpp.index, ass_obs, dates_obs )

    eBIAS = calcBIAS(spa_et[dates_overlap], eobs_pd[dates_overlap])
    assBIAS = calcBIAS(spa_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMinAnnRE  = calcREmin(spa_et[dates_overlap], eobs_pd[dates_overlap])
    assMinAnnRE  = calcREmin(spa_gpp[dates_overlap], assobs_pd[dates_overlap])

    #put results together
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE, eMAE, eAmpRE, eBIAS, eMinAnnRE, eMeanAnn_mod, eMeanAnn_obs ]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE, assMAE, assAmpRE, assBIAS, assMinAnnRE, assMeanAnn_mod, assMeanAnn_obs ]
 
    #write output files
    np.savetxt( args.out_spa + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.out_spa + "/ass_beststats.txt", assresult, comments='', delimiter=" " )

    #############################
    #cable statistics
    dates_overlap = cable_dates.intersection(eobs_pd.index)
    print("Evaluating CABLE fluxes for:")
    print(dates_overlap[0])
    print(dates_overlap[-1])

    #calc KGE
    eKGE  = calcKGE(cable_et[dates_overlap], eobs_pd[dates_overlap])
    assKGE  = calcKGE(cable_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnnRE  = calcREmean(cable_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnnRE  = calcREmean(cable_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanAnn_mod, eMeanAnn_obs   = calc_meanann(cable_et[dates_overlap], eobs_pd[dates_overlap])
    assMeanAnn_mod, assMeanAnn_obs  = calc_meanann(cable_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMAE  = calcMAE(cable_et[dates_overlap], eobs_pd[dates_overlap])
    assMAE = calcMAE(cable_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMeanSeas1RE  = calcREmean_seasonal(cable_et[dates_overlap], eobs_pd[dates_overlap], args.startdry, args.enddry)
    assMeanSeas1RE  = calcREmean_seasonal(cable_gpp[dates_overlap], assobs_pd[dates_overlap], args.startdry, args.enddry)

    eMeanSeas2RE  = calcREmean_seasonal(cable_et[dates_overlap], eobs_pd[dates_overlap], args.startwet, args.endwet)
    assMeanSeas2RE  = calcREmean_seasonal(cable_gpp[dates_overlap], assobs_pd[dates_overlap], args.startwet, args.endwet)

    eAmpRE = calcAmpRE(cable_et, cable_et.index, evap_obs, dates_obs )
    assAmpRE = calcAmpRE(cable_gpp, cable_gpp.index, ass_obs, dates_obs )

    eBIAS = calcBIAS(cable_et[dates_overlap], eobs_pd[dates_overlap])
    assBIAS = calcBIAS(cable_gpp[dates_overlap], assobs_pd[dates_overlap])

    eMinAnnRE  = calcREmin(cable_et[dates_overlap], eobs_pd[dates_overlap])
    assMinAnnRE  = calcREmin(cable_gpp[dates_overlap], assobs_pd[dates_overlap])

    #put results together
    eresult = [ eKGE, eMeanAnnRE, eMeanSeas1RE, eMeanSeas2RE, eMAE, eAmpRE, eBIAS, eMinAnnRE, eMeanAnn_mod, eMeanAnn_obs ]
    assresult = [ assKGE, assMeanAnnRE, assMeanSeas1RE, assMeanSeas2RE, assMAE, assAmpRE, assBIAS, assMinAnnRE, assMeanAnn_mod, assMeanAnn_obs ]
 
    #write output files
    np.savetxt( args.out_cable + "/evap_beststats.txt", eresult, comments='', delimiter=" " )
    np.savetxt( args.out_cable + "/ass_beststats.txt", assresult, comments='', delimiter=" " )




    print("finished!")

def calcKGE(sim, obs ):

        #mean value    
        mu_s = np.nanmean( sim )
        mu_o = np.nanmean( obs )

        #standard deviations
        sigma_s = np.nanstd( sim )
        sigma_o = np.nanstd( obs )

        #correlation coefficient
        r = np.corrcoef( sim[~np.isnan(sim)], obs[~np.isnan(sim)] )[0,1]

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

def calc_meanann(sim, obs ):

        #mean value    

        sim_annmean = sim.resample("A").sum()
        obs_annmean = obs.resample("A").sum()

        #remove first and last value to avoid incomplete series
        mu_s = np.mean( sim_annmean )
        mu_o = np.mean( obs_annmean )  

        return(mu_s, mu_o)

def calcMAE(sim, obs ):

        MAE  = np.nanmean(abs(sim - obs))

        return(MAE)



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


def read_bess(infile):

    data = np.loadtxt(infile, delimiter=",") 
    time = pd.date_range("01-01-2000", periods = len(data[:,0]), freq='D')

    return data, time

def read_bios2(infile):

    data = np.loadtxt(infile, delimiter=",") 
    time = pd.date_range(datetime(int(data[0,0]),int(data[0,1]),int(data[0,2])), 
              datetime(int(data[-1,0]),int(data[-1,1]),int(data[-1,2])),freq='D')

    return data, time

def read_lpjguess(infile_et, infile_gpp):
    data_et = np.loadtxt(infile_et, skiprows=1, usecols=3)
    data_gpp = np.loadtxt(infile_gpp, skiprows=1, usecols=3)
    time_tmp = np.loadtxt(infile_gpp, skiprows=1)
    time = pd.date_range(datetime(int(time_tmp[0,0]),int(time_tmp[0,1]),int(time_tmp[0,2])), 
              datetime(int(time_tmp[-1,0]),int(time_tmp[-1,1]),int(time_tmp[-1,2])),freq='D')

    return data_et, data_gpp, time

def read_maespa(infile):

    data = np.loadtxt(infile, delimiter=",", skiprows=3, usecols=(3,6))
    data[data == -9999.9] = np.nan
    data[data == -999] = np.nan
    data[data == -1388055] = np.nan
    time_tmp = np.loadtxt(infile, delimiter=",", dtype=np.str, skiprows=3, usecols=0)
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    return data, time

def read_spa(infile):
    data = np.loadtxt(infile, delimiter=",", skiprows=1, usecols=(1,3))
    time_tmp = np.loadtxt(infile, delimiter=",", dtype=np.str, skiprows=1, usecols=0)
    time = pd.date_range(time_tmp[0], time_tmp[-1],freq='30min')

    return data, time

def read_cable(infile):
    ncfile = Dataset(infile)
    data_gpp = np.squeeze(ncfile.variables["GPP"]) # extract variable
    data_et = np.squeeze(ncfile.variables["Evap"]) # extract variable
    time_tmp = np.squeeze(ncfile.variables["time"]) # extract variable
    time_unit = ncfile.variables["time"].units
    time_tmp2 = num2date(time_tmp,units = time_unit,calendar = 'gregorian')
    #time_tmp = [pd.to_datetime("2007-01-01 00:01:00") + pd.Timedelta(seconds=i) for i in time_tmp]
    time = pd.date_range(time_tmp2[0], time_tmp2[-1],freq='30min')

    return data_et, data_gpp, time

def calcAmpRE(vals, time, vals_obs, time_obs):    
    
    ens = np.zeros([366])
    ens7d = np.zeros([367])    

    enso = np.zeros([366])
    enso7d = np.zeros([367])      


    DOY = time.dayofyear[0:len(vals)] 
    DOYobs = time_obs.dayofyear[0:len(vals_obs)] 

    for iday in range(0,366):
        ens[iday] = np.nanmean( vals[DOY == (iday+1)]  ) 
        enso[iday] = np.nanmean( vals_obs[DOYobs == (iday+1)]  ) 


    #7-day running mean
    N = 7
    for iday in range(0,367):
        if iday > (366-N):
            ens7d[iday]  = np.nanmean( np.concatenate( (ens[iday:366], ens[0:(N-(366-iday))] )) )
            enso7d[iday]  = np.nanmean( np.concatenate( (enso[iday:366], enso[0:(N-(366-iday))] )) )
        else:    
            ens7d[iday] = np.nanmean(ens[iday:(iday+N)])
            enso7d[iday] = np.nanmean(enso[iday:(iday+N)])   

    ampl = np.max(ens7d) - np.min(ens7d)
    amplo = np.max(enso7d) - np.min(enso7d)            


    RE = (ampl - amplo)/amplo

    return RE


def calcBIAS(sim, obs ):

        BIAS  = np.nanmean(sim - obs)

        return(BIAS)

def calcREmin(sim, obs ):

        #mean value    

        sim_annmin = sim.resample("A").min()
        obs_annmin = obs.resample("A").min()

        #remove first and last value to avoid incomplete series
        mu_s = np.mean( sim_annmin )
        mu_o = np.mean( obs_annmin )  

        #print(np.min(sim))
        MIN_ERR = (mu_s-mu_o)/mu_o

        return(MIN_ERR)

main()






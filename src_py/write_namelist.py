import numpy as np
import os
import sys
import argparse
from netCDF4 import Dataset
import pandas as pd
import csv
import re

#file to prepare meterological data from SILO
#and CO2 from Mauna Loa for applying it in
#the Vegetation Optimality Model (VOM)
#output: 
#dailyweather.prn: input file VOM
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--outputfile", help="outputfile")
    parser.add_argument("-is", "--input_stats", help="file with statistics on elevation")

    parser.add_argument("--i_alpha", default="0.3d0", help="initial slope of j(par) curve")
    parser.add_argument("--i_cpccf", default="0.2d-6", help="water transport cost factor (cpcc=pc*rootdepth*cpccf) in mol/m/m2/s")
    parser.add_argument("--i_tcf", default="2.2d-7", help="turnover cost factor for foliage (tc=tcf*LAI) in mol/m2/s")
    parser.add_argument("--i_maxyear", default="37", help="number of years to process")
    parser.add_argument("--i_testyear", default="1", help="number of years after which to perform initial test of netass")
    parser.add_argument("--i_ha", default="43790.0d0", help="parameters to calculate jmax(temp)")
    parser.add_argument("--i_hd", default="2.0d5", help="parameters to calculate jmax(temp)")
    parser.add_argument("--i_toptf", default="0.0d0", help="parameter to calculate adaptation of topt (range 0-1, 0.0 means no adaption, 1.0 means topt=tair)")
    parser.add_argument("--i_toptstart", default="305.0d0", help="start parameter for topt to calculate jmax(temp in K)")
    parser.add_argument("--i_rlratio", default="0.07d0", help="leaf respiration parameter (rl=rlratio*assmax)")
    parser.add_argument("--i_mdtf", default="10000.0d0", help="total dry mass of living tissues of trees per unit pc g/m^2")
    parser.add_argument("--i_mqxtf", default="1.0d0", help="total water storage capacity in living tissues of trees per unit md")
    parser.add_argument("--i_rrootm", default="1.02d8", help="root water uptake resistivity in s")
    parser.add_argument("--i_rsurfmin", default="0.03d0", help="minimum root area per m^3 to be maintained")
    parser.add_argument("--i_rsurf_", default="0.3d0", help="initial root surface area per m^3")
    parser.add_argument("--i_rootrad", default="0.3d-3", help="fine root radius in m")
    parser.add_argument("--i_prootmg", default="150.0d0", help="constant root balance pressure of 1.5 MPa in grasses")
    parser.add_argument("--i_growthmax", default="0.1d0", help="parameter determining maximum daily growth increment of root surface area")
    parser.add_argument("--i_incrcovg", default="0.02d0", help="parameter determining maximum increment percentage of grass cover")
    parser.add_argument("--i_incrjmax", default="0.01d0", help="parameter determining maximum increment percentage of jmax25")
    parser.add_argument("--i_incrlait", default="0.02d0", help="parameter determining maximum increment percentage of LAI grasses")
    parser.add_argument("--i_incrlaig", default="0.02d0", help="parameter determining maximum increment percentage of LAI trees")
    parser.add_argument("--i_extcoeffg", default="0.5d0", help="extinction coefficient beer's law grasses")
    parser.add_argument("--i_extcoefft", default="0.5d0", help="extinction coefficient beer's law trees")
    parser.add_argument("--i_firstyear", default="2000", help="firstyear for the generation of hourly output in computation mode")
    parser.add_argument("--i_lastyear", default="2000", help="lastyear for the generation of hourly output in computation mode")
    parser.add_argument("--i_write_h", default="0", help="flag to greate a file with hourly values from daily values")
    parser.add_argument("--i_read_pc", default="0", help="flag to read vegetation coverage values from file")
    parser.add_argument("--i_lai_function", default="1", help="switch for 1) linear or 2) exponential function of LAI for foliage cost")
    parser.add_argument("--i_inputpath", default="'input/'", help="path to folder with inputfiles ")
    parser.add_argument("--i_outputpath", default="'output/'", help="path to folder with outputfiles ")
    parser.add_argument("--o_lambdagf", default="0.779827d3", help="factor for calculating lambdag_d")
    parser.add_argument("--o_wsgexp", default="-0.132889d1", help="exponent for calculating lambdag")
    parser.add_argument("--o_lambdatf", default="0.160181d4", help="factor for calculating lambdat_d")
    parser.add_argument("--o_wstexp", default="-0.564496d0", help="exponent for calculating lambdat_d")
    parser.add_argument("--o_cai", default="0.3d0", help="projected cover perennial vegetation (0-1)")
    parser.add_argument("--o_rtdepth", default="0.3d1", help="tree rooting depth (m)")
    parser.add_argument("--o_mdstore", default="1.0d2", help="wood water storage parameter of trees (can be in shufflepar)")
    parser.add_argument("--o_rgdepth", default="0.1d1", help="root depth grasses (can be in shufflepar)")

    parser.add_argument("--i_lat", help="geogr. latitude in degrees ")
    parser.add_argument("--i_cz", help="average soil elevation in m ")
    parser.add_argument("--i_cgs", help="Capital Gamma S (length scale for seepage outflow REG) (m) ")
    parser.add_argument("--i_zr", help="average channel bed elevation in m")
    parser.add_argument("--i_go", help="slope close to channel in radians")
    parser.add_argument("--i_ksat", default="1.9d-6", help="Saturated hydraulic conductivity in [m/s]")
    parser.add_argument("--i_thetar", default="0.065d0", help="residual soil moisture")
    parser.add_argument("--i_thetas", default="0.41d0", help="saturated soil moisture")
    parser.add_argument("--i_nvg", default="1.89d0", help="van Genuchten soil parameter n")
    parser.add_argument("--i_avg", default="7.5d0", help="van Genuchten soil parameter alpha (1/m)")
    parser.add_argument("--i_delz", default="0.2", help="thickness of soil sublayers (m)")

    parser.add_argument("--vom_command", default="1", help="COMMAND LINE TO RUN ASSIMILATION MODEL (1 for -optimise with sce, 2 for -run without optization with pars.txt, 3 for run for ncp only with pars.txt, 4 for optimise without random_seed)")
    parser.add_argument("--i_ncomp_", default="2", help="MAXIMUM NUMBER OF COMPLEXES (p)")
    parser.add_argument("--i_ncompmin", default="2", help="MINIMUM NUMBER OF COMPLEXES (pmin)")
    parser.add_argument("--i_resolution", default="1.0", help="RESOLUTION OF OPTIMISATION (% OF MAX VARIATION WHEN OPTIMISATION STOPS)")
    parser.add_argument("--i_patience", default="10", help="NUMBER OF LOOPS WITHOUT INCREASE IN OF BEFORE OPTIMISATION STOPS")
    parser.add_argument("--i_nsimp", default="3", help="NUMBER OF OPTIMISATIONS PER COMPLEX AND RUN")
    parser.add_argument("--i_focus", default="1.0", help="IF <1.0, THE SPREAD OF THE RANDOM SEED AROUND THE INITIAL VALUES IS LIMITED")
    parser.add_argument("--i_iter", default="10", help="Maximum iterations in case of random runs")
    parser.add_argument("--vom_npar", default="8", help="number of parameters in shuffle2par used for optimization in SCE")
    parser.add_argument("--n_thread", default="4", help="number of threads to be used in parallel")

    parser.add_argument("--min_lambdagf", default="0.0d0", help="factor for calculating lambdag_d")
    parser.add_argument("--min_wsgexp", default="-3.0d0", help="exponent for calculating lambdag")
    parser.add_argument("--min_lambdatf", default="0.0d0", help="factor for calculating lambdat_d")
    parser.add_argument("--min_wstexp", default="-3.0d0", help="exponent for calculating lambdat_d")
    parser.add_argument("--min_cai", default="0.0d0", help="projected cover perennial vegetation (0-1)")
    parser.add_argument("--min_rtdepth", default="1.0d0", help="tree rooting depth (m)")
    parser.add_argument("--min_mdstore", default="0.9d2", help="wood water storage parameter of trees (can be in shufflepar)")
    parser.add_argument("--min_rgdepth", default="0.05d0", help="root depth grasses (can be in shufflepar)")

    parser.add_argument("--min_cgs", default="10.0d0", help="Capital Gamma S (length scale for seepage outflow REG) (m) ")
    parser.add_argument("--min_zr", default="1.0d0", help="average channel bed elevation in m")
    parser.add_argument("--min_go", default="0.003d0", help="slope close to channel in radians")
    parser.add_argument("--min_ksat", default="1.00d-6", help="Saturated hydraulic conductivity in [m/s]")
    parser.add_argument("--min_thetar", default="0.055d0", help="residual soil moisture")
    parser.add_argument("--min_thetas", default="0.20d0", help="saturated soil moisture")
    parser.add_argument("--min_nvg", default="1.2d0", help="van Genuchten soil parameter n")
    parser.add_argument("--min_avg", default="1.5d0",  help="van Genuchten soil parameter alpha (1/m)")

    parser.add_argument("--max_lambdagf", default="1.0d04", help="factor for calculating lambdag_d")
    parser.add_argument("--max_wsgexp", default="1.0d0", help="exponent for calculating lambdag")
    parser.add_argument("--max_lambdatf", default="1.0d04", help="factor for calculating lambdat_d")
    parser.add_argument("--max_wstexp", default="1.0d0", help="exponent for calculating lambdat_d")
    parser.add_argument("--max_cai", default="1.0d0", help="projected cover perennial vegetation (0-1)")
    parser.add_argument("--max_rtdepth", default="9.0d0", help="tree rooting depth (m)")
    parser.add_argument("--max_mdstore", default="1.1d2", help="wood water storage parameter of trees (can be in shufflepar)")
    parser.add_argument("--max_rgdepth", default="2.0d0", help="root depth grasses (can be in shufflepar)")

    parser.add_argument("--max_cgs", default="1000.0d0", help="Capital Gamma S (length scale for seepage outflow REG) (m) ")
    parser.add_argument("--max_zr", default="36.47d0", help="average channel bed elevation in m")
    parser.add_argument("--max_go", default="0.133d0", help="slope close to channel in radians")
    parser.add_argument("--max_ksat", default="1.50d-5", help="Saturated hydraulic conductivity in [m/s]")
    parser.add_argument("--max_thetar", default="0.075d0", help="residual soil moisture")
    parser.add_argument("--max_thetas", default="0.50d0", help="saturated soil moisture")
    parser.add_argument("--max_nvg", default="2.0d0", help="van Genuchten soil parameter n")
    parser.add_argument("--max_avg", default="10.0d0",  help="van Genuchten soil parameter alpha (1/m)")

    parser.add_argument("--opt_lambdagf", default="1", help="optimize factor for calculating lambdag_d")
    parser.add_argument("--opt_wsgexp", default="1", help="optimize exponent for calculating lambdag")
    parser.add_argument("--opt_lambdatf", default="1", help="optimize factor for calculating lambdat_d")
    parser.add_argument("--opt_wstexp", default="1", help="optimize exponent for calculating lambdat_d")
    parser.add_argument("--opt_cai", default="1", help="optimize projected cover perennial vegetation (0-1)")
    parser.add_argument("--opt_rtdepth", default="1", help="optimize tree rooting depth (m)")
    parser.add_argument("--opt_mdstore", default="0", help="optimize wood water storage parameter of trees (can be in shufflepar)")
    parser.add_argument("--opt_rgdepth", default="1", help="optimize root depth grasses (can be in shufflepar)")

    parser.add_argument("--opt_cgs", default="0", help="optimize Capital Gamma S (length scale for seepage outflow REG) (m) ")
    parser.add_argument("--opt_zr", default="0", help="optimize average channel bed elevation in m")
    parser.add_argument("--opt_go", default="0", help="optimize slope close to channel in radians")
    parser.add_argument("--opt_ksat", default="0", help="optimize Saturated hydraulic conductivity in [m/s]")
    parser.add_argument("--opt_thetar", default="0", help="optimize residual soil moisture")
    parser.add_argument("--opt_thetas", default="0", help="optimize saturated soil moisture")
    parser.add_argument("--opt_nvg", default="0", help="optimize van Genuchten soil parameter n")
    parser.add_argument("--opt_avg", default="0",  help="optimize van Genuchten soil parameter alpha (1/m)")

    args = parser.parse_args()



    ################################################################################################
    #read statistics from file
    area_tmp = 0.0

    if(args.input_stats is not None):

        file_stats = open(args.input_stats,"r") 
        for line in file_stats:
            elev="Elevation statistics:" in line
            slopes="Statistics of slopes:" in line
            area="cat|area" in line
            finished="===============" in line

            if(elev == True):
                reading_slopes = False
                reading_elev = True
                reading_area = False

            if(slopes == True):
                reading_slopes = True
                reading_elev = False
                reading_area = False

            if(area == True):
                reading_slopes = False
                reading_elev = False
                reading_area = True

            maxs = "maximum" in line
            mins = "minimum" in line
            means = "mean" in line

            if( (maxs == True) & (reading_elev == True) & (args.i_cz == None) ): 
                args.i_cz = str(float(line.split(":")[1]))

            if( (mins == True) & (reading_elev == True) & (args.i_zr == None) ): 
                args.i_zr = str(float(line.split(":")[1]))

            if( (means == True) & (reading_slopes == True) & (args.i_go == None) ): 
                args.i_go = str(float(line.split(":")[1]) * np.pi/180)

            if(reading_area == True ): 
                header="cat|area" in line
                if( (not(header)) & (finished == False) ):
                    area_tmp = area_tmp + float(line.split("|")[1])
        file_stats.close()

        if( (area_tmp > 0) & (args.i_cgs == None) ):
            args.i_cgs = str(np.sqrt(area_tmp/np.pi))

    #correct i_cz and i_zr, make sure both can be divided by i_delz
    cz_tmp = float(args.i_cz)
    zr_tmp = float(args.i_zr)
    delz_tmp = float(args.i_delz)

    remainder = cz_tmp % delz_tmp
    if(remainder > 0.5*delz_tmp):
        cz_tmp = round(cz_tmp + (delz_tmp-remainder), 2)
        args.i_cz = str(cz_tmp)

    remainder = zr_tmp % delz_tmp
    if(remainder > 0.5*delz_tmp):
        zr_tmp = round(zr_tmp + (delz_tmp-remainder), 2)
        args.i_zr = str(zr_tmp)



    ################################################################################################
    #write to file
    file = open(args.outputfile,"w") 

    file.write("&inputpar\n")
    file.write("i_alpha="+ args.i_alpha + ",          ! initial slope of j(par) curve\n")
    file.write("i_cpccf="+ args.i_cpccf + ",         ! water transport cost factor (cpcc=pc*rootdepth*cpccf) in mol/m/m2/s\n")
    file.write("i_tcf="+ args.i_tcf + ",           ! turnover cost factor for foliage (tc=tcf*LAI) in mol/m2/s\n")
    file.write("i_maxyear="+ args.i_maxyear + ",           ! number of years to process\n")
    file.write("i_testyear="+ args.i_testyear + ",           ! number of years after which to perform initial test of netass\n")
    file.write("i_ha="+ args.i_ha + ",         ! parameters to calculate jmax(temp)\n")
    file.write("i_hd="+ args.i_hd + ",             ! parameters to calculate jmax(temp)\n")
    file.write("i_toptf="+ args.i_toptf + ",          ! parameter to calculate adaptation of topt (range 0-1, 0.0 means no adaption, 1.0 means topt=tair)\n")
    file.write("i_toptstart="+ args.i_toptstart + ",    ! start parameter for topt to calculate jmax(temp in K)\n")
    file.write("i_rlratio="+ args.i_rlratio + ",       ! leaf respiration parameter (rl=rlratio*assmax)\n")
    file.write("i_mdtf="+ args.i_mdtf + ",       ! total dry mass of living tissues of trees per unit pc g/m^2\n")
    file.write("i_mqxtf="+ args.i_mqxtf + ",          ! total water storage capacity in living tissues of trees per unit md\n")
    file.write("i_rrootm="+ args.i_rrootm + ",        ! root water uptake resistivity in s\n")
    file.write("i_rsurfmin="+ args.i_rsurfmin + ",      ! minimum root area per m^3 to be maintained\n")
    file.write("i_rsurf_="+ args.i_rsurf_ + ",         ! initial root surface area per m^3\n")
    file.write("i_rootrad="+ args.i_rootrad + ",       ! fine root radius in m\n")
    file.write("i_prootmg="+ args.i_prootmg + ",      ! constant root balance pressure of 1.5 MPa in grasses\n")
    file.write("i_growthmax="+ args.i_growthmax + ",      ! parameter determining maximum daily growth increment of root surface area\n")
    file.write("i_incrcovg="+ args.i_incrcovg + ",      ! parameter determining maximum increment percentage of grass cover\n")
    file.write("i_incrjmax="+ args.i_incrjmax + ",      ! parameter determining maximum increment percentage of jmax25\n")
    file.write("i_incrlait="+ args.i_incrlait + ",      ! parameter determining maximum increment percentage of LAI grasses\n")
    file.write("i_incrlaig="+ args.i_incrlaig + ",      ! parameter determining maximum increment percentage of LAI trees\n")
    file.write("i_extcoeffg="+ args.i_extcoeffg + ",      ! extinction coefficient beer's law grasses\n")
    file.write("i_extcoefft="+ args.i_extcoefft + ",      ! extinction coefficient beer's law trees\n")
    file.write("i_firstyear="+ args.i_firstyear + ",       ! firstyear for the generation of hourly output in computation mode\n")
    file.write("i_lastyear="+ args.i_lastyear + ",        ! lastyear for the generation of hourly output in computation mode\n")
    file.write("i_write_h="+ args.i_write_h + ",            ! flag to greate a file with hourly values from daily values\n")
    file.write("i_read_pc="+ args.i_read_pc + ",            ! flag to read vegetation coverage values from file\n")
    file.write("i_lai_function="+ args.i_lai_function + ",       ! switch for 1) linear or 2) exponential function of LAI for foliage cost\n")
    file.write("i_inputpath = "+ args.i_inputpath + ",   ! path to folder with inputfiles\n")
    file.write("i_outputpath = "+ args.i_outputpath + ",   ! path to folder with outputfiles\n")
    file.write("o_lambdagf="+ args.o_lambdagf + ",  ! factor for calculating lambdag_d\n")
    file.write("o_wsgexp="+ args.o_wsgexp + ",   ! exponent for calculating lambdag\n")
    file.write("o_lambdatf="+ args.o_lambdatf + ",  ! factor for calculating lambdat_d\n")
    file.write("o_wstexp="+ args.o_wstexp + ",   ! exponent for calculating lambdat_d\n")
    file.write("o_cai="+ args.o_cai + ",            ! projected cover perennial vegetation (0-1)\n")
    file.write("o_rtdepth="+ args.o_rtdepth + ",        ! tree rooting depth (m)\n")
    file.write("o_mdstore="+ args.o_mdstore + ",        ! wood water storage parameter of trees (can be in shufflepar)\n")
    file.write("o_rgdepth="+ args.o_rgdepth + ",        ! root depth grasses (can be in shufflepar)\n")
    file.write("&end")
    file.write("&input2par\n")
    file.write("i_lat="+ args.i_lat + ",           ! geogr. latitude in degrees\n") 
    file.write("i_cz="+ args.i_cz + ",            ! average soil elevation in m \n")
    file.write("i_cgs="+ args.i_cgs + ",            ! Capital Gamma S (length scale for seepage outflow REG) (m) \n")
    file.write("i_zr="+ args.i_zr + ",            ! average channel bed elevation in m\n")
    file.write("i_go="+ args.i_go + ",           ! slope close to channel in radians\n")
    file.write("i_ksat="+ args.i_ksat + ",           ! Saturated hydraulic conductivity in [m/s]\n")
    file.write("i_thetar="+ args.i_thetar + ",        ! residual soil moisture\n")
    file.write("i_thetas="+ args.i_thetas + ",         ! saturated soil moisture\n")
    file.write("i_nvg="+ args.i_nvg + ",            ! van Genuchten soil parameter n\n")
    file.write("i_avg="+ args.i_avg + ",             ! van Genuchten soil parameter alpha (1/m)\n")
    file.write("i_delz="+ args.i_delz + ",            ! thickness of soil sublayers (m)\n")
    file.write("&end")
    file.write("&shufflepar\n")
    file.write("vom_command="+ args.vom_command + ",          ! COMMAND LINE TO RUN ASSIMILATION MODEL (1 for -optimise with sce, 2 for -run without optization with pars.txt, 3 for run for ncp only with pars.txt, 4 for optimise without random_seed)\n")
    file.write("i_ncomp_="+ args.i_ncomp_ + ",             ! MAXIMUM NUMBER OF COMPLEXES (p)\n")
    file.write("i_ncompmin="+ args.i_ncompmin + ",           ! MINIMUM NUMBER OF COMPLEXES (pmin)\n")
    file.write("i_resolution="+ args.i_resolution + ",       ! RESOLUTION OF OPTIMISATION (% OF MAX VARIATION WHEN OPTIMISATION STOPS)\n")
    file.write("i_patience="+ args.i_patience + ",          ! NUMBER OF LOOPS WITHOUT INCREASE IN OF BEFORE OPTIMISATION STOPS\n")
    file.write("i_nsimp="+ args.i_nsimp + ",              ! NUMBER OF OPTIMISATIONS PER COMPLEX AND RUN\n")
    file.write("i_focus="+ args.i_focus + ",            ! IF <1.0, THE SPREAD OF THE RANDOM SEED AROUND THE INITIAL VALUES IS LIMITED\n")
    file.write("i_iter="+ args.i_iter + ",              ! Maximum iterations in case of random runs\n")
    file.write("vom_npar="+ args.vom_npar + ",             ! number of parameters in shuffle2par used for optimization in SCE\n")
    file.write("n_thread="+ args.n_thread + ",             ! number of threads to be used in parallel\n")
    file.write("&end")
    file.write("&shuffle2par\n")
    file.write("parname0='lambdagf'   'wsgexp'      'lambdatf'   'wstexp'      'cai'        'rtdepth' 'mdstore' 'rgdepth' 'i_cgs'    'i_zr'   'i_go' 'i_ksat' 'i_thetar' 'i_thetas' 'i_nvg' 'i_avg'\n")
    file.write("parval0="+ args.o_lambdagf + " " + args.o_wsgexp + " " + args.o_lambdatf + " " + args.o_wstexp + " " + args.o_cai + " " + args.o_rtdepth + " " + args.o_mdstore + " " args.o_rgdepth + "" + args.i_cgs + " " + args.i_go + " " + args.i_ksat + " " + args.i_thetar + " " + args.i_thetas + " " + args.i_nvg + " " + args.i_avg + "\n" )
    file.write("parmin0="+ args.min_lambdagf + " " + args.min_wsgexp + " " + args.min_lambdatf + " " + args.min_wstexp + " " + args.min_cai + " " + args.min_rtdepth + " " + args.min_mdstore + " " + args.min_rgdepth + " " + args.min_cgs + " " + args.min_go + " " + args.min_ksat + " " + args.min_thetar + " " + args.min_thetas + " " + args.min_nvg + " " + args.min_avg + "\n")
    file.write("parmax0="+ args.max_lambdagf + " " + args.max_wsgexp + " " + args.max_lambdatf + " " + args.max_wstexp + " " + args.max_cai + " " + args.max_rtdepth + " " + args.max_mdstore + " " + args.max_rgdepth + " " + args.max_cgs + " " + args.max_go + " " + args.max_ksat + " " + args.max_thetar + " " + args.max_thetas + " " + args.max_nvg + " " + args.max_avg + "\n")
    file.write("paropt0="+ args.opt_lambdagf + " " + args.opt_wsgexp + " " + args.opt_lambdatf + " " + args.opt_wstexp + " " + args.opt_cai + " " + args.opt_rtdepth + " " + args.opt_mdstore + " " args.opt_rgdepth + " " + args.opt_cgs + " " + args.opt_go + " " + args.opt_ksat + " " + args.opt_thetar + " " + args.opt_thetas + " " + args.opt_nvg + " " + args.opt_avg + "\n" )
    file.write("&end\n")

    file.close()


    print("Script finished")

main()









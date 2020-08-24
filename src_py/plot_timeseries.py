import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date


#file to prepare timeseries plot of VOM-results
#Vegetation Optimality Model (VOM)
#written: June 2018, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    #required input
    parser.add_argument("-i", "--input", help="results_daily (can be multiple)", nargs='+')
    parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-ds", "--daystart", help="startyear for plotting", type=int, default=1)
    parser.add_argument("-de", "--dayend", help="endyear for plotting", type=int, default=31)
    parser.add_argument("-ms", "--monthstart", help="startyear for plotting", type=int, default=1)
    parser.add_argument("-me", "--monthend", help="endyear for plotting", type=int, default=12)
    parser.add_argument("-w", "--weather", help="dailyweather.prn")
    parser.add_argument("-v", "--var", help="variable in results_daily, or total assimilation (asstot) or evaporation(evaptot)", nargs='+')

    #optional input
    parser.add_argument("--i2015", help="results_daily AoB2015 ")
    parser.add_argument("--var2015", help="variable in results_daily, or total assimilation (asstot) or evaporation(evaptot), 2015 format")
    parser.add_argument("--maxmod", help="results_daily max-values ")
    parser.add_argument("--minmod", help="results_daily min-values")
    parser.add_argument("--emp1", help="empirical solution 1")
    parser.add_argument("--emp2", help="empirical solution 2")
    parser.add_argument("--eobs", help="observations evaporation")
    parser.add_argument("--eobs_qc", help="quality of observations evaporation")
    parser.add_argument("--assobs", help="observations evaporation")
    parser.add_argument("--assobs_qc", help="quality of observations evaporation")
    parser.add_argument("--pcobs", help="observations of fpar")
    parser.add_argument("--pcobsdates", help="dates of fpar")

    parser.add_argument("--stats_evap", help="statistics of evaporation timeseries", nargs='+')
    parser.add_argument("--stats_ass", help="statistics of assimilation timeseries", nargs='+')
    parser.add_argument("--stats_pc", help="statistics of projective cover timeseries", nargs='+')
    parser.add_argument("--stats_label", help="label for statistics", nargs='+')
    parser.add_argument("--moving_average", help="days for moving average",  type=int )
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [14,35] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--labelsize", help="size of labels",  type=float, default = 24 )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")
    parser.add_argument("--cblabel", help="label for colorbar", default=" ")
    parser.add_argument("--title", help="title", default=" ")
    parser.add_argument("--plot_prec", help="add precipation to figure", type=bool, default = False )
    parser.add_argument("--plot_cbar", help="add colorbar", type=bool, default = False )
    parser.add_argument("--cbar_min", help="min value for colorbar", type=float, default = 0.2)
    parser.add_argument("--cbar_max", help="max value for colorbar", type=float, default = 2.6 )
    parser.add_argument("--ymin", help="min value for y-axis", type=float, default = 1, nargs='+')
    parser.add_argument("--ymax", help="max value for y-axis", type=float, default = 1, nargs='+')
    parser.add_argument("--legend", help="show legend", type=bool, default = False )
    parser.add_argument("--palette", help="color-palette", default = 'OrRd' )
    parser.add_argument("--xloc_title", help="location x title", type=float, default = 0.01 )
    parser.add_argument("--yloc_title", help="location y title", type=float, default = 1.10 )
    parser.add_argument("--size_title", help="size of title", type=float, default = 20 )
    parser.add_argument("--locx_qctitle", help="x-location of qflag-label", type=float, default = 1.04 )
    parser.add_argument("--locy_qctitle", help="y-location of qflag-label", type=float, default = 0.92 )
    parser.add_argument("--hpad", help="h_pad tight_layout", type=float, default = 0 )
    parser.add_argument("--wpad", help="w_pad tight_layout", type=float, default = 0 )
    parser.add_argument("--fig_lab", dest="fig_lab", action='store_true', help="plot labels of subplots")
    parser.add_argument("--no_fig_lab", dest="fig_lab", action='store_false', help="do not plot labels of subplots")
    parser.add_argument("--sharex", help="share x-axis", dest="sharex", action='store_true' )
    parser.add_argument("--hourly", help="plot hourly results", dest="hourly", action='store_true' )
    parser.add_argument("--no_sharex", help="share x-axis", dest="sharex", action='store_false')
    parser.add_argument("--tight_layout", help="tight layout", dest="tight_layout", action='store_true' )
    parser.add_argument("--no_tight_layout", help="no tight layout", dest="tight_layout", action='store_false')
    parser.set_defaults(fig_lab=True, sharex = False, tight_layout=True, hourly=False)

    args = parser.parse_args()

    ##########################################
    #years to plot
    yearstart = args.yearstart
    yearend = args.yearend

    #get benchmark if defined
    if args.emp1 is not None:
        emp1 = np.genfromtxt(args.emp1, usecols=1, dtype=np.float)
    if args.emp2 is not None:
        emp2 = np.genfromtxt(args.emp2, usecols=1, dtype=np.float)
        t_emp = np.genfromtxt( args.emp2, usecols=0, dtype=np.str)
        t_emp = pd.date_range(t_emp[0], t_emp[-1], freq='D')    

    #load results
    vals = []
    ylabels = []

    tmod = []


    for i in range(0, len(args.input)):
        data_tmp = np.genfromtxt(args.input[i], names=True)

        if(args.hourly == True):

            tmod.append(np.arange(datetime(int(data_tmp["fyear"][0]),int(data_tmp["fmonth"][0]),int(data_tmp["fday"][0]),int(data_tmp["nhour"][0]-1)), 
                          datetime(int(data_tmp["fyear"][-1]),int(data_tmp["fmonth"][-1]),int(data_tmp["fday"][-1]), int(data_tmp["nhour"][-1]-1))+timedelta(hours=1), 
                          timedelta(hours=1)).astype(datetime))
        else:
            tmod.append(np.arange(datetime(int(data_tmp["fyear"][0]),int(data_tmp["fmonth"][0]),int(data_tmp["fday"][0])), 
                          datetime(int(data_tmp["fyear"][-1]),int(data_tmp["fmonth"][-1]),int(data_tmp["fday"][-1]))+timedelta(days=1), 
                          timedelta(days=1)).astype(datetime))

        data = pd.DataFrame(index=tmod[i], columns=args.var)
 

        for ivar in range(0, len(args.var)):
            var = args.var[ivar]

            if(args.hourly):
                if(var == "evaptot"):
                    data["evaptot"] = (data_tmp["etmt"] + data_tmp["etmg"] + data_tmp["esoil"])*1000.0
                    ylabels.append("ET (mm h$^{-1}$)")
                if(var == "etmt"):
                    data["etmt"] = data_tmp["etmt"]*1000.0
                    ylabels.append("E$_{perennials}$ \n (mm h$^{-1}$)")
                if(var == "etmg"):
                    data["etmg"] = data_tmp["etmg"]*1000.0
                    ylabels.append("E$_{seasonals}$ \n (mm h$^{-1}$)")
                if(var == "esoil"):
                    data["esoil"] = data_tmp["esoil"]*1000.0
                    ylabels.append("E$_{soil}$ \n (mm h$^{-1}$)")


                if(var == "par"):
                    data["par"] = data_tmp["par"] 
                    ylabels.append("PAR \n (mol m$^{-2}$ s$^{-1}$)")

                if(var == "asstot"):
                    data["asstot"] = data_tmp["asst"] + data_tmp["assg"]
                    ylabels.append('GPP \n (mol m$^{-2}$ h$^{-1}$)')
                if(var == "asst"):
                    data["asst"] = data_tmp["asst"] 
                    ylabels.append("GPP$_{perennials}$ \n (mol m$^{-2}$ d=h$^{-1}$)")
                if(var == "assg"):
                    data["assg"] = data_tmp["assg"] 
                    ylabels.append("GPP$_{seasonals}$ \n (mol m$^{-2}$ h$^{-1}$)")

                if(var == "jmax25t"):
                    data["jmax25t"] = data_tmp["jmax25t"] 
                    ylabels.append("J$_{max25,p}$ \n (mol m$^{-2}$ s$^{-1}$)")
                if(var == "jmax25g"):
                    data["jmax25g"] = data_tmp["jmax25g"] 
                    ylabels.append("J$_{max25,s}$ \n (mol m$^{-2}$ s$^{-1}$)")
                if(var == "rlt"):
                    data["rlt"] = data_tmp["rlt"] 
                    ylabels.append("Rl$_{p}$ \n (mol m$^{-2}$ h$^{-1}$)")
                if(var == "rlg"):
                    data["rlg"] = data_tmp["rlg"] 
                    ylabels.append("Rl$_{s}$ \n (mol m$^{-2}$ h$^{-1}$)")
                if(var == "rl"):
                    data["rl"] = data_tmp["rlg"]  + data_tmp["rlt"] 
                    ylabels.append("Rl \n (mol m$^{-2}$ h$^{-1}$)")


                if(var == "rrt"):
                    data["rrt"] = data_tmp["rrt"] 
                    ylabels.append("Rr$_{p}$ \n (mol m$^{-2}$ h$^{-1}$)")
                if(var == "rrg"):
                    data["rrg"] = data_tmp["rrg"] 
                    ylabels.append("Rr$_{s}$ \n (mol m$^{-2}$ h$^{-1}$)")
                if(var == "tct"):
                    data["tct"] = data_tmp["tct"] 
                    ylabels.append("Tc$_{p}$ \n (mol m$^{-2}$ h$^{-1}$)")
                if(var == "tcg"):
                    data["tcg"] = data_tmp["tcg"]
                    ylabels.append("Tc$_{s}$ \n (mol m$^{-2}$ h$^{-1}$)") 
                if(var == "cpcct_d"):
                    data["cpcct_d"] = data_tmp["cpcct_d"] 
                    ylabels.append("Rv$_{p}$ \n (mol m$^{-2}$ h$^{-1}$)") 
                if(var == "cpccg_d"):
                    data["cpccg_d"] = data_tmp["cpccg_d"] 
                    ylabels.append("Rv$_{s}$ \n (mol m$^{-2}$ h$^{-1}$)") 
                if(var == "su_avg"):
                    data["su_avg"] = data_tmp["su_avg"]
                    ylabels.append("S$_{u,avg}$ \n (-)")  
                if(var == "su_1"):
                    data["su_1"] = data_tmp["su_1"] 
                    ylabels.append("S$_{u,1}$ \n (-)")  
                if(var == "zw"):
                    data["zw"] = data_tmp["zw"]     
                    ylabels.append("Z$_{w}$ \n (m)")  
                if(var == "ws"):
                    data["ws"] = data_tmp["ws"] 
                    ylabels.append("w$_{s}$ \n (m)")  
                if(var == "spgfcf"):
                    data["spgfcf"] = data_tmp["spgfcf"] 
                    ylabels.append("Q$_{sf}$ \n (m h$^{-1}$)")  
                if(var == "infx"):
                    data["infx"] = data_tmp["infx"] 
                    ylabels.append("Q$_{iex}$ \n (m h$^{-1}$)")  
                if(var == "topt"):
                    data["topt"] = data_tmp["topt"] 
                    yylabels.append("T$_{opt}$ \n ($^{o}$C)")  
                if(var == "lambdat"):
                    data["lambdat"] = data_tmp["lambdat"] 
                    ylabels.append("$\lambda_{p}$ \n (mol mol$^{-1}$)")  
                if(var == "lambdag"):
                    data["lambdag"] = data_tmp["lambdag"] 
                    ylabels.append("$\lambda_{s}$ \n (mol mol$^{-1}$)")  
                if(var == "pc"):
                    data["pc"] = data_tmp["pc"] *100
                    ylabels.append(r"Proj. Cover (%)")  

                if(var == "ncp_t"):
                    data["ncp_t"][:] = np.nan
                    ylabels.append("NCP$_{p}$ \n (mol m$^{-2}$ h$^{-1}$)") 
                if(var == "ncp_g"):
                    data["ncp_g"][:] = np.nan
                    ylabels.append("NCP$_{s}$ \n (mol m$^{-2}$ h$^{-1}$)") 

            else:
                if(var == "evaptot"):
                    data["evaptot"] = (data_tmp["etmt"] + data_tmp["etmg"] + data_tmp["esoil"])*1000.0
                    ylabels.append("ET (mm d$^{-1}$)")
                if(var == "etmt"):
                    data["etmt"] = data_tmp["etmt"]*1000.0
                    ylabels.append("E$_{perennials}$ \n (mm d$^{-1}$)")
                if(var == "etmg"):
                    data["etmg"] = data_tmp["etmg"]*1000.0
                    ylabels.append("E$_{seasonals}$ \n (mm d$^{-1}$)")
                if(var == "esoil"):
                    data["esoil"] = data_tmp["esoil"]*1000.0
                    ylabels.append("E$_{soil}$ \n (mm d$^{-1}$)")

                if(var == "asstot"):
                    data["asstot"] = data_tmp["asst"] + data_tmp["assg"]
                    ylabels.append('GPP \n (mol m$^{-2}$ d$^{-1}$)')
                if(var == "asst"):
                    data["asst"] = data_tmp["asst"] 
                    ylabels.append("GPP$_{perennials}$ \n (mol m$^{-2}$ d$^{-1}$)")
                if(var == "assg"):
                    data["assg"] = data_tmp["assg"] 
                    ylabels.append("GPP$_{seasonals}$ \n (mol m$^{-2}$ d$^{-1}$)")

                if(var == "par"):
                    data["par"] = data_tmp["par"] 
                    ylabels.append("PAR \n (mol m$^{-2}$ d$^{-1}$)")

                if(var == "tairmax"):
                    data["tairmax"] = data_tmp["tairmax"] 
                    ylabels.append("Tmax \n (C$^{o}$)")

                if(var == "tairmin"):
                    data["tairmin"] = data_tmp["tairmin"] 
                    ylabels.append("Tmin \n (C$^{o}$)")


                if(var == "jmax25t"):
                    data["jmax25t"] = data_tmp["jmax25t"] 
                    ylabels.append("J$_{max25,p}$ \n (mol m$^{-2}$ s$^{-1}$)")
                if(var == "jmax25g"):
                    data["jmax25g"] = data_tmp["jmax25g"] 
                    ylabels.append("J$_{max25,s}$ \n (mol m$^{-2}$ s$^{-1}$)")
                if(var == "rlt"):
                    data["rlt"] = data_tmp["rlt"] 
                    ylabels.append("Rl$_{p}$ \n (mol m$^{-2}$ d$^{-1}$)")
                if(var == "rlg"):
                    data["rlg"] = data_tmp["rlg"] 
                    ylabels.append("Rl$_{s}$ \n (mol m$^{-2}$ d$^{-1}$)")
                if(var == "rl"):
                    data["rl"] = data_tmp["rlg"]  + data_tmp["rlt"] 
                    ylabels.append("Rl \n (mol m$^{-2}$ d$^{-1}$)")

                if(var == "rrt"):
                    data["rrt"] = data_tmp["rrt"] 
                    ylabels.append("Rr$_{p}$ \n (mol m$^{-2}$ d$^{-1}$)")
                if(var == "rrg"):
                    data["rrg"] = data_tmp["rrg"] 
                    ylabels.append("Rr$_{s}$ \n (mol m$^{-2}$ d$^{-1}$)")
                if(var == "tct"):
                    data["tct"] = data_tmp["tct"] 
                    ylabels.append("Tc$_{p}$ \n (mol m$^{-2}$ d$^{-1}$)")
                if(var == "tcg"):
                    data["tcg"] = data_tmp["tcg"]
                    ylabels.append("Tc$_{s}$ \n (mol m$^{-2}$ d$^{-1}$)") 
                if(var == "cpcct_d"):
                    data["cpcct_d"] = data_tmp["cpcct_d"] 
                    ylabels.append("Rv$_{p}$ \n (mol m$^{-2}$ d$^{-1}$)") 
                if(var == "cpccg_d"):
                    data["cpccg_d"] = data_tmp["cpccg_d"] 
                    ylabels.append("Rv$_{s}$ \n (mol m$^{-2}$ d$^{-1}$)") 
                if(var == "su_avg"):
                    data["su_avg"] = data_tmp["su_avg"]
                    ylabels.append("S$_{u,avg}$ \n (-)")  
                if(var == "su_1"):
                    data["su_1"] = data_tmp["su_1"] 
                    ylabels.append("S$_{u,1}$ \n (-)")  
                if(var == "zw"):
                    data["zw"] = data_tmp["zw"]     
                    ylabels.append("Z$_{w}$ \n (m)")  
                if(var == "ws"):
                    data["ws"] = data_tmp["ws"] 
                    ylabels.append("w$_{s}$ \n (m)")  
                if(var == "spgfcf"):
                    data["spgfcf"] = data_tmp["spgfcf"] *1000
                    ylabels.append("Q$_{sf}$ \n (mm d$^{-1}$)")  
                if(var == "infx"):
                    data["infx"] = data_tmp["infx"] 
                    ylabels.append("Q$_{iex}$ \n (m d$^{-1}$)")  
                if(var == "topt"):
                    data["topt"] = data_tmp["topt"] 
                    yylabels.append("T$_{opt}$ \n ($^{o}$C)")  
                if(var == "lambdat"):
                    data["lambdat"] = data_tmp["lambdat"] 
                    ylabels.append("$\lambda_{p}$ \n (mol mol$^{-1}$)")  
                if(var == "lambdag"):
                    data["lambdag"] = data_tmp["lambdag"] 
                    ylabels.append("$\lambda_{s}$ \n (mol mol$^{-1}$)")  
                if(var == "pc"):
                    data["pc"] = data_tmp["pc"] *100
                    ylabels.append(r"Proj. Cover (%)")  

                if(var == "ncp_t"):
                    data["ncp_t"] = data_tmp["ncp_t"] 
                    ylabels.append("NCP$_{p}$ \n (mol m$^{-2}$ d$^{-1}$)") 
                if(var == "ncp_g"):
                    data["ncp_g"] = data_tmp["ncp_g"] 
                    ylabels.append("NCP$_{s}$ \n (mol m$^{-2}$ d$^{-1}$)") 

            if args.moving_average is not None:
                data = data.rolling( window = args.moving_average ).mean()

        vals.append(data)


    if args.i2015 is not None:

        data_tmp = np.genfromtxt(args.i2015, names=True)

        if(args.hourly == True):
            tmod2015 = np.arange(datetime(int(data_tmp["year"][0]),int(data_tmp["month"][0]),int(data_tmp["day"][0]),int(data_tmp["hour"][0]-1)), 
                          datetime(int(data_tmp["year"][-1]),int(data_tmp["month"][-1]),int(data_tmp["day"][-1]),int(data_tmp["hour"][-1]-1))+timedelta(hours=len(data_tmp["day"]) ), 
                          timedelta(hours=1)).astype(datetime)
            date2015 = []
            for iday in range(0,len(data_tmp["day"])):
                date_tmp = datetime(int(data_tmp["year"][iday]),int(data_tmp["month"][iday]),int(data_tmp["day"][iday]), int(data_tmp["hour"][iday]-1))
                date2015.append(date_tmp)

        else:
            tmod2015 = np.arange(datetime(int(data_tmp["year"][0]),int(data_tmp["month"][0]),int(data_tmp["day"][0])), 
                          datetime(int(data_tmp["year"][-1]),int(data_tmp["month"][-1]),int(data_tmp["day"][-1]))+timedelta(days=len(data_tmp["day"]) ), 
                          timedelta(days=1)).astype(datetime)

            date2015 = []
            for iday in range(0,len(data_tmp["day"])):
                date_tmp = datetime(int(data_tmp["year"][iday]),int(data_tmp["month"][iday]),int(data_tmp["day"][iday]))
                date2015.append(date_tmp)

        data2015 = pd.DataFrame(index=date2015, columns=args.var)

        for ivar in range(0, len(args.var)):
            var = args.var[ivar]

            if(args.hourly):
                if(var == "evaptot"):
                    data2015["evaptot"] = (data_tmp["het_t"] + data_tmp["het_g"] + data_tmp["esoil"])*1000.0
                if(var == "etmt"):
                    data2015["etmt"] = data_tmp["het_t"]*1000.0
                if(var == "etmg"):
                    data2015["etmg"] = data_tmp["het_g"]*1000.0
                if(var == "esoil"):
                    data2015["esoil"] = data_tmp["esoil"]*1000.0

                if(var == "asstot"):
                    data2015["asstot"] = data_tmp["ass_t"] + data_tmp["ass_g"]
                if(var == "asst"):
                    data2015["asst"] = data_tmp["ass_t"] 
                if(var == "assg"):
                    data2015["assg"] = data_tmp["ass_g"] 

                if(var == "jmax25t"):
                    data2015["jmax25t"] = data_tmp["jmax25_t"] 
                if(var == "jmax25g"):
                    data2015["jmax25g"] = data_tmp["jmax25_g"] 
                if(var == "rlt"):
                    data2015["rlt"] = data_tmp["rl"] 
                if(var == "rlg"):
                    data2015["rlg"] = data_tmp["rl"] 

                if(var == "par"):
                    data2015["par"] = data_tmp["par"] 
                if(var == "tairmax"):
                    data2015["tairmax"] = data_tmp["tmax"] 

                if(var == "tairmin"):
                    data2015["tairmin"] = data_tmp["tmin"] 

                if(var == "rr_t"):
                    data2015["rrt"] = data_tmp["rr"] 
                if(var == "rr_g"):
                    data2015["rrg"] = data_tmp["rr"] 
                if(var == "tct"):
                    data2015["tct"][:] = np.nan  
                if(var == "tcg"):
                    data2015["tcg"][:] = np.nan
                if(var == "cpcct"):
                    data2015["cpcct"][:] = np.nan 
                if(var == "cpccg"):
                    data2015["cpccg"][:] = np.nan

                if(var == "su_avg"):
                    data2015["su_avg"][:] = np.nan 
                if(var == "su_1"):
                    data2015["su_1"] = data_tmp["su_1"] 
                if(var == "zw"):
                    data2015["zw"] = data_tmp["ys"] 
                if(var == "ws"):
                    data2015["wdata2015s"] = data_tmp["Ws"] 
                if(var == "spgfcf"):
                    data2015["spgfcf"] = data_tmp["spgfcf"] 
                if(var == "infx"):
                    data2015["infx"] = data_tmp["infx"] 
                if(var == "topt"):
                    data2015["topt"] = data_tmp["topt"] 
                if(var == "lambdat"):
                    data2015["lambdat"] = data_tmp["lambda_t"] 
                if(var == "lambdag"):
                    data2015["lambdag"] = data_tmp["lambda_g"] 
                if(var == "pc"):
                    data2015["pc"] = data_tmp["pc"] *100
        
                if(var == "ncpt"):
                    data2015["ncpt"][:] = np.nan
                if(var == "ncpg"):
                    data2015["ncpg"][:] = np.nan

            else:

                if(var == "evaptot"):
                    data2015["evaptot"] = (data_tmp["etm_t"] + data_tmp["etm_g"] + data_tmp["esoil"])*1000.0
                if(var == "etmt"):
                    data2015["etmt"] = data_tmp["etm_t"]*1000.0
                if(var == "etmg"):
                    data2015["etmg"] = data_tmp["etm_g"]*1000.0
                if(var == "esoil"):
                    data2015["esoil"] = data_tmp["esoil"]*1000.0

                if(var == "asstot"):
                    data2015["asstot"] = data_tmp["ass_t"] + data_tmp["ass_g"]
                if(var == "asst"):
                    data2015["asst"] = data_tmp["ass_t"] 
                if(var == "assg"):
                    data2015["assg"] = data_tmp["ass_g"] 


                if(var == "par"):
                    data2015["par"] = data_tmp["par"] 
                if(var == "tairmax"):
                    data2015["tairmax"] = data_tmp["tmax"] 

                if(var == "tairmin"):
                    data2015["tairmin"] = data_tmp["tmin"] 

                if(var == "jmax25t"):
                    data2015["jmax25t"] = data_tmp["jmax25_t"] 
                if(var == "jmax25g"):
                    data2015["jmax25g"] = data_tmp["jmax25_g"] 
                if(var == "rlt"):
                    data2015["rlt"] = data_tmp["rltrlg"] 
                if(var == "rlg"):
                    data2015["rlg"] = data_tmp["rltrlg"] 

                if(var == "rl"):
                    data2015["rl"] = data_tmp["rltrlg"] 

                if(var == "rr_t"):
                    data2015["rrt"] = data_tmp["rr_t"] 
                if(var == "rr_g"):
                    data2015["rrg"] = data_tmp["rr_g"] 
                if(var == "tct"):
                    data2015["tct"][:] = np.nan  
                if(var == "tcg"):
                    data2015["tcg"][:] = np.nan
                if(var == "cpcct"):
                    data2015["cpcct"][:] = np.nan 
                if(var == "cpccg"):
                    data2015["cpccg"][:] = np.nan

                if(var == "su_avg"):
                    data2015["su_avg"] = data_tmp["su_avg"] 
                if(var == "su_1"):
                    data2015["su_1"] = data_tmp["su_1"] 
                if(var == "zw"):
                    data2015["zw"] = data_tmp["ys"] 
                if(var == "ws"):
                    data2015["ws"] = data_tmp["ws"] 
                if(var == "spgfcf"):
                    data2015["spgfcf"] = data_tmp["spgfcf"] *1000
                if(var == "infx"):
                    data2015["infx"] = data_tmp["infx"] 
                if(var == "topt"):
                    data2015["topt"] = data_tmp["topt"] 
                if(var == "lambdat"):
                    data2015["lambdat"] = data_tmp["lambda_t"] 
                if(var == "lambdag"):
                    data2015["lambdag"] = data_tmp["lambda_g"] 
                if(var == "pc"):
                    data2015["pc"] = data_tmp["pc"] *100
        
                if(var == "ncpt"):
                    data2015["ncpt"][:] = np.nan
                if(var == "ncpg"):
                    data2015["ncpg"][:] = np.nan

            if args.moving_average is not None:
                data2015 = data2015.rolling( window = args.moving_average ).mean()


    #load observations
    if args.eobs is not None:
        #values observations
        eobs = (np.loadtxt(args.eobs, usecols=2) )  #mm/d
        #date/times observations
        t_eobs = np.genfromtxt(args.eobs,usecols=0, dtype=np.str )#mm/d
        t_eobs = pd.date_range(t_eobs[0], t_eobs[-1], freq='D')   

        if args.moving_average is not None:
            eobs_pd = pd.DataFrame(eobs, index=t_eobs)
            eobs_ma = eobs_pd.rolling( window = args.moving_average ).mean()

            #replace values
            eobs = eobs_ma
            t_eobs = eobs_ma.index

    if args.assobs is not None:
        #values observations
        assobs = (np.loadtxt(args.assobs, usecols=2) ) *-1.0  #mm/d
        #date/times observations
        t_assobs = np.genfromtxt(args.assobs,usecols=0, dtype=np.str )#mm/d
        t_assobs = pd.date_range(t_assobs[0], t_assobs[-1], freq='D')   

        if args.moving_average is not None:
            assobs_pd = pd.DataFrame(assobs, index=t_assobs)
            assobs_ma = assobs_pd.rolling( window = args.moving_average ).mean()

            #replace values
            assobs = assobs_ma
            t_assobs = assobs_ma.index

    #load observations
    if args.pcobs is not None:
        #values observations
        pcobs = np.genfromtxt(args.pcobs,delimiter=',', usecols=3, missing_values=-999 )
        pcobs[pcobs <= 0] = np.nan
        pcobs = 100*pcobs/0.95 #from fPar to vegetative cover
        t_pcobs = np.genfromtxt(args.pcobsdates, dtype='str', delimiter=',')
        t_pcobs = pd.to_datetime(t_pcobs[:,1], format="%Y%m")

    if args.eobs_qc is not None:
        #values observations
        eobs_qc = (np.loadtxt(args.eobs_qc, usecols=2) )  #mm/d
        #date/times observations
        teobs_qc = np.genfromtxt(args.eobs_qc,usecols=0, dtype=np.str )
        teobs_qc2 = np.genfromtxt(args.eobs_qc,usecols=1, dtype=np.str )#mm/d
        teobs_qc = pd.date_range(teobs_qc[0]+" "+teobs_qc2[0], teobs_qc[-1]+" "+teobs_qc2[-1], freq='30Min') 
        qce_pd = pd.Series(eobs_qc, index=teobs_qc)
        qce_daily = qce_pd.resample("D").mean()

    if args.assobs_qc is not None:
        #values observations
        assobs_qc = (np.loadtxt(args.assobs_qc, usecols=2) )  #mm/d
        #date/times observations
        tassobs_qc = np.genfromtxt(args.assobs_qc,usecols=0, dtype=np.str )
        tassobs_qc2 = np.genfromtxt(args.assobs_qc,usecols=1, dtype=np.str )#mm/d
        tassobs_qc = pd.date_range(tassobs_qc[0]+" "+tassobs_qc2[0], tassobs_qc[-1]+" "+tassobs_qc2[-1], freq='30Min') 
        qcass_pd = pd.Series(assobs_qc, index=tassobs_qc)
        qcass_daily = qcass_pd.resample("D").mean()

    #load statistics
    evap_stats = []
    ass_stats = []
    pc_stats = []
    if args.stats_evap is not None:
        for i in range(0, len(args.stats_evap)):
            evap_stats.append( np.genfromtxt(args.stats_evap[i] ) )

    if args.stats_ass is not None:
        for i in range(0, len(args.stats_ass)):
            ass_stats.append( np.genfromtxt(args.stats_ass[i] ) )

    if args.stats_pc is not None:
        for i in range(0, len(args.stats_pc)):
            pc_stats.append( np.genfromtxt(args.stats_pc[i] ) )

    #load weather data
    weather_data = np.genfromtxt(args.weather, names=True)
    tweather = np.arange(datetime(int(weather_data["Year"][0]),int(weather_data["Month"][0]),int(weather_data["Day"][0])), 
                  datetime(int(weather_data["Year"][-1]),int(weather_data["Month"][-1]),int(weather_data["Day"][-1]))+timedelta(days=1), 
                  timedelta(days=1)).astype(datetime)
    prec = weather_data["Rain"] #mm/d


    #######################################################################################
    #make plot

    if args.fig_lab is True:
        plot_label = [ "a)","b)","c)","d)","e)","f)", "g)", "h)" ]
    else: 
        plot_label = [ " "," "," "," "," "," ", " ", " " ]

    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    if(args.plot_cbar == True):
        if(args.sharex == True):
            fig, ax = plt.subplots(nrows=len(args.var), ncols=2, figsize=(args.figsize[0], 
                       args.figsize[1]), sharex='col', gridspec_kw={'width_ratios': [30, 1]}) 
        else:
           fig, ax = plt.subplots(nrows=len(args.var), ncols=2, figsize=(args.figsize[0], 
                       args.figsize[1]), sharex=False, gridspec_kw={'width_ratios': [30, 1]}) 
    else:
        fig, ax = plt.subplots(nrows=len(args.var), ncols=1, figsize=(args.figsize[0], 
                args.figsize[1]),squeeze=False, sharex=args.sharex) 
       
        #ax = axes.flat

    if args.palette is not None:
        palette = plt.get_cmap(args.palette, len(args.input))

    if args.colors is not None:
        colors = args.colors

    #############################
    #plot observations
    if args.eobs is not None:

        iplot = np.where(np.array(args.var) == "evaptot")[0][0]
        ax[iplot, 0].plot(t_eobs, eobs, color='blue', label='Obs.', zorder=2)

    if args.assobs is not None:
        iplot = np.where(np.array(args.var) == "asstot")[0][0]
        ax[iplot, 0].plot(t_assobs, assobs, color='blue', label='Obs.', zorder=2)

    if args.pcobs is not None:
        iplot = np.where(np.array(args.var) == "pc")[0][0]
        ax[iplot, 0].plot(t_pcobs, pcobs, color='blue', label='Obs.', zorder=2)

    #############################
    #plot observations quality flux towers
    if args.eobs_qc is not None:

        iplot = np.where(np.array(args.var) == "evaptot")[0][0]

       #add quality flag on top
        ax0twin = ax[iplot, 0].twinx()
        ax0twin.plot(qce_daily.index, -qce_daily,"--" ,color='black', label='Qflag', zorder=2)
        ax0twin.text(args.locx_qctitle, args.locy_qctitle, "Qflag (-)", ha='left', va='center', transform=ax0twin.transAxes, fontsize=16, rotation=90 )
        ax0twin.set_xlim([datetime(yearstart,args.monthstart, args.daystart), datetime( yearend, args.monthend, args.dayend)])
        
        #set labels
        #max_pre = max(prec)
        ax0twin_yticks = np.linspace(0, 100, 3)
        ax0twin_yticklabels = ["0", "50", "100"]
        ax0twin.set_yticks(-1 * ax0twin_yticks)
        ax0twin.set_yticklabels(ax0twin_yticklabels, fontsize = 14)
        for tick in ax0twin.yaxis.get_major_ticks():
            tick.label.set_fontsize(14)
        ax0twin.set_ylim( [-500, 0] )
        ax[iplot, 0].set_zorder(ax0twin.get_zorder()+1) # put ax in front of ax2

    #plot observations quality assimilation
    if args.assobs_qc is not None:

        iplot = np.where(np.array(args.var) == "asstot")[0][0]
       #add quality flag on top
        ax1twin = ax[iplot, 0].twinx()
        ax1twin.plot(qcass_daily.index, -qcass_daily,"--" ,color='black', label='Qflag', zorder=2)
        ax1twin.text(args.locx_qctitle, args.locy_qctitle, "Qflag (-)", ha='left', va='center', transform=ax1twin.transAxes, fontsize=16, rotation=90 )
        ax1twin.set_xlim([datetime(yearstart,args.monthstart, args.daystart), datetime( yearend, args.monthend, args.dayend)])
        
        #set labels
        #max_pre = max(prec)
        ax1twin_yticks = np.linspace(0, 100, 3)
        ax1twin_yticklabels = ["0", "50", "100"]
        ax1twin.set_yticks(-1 * ax1twin_yticks)
        ax1twin.set_yticklabels(ax1twin_yticklabels, fontsize = 14)
        for tick in ax1twin.yaxis.get_major_ticks():
            tick.label.set_fontsize(14)
        ax1twin.set_ylim( [-500, 0] )
        ax[iplot, 0].set_zorder(ax1twin.get_zorder()+1) # put ax in front of ax2

    #############################
    #plot observations
    if args.i2015 is not None:
        for iplot in range(0, len(args.var)):
            ax[iplot, 0].plot(data2015.index, data2015[args.var[iplot]], color='green', label='Schymanski et al. (2015)', zorder=2)

    #############################
    if(args.plot_cbar == True):

        axcbar = []
        cb = []
        norm = mpl.colors.Normalize(vmin=args.cbar_min, vmax=args.cbar_max)

        iplot = 2
        for ivar in range(0, len(args.var)):
            #axcbar.append(  ax[ivar,1]     )#fig.add_subplot( len(args.var) , 2, iplot))
            ax[ivar,1].set_xticks([])
            ax[ivar,1].set_yticks([])
            cb.append(mpl.colorbar.ColorbarBase(ax[ivar,1] ,cmap=palette,norm=norm,orientation='vertical'))
            cb[ivar].ax.tick_params(labelsize=14)
            cb[ivar].set_label(r'' + args.cblabel, labelpad=10, size=20)
            #cb[ivar].set_label(r'' + args.cblabel, labelpad=10, size=20)

            #cb[ivar].ax.set_yticks([])
            iplot = iplot + 2

    
    #############################
    #plot model results
    for iplot in range(0, len(args.var)):
        if(args.plot_cbar == True):
            for i in range(0, len(args.input)):
                    ax[iplot, 0].plot(tmod[i], vals[i][args.var[iplot]], color=palette(i), zorder=1, label="") 
        else:
            try:
                for i in range(0, len(args.input)):
                    ax[iplot, 0].plot(tmod[i], vals[i][args.var[iplot]], color=colors[i], label=args.labels[i], zorder=1)                 
            except IndexError:
                for i in range(0, len(args.input)):
                    ax[iplot, 0].plot(tmod[i], vals[i][args.var[iplot]], color=colors[i], label=str(i), zorder=1) 
             
        #set axis and ticks   
        ax[iplot, 0].set_ylabel(ylabels[iplot] , size=args.labelsize  )
        ax[iplot, 0].set_xlim([datetime(yearstart,args.monthstart, args.daystart), datetime( yearend, args.monthend, args.dayend)]) 

        for tick in ax[iplot, 0].xaxis.get_major_ticks():
            tick.label.set_fontsize(20)
            tick.label.set_rotation(90)
        for tick in ax[iplot, 0].yaxis.get_major_ticks():
            tick.label.set_fontsize(20)
        ax[iplot, 0].set_frame_on(True) 
 
        if(args.legend == True):
            ax[iplot, 0].legend(prop={'size':15}, loc='upper right')

        ax[iplot, 0].text(args.xloc_title, args.yloc_title, plot_label[iplot], ha='left', va='center', transform=ax[iplot, 0].transAxes, fontsize=args.size_title)
        ax[iplot, 0].patch.set_visible(False)

        ax[iplot, 0].set_ylim( [args.ymin[iplot], args.ymax[iplot]] )



    #add statistics
    yloc = 0.93
    if args.stats_evap is not None:
        iplot = np.where(np.array(args.var) == "evaptot")[0][0]
        for i in range(0, len(args.stats_evap)):
            ax[iplot, 0].text(0.01, yloc,  args.stats_label[i] + " = {0:.2f} mm/d".format(evap_stats[i][4])  , ha='left', va='center', transform=ax[iplot, 0].transAxes, fontsize=14, bbox=dict(boxstyle="square", alpha=0.75, color='white'  ))
            yloc = yloc - 0.12

    yloc = 0.93
    if args.stats_ass is not None:
        iplot = np.where(np.array(args.var) == "asstot")[0][0]
        for i in range(0, len(args.stats_ass)):
            ax[iplot, 0].text(0.01, yloc,  args.stats_label[i] + " = {0:.2f} mol/m$^2$/d".format(ass_stats[i][4]) , ha='left', va='center', transform=ax[iplot, 0].transAxes, fontsize=14, bbox=dict(boxstyle="square", alpha=0.75, color='white' ))
            yloc = yloc - 0.12

    yloc = 0.93
    if args.stats_pc is not None:
        iplot = np.where(np.array(args.var) == "pc")[0][0]
        for i in range(0, len(args.stats_pc)):
            ax[iplot, 0].text(0.01, yloc,  args.stats_label[i] + " = {0:.2f}%".format(pc_stats[i][4]) , ha='left', va='center', transform=ax[iplot, 0].transAxes, fontsize=14, bbox=dict(boxstyle="square", alpha=0.75, color='white' ))
            yloc = yloc - 0.12

    if(args.tight_layout == True):
        plt.tight_layout(h_pad=args.hpad, w_pad = args.wpad)

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile, bbox_inches = "tight")
    else:
        plt.show()



main()



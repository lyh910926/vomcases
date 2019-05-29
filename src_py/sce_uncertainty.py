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

    parser.add_argument("-i", "--inputfile", help="SCE_out from VOM")
    parser.add_argument("-o1", "--outputfilemax", help="outputfile maximum values")    
    parser.add_argument("-o2", "--outputfilemin", help="outputfile minimum values")    
    parser.add_argument("-w", "--workfolder", help="workfolder")    
    parser.add_argument("-d", "--dailyweather", help="dailyweather.prn")    
    parser.add_argument("-p", "--percentage", help="percentage to keep", type=np.float) 
    parser.add_argument("-op", "--optpar", help="number of parameters", type=int, nargs='+')
    parser.add_argument("-cd", "--codedir", help="directory of VOM")                          
    parser.add_argument("-c", "--code", help="code of VOM", nargs='+')                          
    args = parser.parse_args()

       
    try:
        if(len(args.optpar) != 8):
            raise ValueError
    except ValueError:
        print("Error: optpar must be of length 8")
        #exit the program
        sys.exit(1)

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
    os.system( "make --directory " + args.codedir )  

    #copy exe to workdir
    os.system( "cp " + args.codedir + "/model.x " + args.workfolder + "/model.x" )  

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

    #derive uncertainties
    #read data
    tmp = pd.read_csv( "out_tot/results_daily1", delim_whitespace=True)

    varmax = np.zeros((len(tmp['nday']), 30 ))
    varmin = np.zeros((len(tmp['nday']), 30 ))

    for k in range(4,30):

        for j in range(0,indend):
            filenum = str(j + 1)

            tmp = pd.read_csv( "out_tot/results_daily" + filenum, delim_whitespace=True)
            if j==0:
                var_out = np.zeros((indend , len(tmp[tmp.columns[k]]) ))
                var_out[j,0:len(tmp['nday'])] = tmp[tmp.columns[k]] 
            else:
                if len(tmp['nday']) != len( var_out[0,:] ):
                    print("WARNING: timeseries incomplete")
                    print("Skipping solution:" + ifile)
                    var_out[j,0:len(tmp['nday'])] = tmp[tmp.columns[k]] 
                else:
                    var_out[j,0:len(tmp['nday'])] = tmp[tmp.columns[k]] 

        #derive uncertainties
        varmax[:,k] = np.amax(var_out , 0)
        varmin[:,k] = np.amin(var_out , 0)

    varmax[:,0] = tmp[tmp.columns[0]]
    varmax[:,1] = tmp[tmp.columns[1]]
    varmax[:,2] = tmp[tmp.columns[2]]
    varmax[:,3] = tmp[tmp.columns[3]]

    varmin[:,0] = tmp[tmp.columns[0]]
    varmin[:,1] = tmp[tmp.columns[1]]
    varmin[:,2] = tmp[tmp.columns[2]]
    varmin[:,3] = tmp[tmp.columns[3]]

    os.chdir( currdir )

    print( tmp.columns.get_values() )
    print( tmp.columns.get_values()[0:29] )

    #write resultsdaily_best, resultsdaily_mean, resultsdaily_max, resultsdaily_min
    np.savetxt( args.outputfolder + "/resultsdaily_max.txt", varmax, comments='', delimiter=" ", header = ' '.join(tmp.columns.get_values()) )
    np.savetxt( args.outputfolder + "/resultsdaily_min.txt", varmin, comments='', delimiter=" ", header = ' '.join(tmp.columns.get_values()) )

    #clean up
    os.system( "rm -r " + args.workfolder + "/out")
    os.system( "rm -r " + args.workfolder + "/out_tot")
    os.system( "rm -r " + args.workfolder + "/input")
    os.system( "rm " + args.workfolder + "/model.x")

    print("finished!")

main()






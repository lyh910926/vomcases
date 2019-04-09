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
    parser.add_argument("-o", "--outputfile", help="outputfile")    
    parser.add_argument("-op", "--optpar", help="number of parameters", type=int, nargs='+')
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
    params_sorted = params[indsort,:]


    param_tmp = par_default

    shiftpar = 0
    for ipar in range(0,8):
        #print(ipar)
        if(args.optpar[ipar] == 1):
            param_tmp[ipar] = params_sorted[-1, shiftpar]
            shiftpar = shiftpar + 1

    param_tmp = np.asarray(param_tmp)
    param_tmp = param_tmp.reshape(1,len(param_tmp))

    #write pars.txt
    np.savetxt(args.outputfile, param_tmp , delimiter=" " )



    print("finished!")

main()






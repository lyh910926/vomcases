import os
import sys
import argparse
import numpy as np
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

#Create benchmarking dataset following Whitley et al. (2016) and Abramowitz et al. (2012)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i1", "--inputfile1", help="input to use with regression model")
    parser.add_argument("-i2", "--inputfile2", help="input to use with regression model")
    parser.add_argument("-i3", "--inputfile3", help="input to use with regression model")
    parser.add_argument("-ix1", "--x_regression1", help="inputfiles for x-values regression", nargs='+')
    parser.add_argument("-ix2", "--x_regression2", help="inputfiles for x-values regression", nargs='+')
    parser.add_argument("-ix3", "--x_regression3", help="inputfiles for x-values regression", nargs='+')
    parser.add_argument("-iy", "--y_regression", help="inputfiles for y-values regression", nargs='+')
    parser.add_argument("-o", "--outputfile", help="outputfile with predicted y-values")
    args = parser.parse_args()

    #########################################################################
    #simple linear regression

    #get xvalues for regression
    x1 = np.array([])
    for file in args.x_regression1:
        with open(file) as file1:
            for line in file1:
                tmp = line.split()
                x1 = np.append(x1, float(tmp[2]) )

    x2 = np.array([])
    for file in args.x_regression2:
        with open(file) as file1:
            for line in file1:
                tmp = line.split()
                x2 = np.append(x2, float(tmp[2]) )

    x3 = np.array([])
    for file in args.x_regression3:
        with open(file) as file1:
            for line in file1:
                tmp = line.split()
                x3 = np.append(x3, float(tmp[2  ]) )

    X = np.column_stack((x1,x2,x3))
    #X = np.array([x1,x2,x3])
    
    #print(X.reshape(len(x1), 3 )

    #get turbulent flux (LE or GPP)
    y = np.array([])
    for file in args.y_regression:
        with open(file) as file1:
            for line in file1:
                tmp = line.split()
                y = np.append(y, float(tmp[2]) )

    #get data to apply model flux (LE or GPP)
    x_val1 = np.array([])
    dates_val = np.array([])
    with open(args.inputfile1) as file1:
        for line in file1:
            tmp = line.split()
            x_val1 = np.append(x_val1, float(tmp[2]) )

    x_val2 = np.array([])
    dates_val = np.array([])
    with open(args.inputfile2) as file1:
        for line in file1:
            tmp = line.split()
            x_val2 = np.append(x_val2, float(tmp[2]) )

    x_val3 = np.array([])
    dates_val = np.array([])
    with open(args.inputfile3) as file1:
        for line in file1:
            tmp = line.split()
            x_val3 = np.append(x_val3, float(tmp[2]) )
            dates_val = np.append(dates_val, tmp[0] )

    Xval = np.column_stack((x_val1, x_val2, x_val3))
    #Xval = pd.DataFrame(x_val1, x_val2, x_val3)

    #simple linear regression between RS and turbulent flux (emp2)
    X = sm.add_constant(X)
    model = sm.OLS(y, X, missing='drop').fit()

    #predict
    Xval = sm.add_constant(Xval)
    y_pred = model.predict(Xval)


    print(model.summary())

    #file for output data, for comparison output
    outfile_file = open(args.outputfile, mode = 'w')

    for i in range(0, len(dates_val)):
        outfile_file.write( "%20s%30s\n" % (dates_val[i], y_pred[i] ))




 
main()

import numpy as np
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date


#file to prepare plot of VOM soil moisture - depth
#Vegetation Optimality Model (VOM)
#written: June 2019, R.C. Nijzink


def main():

    parser = argparse.ArgumentParser()

    #required input
    parser.add_argument("-i", "--input", help="su_hourly (can be multiple)", nargs='+')
    parser.add_argument("-d", "--delz", help="soil layer thickness (can be multiple, should match input)", nargs='+', type=float)
    #parser.add_argument("-ys", "--yearstart", help="startyear for plotting", type=int)
    #parser.add_argument("-ye", "--yearend", help="endyear for plotting", type=int)
    parser.add_argument("-cz", "--cz", help="average soil elevation in m", type=float)
    parser.add_argument("-nd", "--ndays", help="number of days used for averaging, starting from the last day", type=int)

    #optional input
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--mf", help="multiplication factor for unit conversion", type=float, default = 1.0)
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,5] )
    parser.add_argument("--ylim", help="ylim", nargs='+', type=float, default = [-2,2] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")
    args = parser.parse_args()

    ##########################################
    #years to plot
    #yearstart = args.yearstart
    #yearend = args.yearend


    #initialize plot
    fig=plt.figure(figsize=(args.figsize[0], args.figsize[1]), dpi= args.dpi, facecolor='w', edgecolor='k' )
    ax0  = fig.add_axes([0.10,0.10,0.75,0.85])
    #load results
    vals = []
    tmod = []

    su05 = np.zeros( (len(args.input)) )
    su25 = np.zeros( (len(args.input)) )
    su50 = np.zeros( (len(args.input)) )
    su75 = np.zeros( (len(args.input)) )
    su95 = np.zeros( (len(args.input)) )

    palette = plt.get_cmap('OrRd', len(args.input))

    for i in range(0, len(args.input)):

        #open file
        file = open(args.input[i]) #mm/d     

        nlines = 0
        for line in file: 
            nlines = nlines + 1
        file.close()

        nlayers = int(args.cz/args.delz[i])
        su = np.zeros((nlayers))
        su_data = np.zeros((nlines,nlayers))
        depth = np.zeros((nlayers))
        depth[0] = args.cz-args.delz[i]/2
        time = []
        t = 0

        #open file
        file = open(args.input[i]) #mm/d     

        #read per line as lines have different lengths
        for line in file: 
            tmp_data = line.split()
            if(len(tmp_data)>5):
                time.append(tmp_data[0:4])
                su_data[t,0:len(tmp_data[5:-1])] = np.float_(tmp_data[5:-1])
                t = t + 1
        file.close()

        for ilayer in range(1,nlayers):
            su[ilayer] = np.mean(su_data[:,ilayer])          
            depth[ilayer] = depth[ilayer - 1] - args.delz[i]

        su05[i] = su[int(0.05*nlayers)]
        su25[i] = su[int(0.25*nlayers)]
        su50[i] = su[int(0.5*nlayers)]
        su75[i] = su[int(0.75*nlayers)]
        su95[i] = su[int(0.95*nlayers)]



        #######################################################################################
        #plot model results
    ax0.plot(args.delz[1:], np.diff(su05),"o", ms=16, color="darkred", zorder=1, label = "5% depth")
    ax0.plot(args.delz[1:], np.diff(su25),"s", ms=13,color="red",  zorder=1, label = "25% depth")
    ax0.plot(args.delz[1:], np.diff(su50),"*", ms=10,color="orange", zorder=1, label = "50% depth")
    ax0.plot(args.delz[1:], np.diff(su75),"v", ms=9,color="green", zorder=1, label = "75% depth")
    ax0.plot(args.delz[1:], np.diff(su95),".", ms=8,color="black", zorder=1, label = "100% depth")
    ax0.grid(b=True, which='major', color='grey', linestyle='--')

    #set labels
    ax0.set_ylabel( args.ylabel, size=24  )
    ax0.set_xlabel( args.xlabel, size=24  )

    ax0.set_ylim( [args.ylim[0],args.ylim[1]]  )
    ax0.set_frame_on(True) # make it transparent  
    ax0.legend(prop={'size':15})



    plt.tight_layout()

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile)
    else:
        plt.show()

    print("Script finished")


main()



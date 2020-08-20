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
    parser.add_argument("-cz", "--cz", help="average soil elevation in m", nargs='+', type=float)
    parser.add_argument("-nd", "--ndays", help="number of days used for averaging, starting from the last day", type=int)

    #optional input
    parser.add_argument("--outputfile", help="outputfile")
    parser.add_argument("--mf", help="multiplication factor for unit conversion", type=float, default = 1.0)
    parser.add_argument("--labels", help="labels corresponding to input-files", nargs='+', default = ["VOM"] )
    parser.add_argument("--figsize", help="figure size", nargs='+', type=float, default = [16,5] )
    parser.add_argument("--dpi", help="dpi of figure",  type=float, default = 80 )
    parser.add_argument("--ylabel", help="ylabel" )
    parser.add_argument("--xlabel", help="xlabel", default=" ")
    parser.add_argument("--xlim", help="min-max x-axis", nargs='+',type=float, default = [0,100])
    parser.add_argument("--ylim", help="min-max y-axis", nargs='+',type=float )
    parser.add_argument("--cbar_min", help="min value for colorbar", type=float, default = 0.2)
    parser.add_argument("--cbar_max", help="max value for colorbar", type=float, default = 2.6 )
    parser.add_argument("--cblabel", help="colorbar label", default=" ")
    parser.add_argument("--plot_cbar", help="add colorbar", type=lambda x: bool(int(x)), default = False )
    parser.add_argument("--legend", help="plot legend", type=bool, default = False )
    parser.add_argument("--xloc_title", help="location x title", type=float, default = 0.01 )
    parser.add_argument("--yloc_title", help="location y title", type=float, default = 1.05 )
    parser.add_argument("--title", help="title", default=" ")
    parser.add_argument("--size_title", help="size of title", type=float, default = 20 )
    parser.add_argument("--palette", help="color-palette", default = 'OrRd' )
    parser.add_argument("--colors", help="colors corresponding to input-files", nargs='+', default = ["red"] )

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

    palette = plt.get_cmap(args.palette, len(args.input))

    for i in range(0, len(args.input)):

        #open file
        file = open(args.input[i]) #mm/d     

        nlines = 0
        for line in file: 
            nlines = nlines + 1
        file.close()

        nlayers = int(args.cz[i]/args.delz[i])
        su = np.zeros((nlayers))
        su_data = np.zeros((nlines,nlayers))
        depth = np.zeros((nlayers))
        depth[0] = 0.0-args.delz[i]/2
        time = []
        t = 0

        #open file
        file = open(args.input[i]) #mm/d     

        #read per line as lines have different lengths
        for line in file: 
            tmp_data = line.split()
            if(t>0):
                if(len(tmp_data)>5):
                    time.append(tmp_data[0:4])
                    su_data[t-1,0:len(tmp_data[5:-1])] = np.float_(tmp_data[5:-1])
                else:
                    time.append(tmp_data[0:4])
                    su_data[t-1,0:len(tmp_data[5:-1])] = 0.0
            t = t + 1
        file.close()

        for ilayer in range(1,nlayers):
            su[ilayer] = np.mean(su_data[:,ilayer])
            depth[ilayer] = depth[ilayer - 1] - args.delz[i]
            if( (ilayer > 1 ) & (su[ilayer] <= 0)):
                su[ilayer] = 1

        #######################################################################################
        #plot model results
        if(args.plot_cbar == True):
            ax0.plot(su, depth, color=palette(i), zorder=1)
        else:
            ax0.plot(su, depth, zorder=1, color=args.colors[i], label = args.labels[i])
                   
        #ax0.plot(su, depth, color='red', label=args.labels[i], zorder=1)           

    #set labels
    ax0.set_ylabel( args.ylabel, size=24  )
    ax0.set_xlabel( args.xlabel, size=24  )
    ax0.set_xlim( args.xlim  )

    ax0.set_frame_on(True) # make it transparent
    if(args.legend == True):  
        ax0.legend(prop={'size':15})


    if(args.plot_cbar == True):
        ax2  = fig.add_axes([0.90,0.10,0.03,0.85])
        norm = mpl.colors.Normalize(vmin=args.cbar_min, vmax=args.cbar_max)
        cb  = mpl.colorbar.ColorbarBase(ax2,cmap=palette,norm=norm,orientation='vertical')
        cb.ax.tick_params(labelsize=14)
        cb.set_label(args.cblabel, labelpad=10, size=20)

    for tick in ax0.yaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    for tick in ax0.xaxis.get_major_ticks():
        tick.label.set_fontsize(20)

    if args.title is not None:
        ax0.text(args.xloc_title, args.yloc_title, args.title, ha='left', va='center', transform=ax0.transAxes, fontsize=args.size_title)


    plt.tight_layout()

    #save figure
    if args.outputfile is not None:
        plt.savefig(args.outputfile)
    else:
        plt.show()




main()



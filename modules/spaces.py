import matplotlib
import matplotlib.pyplot as plt
import pylab
import ROOT
import rootplot.root2matplotlib as r2m

from math import sqrt
from math import floor
from math import ceil

from plotnames import fig_name
from plotnames import grid_name

full_plot_size = [8,6]
sml_plot_size = [4,3]

def makeSingleSpacePlot( histos, filename, ext="png" ) :
    i=0
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
        i += 1
        fig = plt.figure( figsize=[8,6] )
        xmin,xmax = hist.xedges[0], hist.xedges[-1]
        ymin,ymax = hist.yedges[0], hist.yedges[-1]
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hist.xlabel )
        axes.set_ylabel( hist.ylabel )
        hist.contour( levels = options["contours"], colors = options["colors"], linewidths = 2 )
        hist.colz()
        plt.axis( [xmin, xmax, ymin, ymax] )
        plt.clim( *options["zrange"] )
        pylab.yticks(pylab.arange( ymin, ymax+0.1, options["yticks"] ) )
        pylab.xticks(pylab.arange( xmin, xmax+0.1, options["xticks"] ) )
        axes.set_title( options["title"] )
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )

def makeGridPlots( histos, filename, ext="png" ) :
    # old code : doesnt owrk
    nplot = len( histos.keys() )
    sh = sqrt( nplot )
    fl = floor( sh )
    ce = ceil( sh )
    if sh - fl > 0.5 :
        fl = ce

    f = r2m.RootFile(filename)
    hists = [ f.get(hist) for hist in sorted(histos.keys()) ]
    opts  = [ histos[key] for key  in sorted(histos.keys()) ]

    fig = plt.figure(figsize=[ce*(sml_plot_size[0]+fl),fl*(sml_plot_size[1]+fl)])
    #fig.subplots_adjust(left=1, right=2, top=2, bottom=1)


    ax_list = []
    for h, (hist,opt) in enumerate(zip(hists,opts)) :
        ax_list.append( fig.add_subplot(ce, fl, h  ))
        ax_list[-1].set_xlabel( hist.xlabel )
        ax_list[-1].set_ylabel( hist.ylabel )
        xmin, xmax = hist.xedges[0], hist.xedges[-1]
        ymin, ymax = hist.yedges[0], hist.yedges[-1]
        plt.axis([xmin, xmax, ymin, ymax])
        hist.contour( levels=opt["contours"], colors = opt["colors"], linewidths=2 )
        hist.colz()
        plt.axis([xmin, xmax, ymin, ymax])
        plt.clim(opt["zrange"][0],opt["zrange"][1])
        pylab.yticks(pylab.arange(ymin, ymax, opt["yticks"]))
        pylab.xticks(pylab.arange(xmin, xmax, opt["xticks"]))
        ax_list[-1].set_title( opt["title"] )

    #plt.show()
    plt.savefig( grid_name( filename ) + ".%s" % ext )

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

def find_minimum_2d(hist):
    min_val = min(hist)
    x_index = -1
    y_index = -1
    for x, xvals in enumerate(hist.content):
        if min_val in xvals:
            x_index = x
            y_index = xvals.index(min_val)
    return x_index, y_index

def make_single_space_overlay( histos, filenames, ext="png" ) :
    linestyles=['solid','dotted','-.']
    i=0
    fs = [ r2m.RootFile(name) for name in filenames  ]
    for hname, options in histos.iteritems() :
        hists = [f.get(hname) for f in fs ]
        i += 1
        fig = plt.figure( figsize=[8,6] )
        xmins  =[ hist.xedges[0]  for hist in hists ] 
        ymins  =[ hist.yedges[0]  for hist in hists ]
        xmaxs  =[ hist.xedges[-1] for hist in hists ]
        ymaxs  =[ hist.yedges[-1] for hist in hists ]
        xmin, xmax, ymin, ymax = min(xmins), max(xmaxs), min(ymins), max(ymaxs)
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hists[0].xlabel )
        axes.set_ylabel( hists[0].ylabel )
        for hist, lst in zip(hists, linestyles  ):
            hist.contour( levels = options["contours"], colors = options["colors"], linewidths = 3, linestyles=lst )
            x_i, y_i = find_minimum_2d(hist)
            print x_i,y_i, hist.x[x_i] , hist.y[y_i], hist.xedges[x_i],hist.yedges[y_i]
#            plt.plot([hist.xedges[x_i],hist.yedges[y_i]],'g',markersize=10 )
            plt.plot([hist.x[x_i],hist.y[y_i]],'g' )
#            plt.plot([x_i,y_i],'g',markersize=100 )
#            plt.plot([500,1000],'g',markersize=100 )
            # FIXME: HERE WE NEED THE GREEN STARS
       
        pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
        pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
        axes.set_title( options["title"] )
        plt.savefig( fig_name( options, filenames[0] ) + ".%s" % ext )

def makeSingleSpacePlot( histos, filename, ext="png" ) :
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
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

def make_colour_contour_overlay(colour,contour,filename, ext="png"):
    f = r2m.RootFile(filename)
    for hname1, options1 in colour.iteritems() :
        pass
    for hname2, options2 in contour.iteritems() :
        pass
    hist1 = f.get(hname1)
    hist2 = f.get(hname2)
    fig = plt.figure( figsize=[8,6] )
    xmin,xmax = hist1.xedges[0], hist1.xedges[-1]
    ymin,ymax = hist1.yedges[0], hist1.yedges[-1]
    plt.axis( [xmin, xmax, ymin, ymax] )
    axes = plt.axes()
    axes.set_xlabel( hist1.xlabel )
    axes.set_ylabel( hist1.ylabel )
    hist2.contour( levels = options2["contours"], colors = options2["colors"], linewidths = 2 )
    hist1.colz()
    plt.axis( [xmin, xmax, ymin, ymax] )
    plt.clim( *options1["zrange"] )
    pylab.yticks(pylab.arange( ymin, ymax+0.1, options1["yticks"] ) )
    pylab.xticks(pylab.arange( xmin, xmax+0.1, options1["xticks"] ) )
    axes.set_title( options1["title"] )
    plt.savefig( fig_name( options1, filename ) + "_col_con.%s" % ext )

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

    fig = plt.figure(figsize=[2*(sml_plot_size[0]+1),4*(sml_plot_size[1])+1])
    #fig.subplots_adjust(left=1, right=2, top=2, bottom=1)


    ax_list = []
    for h, (hist,opt) in enumerate(zip(hists,opts)) :
        ax_list.append( fig.add_subplot(4 , 2 , h+1  ))
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

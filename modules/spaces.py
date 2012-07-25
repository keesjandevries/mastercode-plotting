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
    for y, yvals in enumerate(hist.content):
        if min_val in yvals:
            y_index = y
            x_index = yvals.index(min_val)
    return y_index, x_index

def make_single_space_overlay( histos, filenames, ext="png" ) :
    #linestyles=['solid','dotted','-.']
    linestyles=['dotted','solid','-.']
    #filling=['g','w','r']
    filling=['w','g','r']
    fs = [ r2m.RootFile(name) for name in filenames  ]
    for hname, options in histos.iteritems() :
        hists = [f.get(hname) for f in fs ]
        #fig = plt.figure( figsize=[8,6] )
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':18})
        xmins  =[ hist.xedges[0]  for hist in hists ] 
        ymins  =[ hist.yedges[0]  for hist in hists ]
        xmaxs  =[ hist.xedges[-1] for hist in hists ]
        ymaxs  =[ hist.yedges[-1] for hist in hists ]
        xmin, xmax, ymin, ymax = min(xmins), min(xmaxs), min(ymins), max(ymaxs)
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hists[0].xlabel )
        axes.set_ylabel( hists[0].ylabel )
        if options.get("xlog",None) is not None:
            axes.set_xscale('log')
        if options.get("ylog",None) is not None:
            axes.set_yscale('log')
        for hist, lst, fill in zip(hists, linestyles,filling  ): # FIXME: should first plot the dotted, then the solid contour
#            plt.clabel('') FIXME: remove ugly labels 
            cs= hist.contour( levels = options["contours"], colors = options["colors"], linewidths = 3, linestyles=lst )
            # remove the god contour labels!!!
#            for c in cs.collections:
#                paths=c.get_paths()
#                del paths[0:]
            #plt.clabel(cs,manual=True )
#            plt.Show()
            y_i, x_i = find_minimum_2d(hist)
            #xedges[x_i],hist.yedges[y_i] , x_i, y_i
            plt.plot(hist.xedges[x_i], hist.yedges[y_i],marker='*',markeredgecolor='g', color=fill ,ls='', markersize=10)
       
        if options.get('yticks',None) is not None: 
            pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
        if options.get('xticks',None) is not None: 
            pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
        axes.set_title( options["title"] )
        plt.savefig( fig_name( options, filenames[1] ) + "_overlay.%s" % ext )
#        plt.savefig("test.png" )

def makeSingleSpacePlot( histos, filename, ext="png" ) :
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
#        print hist
        #fig = plt.figure( figsize=[8,6] )
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':18})
        xmin,xmax = hist.xedges[0], hist.xedges[-1]
        ymin,ymax = hist.yedges[0], hist.yedges[-1]
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hist.xlabel )
        axes.set_ylabel( hist.ylabel )
        hist.contour( levels = options["contours"], colors = options["colors"], linewidths = 2 )
        if options.get("xlog",None) is not None:
            axes.set_xscale('log')
        if options.get("ylog",None) is not None:
            axes.set_yscale('log')
 #       plt.axis( [xmin, xmax, ymin, ymax] )
#        hist.contour( levels = options["contours"], colors = options["colors"], linewidths = 2 )
        hist.colz()
#        plt.axis( [xmin, xmax, ymin, ymax] )
        plt.clim( *options["zrange"] )
        # allow for not specifying x,ytick  
        if options.get('xticks',None) is not None: 
            pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
        if options.get('yticks',None) is not None: 
            pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
        axes.set_title( options["title"] )
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )

def make_colour_contour_overlay(colour,contour,filename, ext="png"):
    f = r2m.RootFile(filename)
    for col,cont in zip(colour,contour) :
        hname1,  hname2=col[0],  cont[0]
        options1, options2=col[1] , cont[1]
        hist1 = f.get(hname1)
        hist2 = f.get(hname2)
        #fig = plt.figure( figsize=[8,6] )
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':18})
        xmin,xmax = hist1.xedges[0], hist1.xedges[-1]
        ymin,ymax = hist1.yedges[0], hist1.yedges[-1]
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hist1.xlabel )
        axes.set_ylabel( hist1.ylabel )
        if options1.get("xlog",None) is not None:
            axes.set_xscale('log')
        if options1.get("ylog",None) is not None:
            axes.set_yscale('log')
        hist2.contour( levels = options2["contours"], colors = options2["colors"], linewidths = 2 )
        hist1.colz()
        plt.axis( [xmin, xmax, ymin, ymax] )
        plt.clim( *options1["zrange"] )
        if options1.get('xticks',None) is not None: 
            pylab.xticks(pylab.arange( xmin, xmax*1.001, options1["xticks"] ) )
        if options1.get('yticks',None) is not None: 
            pylab.yticks(pylab.arange( ymin, ymax*1.001, options1["yticks"] ) )
#        pylab.yticks(pylab.arange( ymin, ymax+0.1  , options1["yticks"] ) )
#        pylab.xticks(pylab.arange( xmin, xmax+0.1, options1["xticks"] ) )
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

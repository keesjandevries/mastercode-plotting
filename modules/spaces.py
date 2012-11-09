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
        print hname
        hists = [f.get(hname) for f in fs ]
        #fig = plt.figure( figsize=[8,6] )
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':12,'axes.labelsize':30,'xtick.labelsize':25, 'ytick.labelsize':25 })
        xmins  =[ hist.xedges[0]  for hist in hists ] 
        ymins  =[ hist.yedges[0]  for hist in hists ]
        xmaxs  =[ hist.xedges[-1] for hist in hists ]
        ymaxs  =[ hist.yedges[-1] for hist in hists ]
        xmin, xmax, ymin, ymax = min(xmins), min(xmaxs), min(ymins), max(ymaxs)
        axes = plt.axes()
        axes.set_xlabel( hists[0].xlabel )
        axes.set_ylabel( hists[0].ylabel )
        plt.axis( [xmin, xmax, ymin, ymax] )
        if options.get("xlog",None) is not None:
            axes.set_xscale('log')
        if options.get("ylog",None) is not None:
            axes.set_yscale('log')
        for hist, lst, fill in zip(hists, linestyles,filling  ): # FIXME: should first plot the dotted, then the solid contour
            cs= plt.contour( hist.x, hist.y, hist.content, levels = options["contours"], colors = options["colors"], linewidths = 3, linestyles=lst )
            y_i, x_i = find_minimum_2d(hist)
            plt.plot(hist.xedges[x_i], hist.yedges[y_i],marker='*',markeredgecolor='g', color=fill ,ls='', markersize=10)
       
        if options.get('yticks',None) is not None: 
            pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
        if options.get('xticks',None) is not None: 
            pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.2)
        plt.savefig( fig_name( options, filenames[1] ) + "_overlay.%s" % ext )

def makeSingleSpacePlot( histos, filename, ext="png" ) :
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
        cs=plt.contour( hist.x, hist.y, hist.content, levels = options["contours"], colors = options["colors"], linewidths = 2 )
        cs_sel=select_segments(cs.allsegs)
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':18})
        xmin,xmax = hist.xedges[0], hist.xedges[-1]
        ymin,ymax = hist.yedges[0], hist.yedges[-1]
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hist.xlabel )
        axes.set_ylabel( hist.ylabel )
#        hist.colz()

#        plt.colorbar(plot)
        if options.get("xlog",None) is not None:
            axes.set_xscale('log')
        if options.get("ylog",None) is not None:
            axes.set_yscale('log')
#        plt.clim( *options["zrange"] )

        # allow for not specifying x,ytick  
        if options.get('xticks',None) is not None: 
            pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
        if options.get('yticks',None) is not None: 
            pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
        if 'green_band' in options.keys():
            x_min, x_max, axis  = options['green_band']
            hv_axis={'x':'v','y':'h'}[axis]
            eval("plt.ax%sspan(%smin= x_min,%smax=x_max,color='#30c048')" % (hv_axis,axis,axis))
        plot_segments(axes,cs_sel,colors = options["colors"])
        y_i, x_i = find_minimum_2d(hist)
        plt.plot(hist.xedges[x_i], hist.yedges[y_i],marker='*',markeredgecolor='g', color='g' ,ls='', markersize=10)

        axes.set_title( options["title"] )
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )


def plot_segments(axes,cs,colors):
    from matplotlib.path import Path
    import matplotlib.patches as patches
    for i, level in enumerate(cs):
        for cont in level:
            verts=[]
            codes=[Path.MOVETO]
            for coor in cont:
                verts.append((coor[0] ,coor[1] )   )
            for vert in verts[1:]:
                codes.append(Path.LINETO)
            path = Path(verts, codes)
            patch = patches.PathPatch(path,edgecolor=colors[i], facecolor='none', lw=2)
            axes.add_patch(patch)
    
    

def make_colour_contour_overlay(colour,contour,filename, ext="png"):
    f = r2m.RootFile(filename)
    for col,cont in zip(colour,contour) :
        hname1,  hname2=col[0],  cont[0]
        options1, options2=col[1] , cont[1]
        hist1 = f.get(hname1)
        hist2 = f.get(hname2)
        #fig = plt.figure( figsize=[8,6] )
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':25,'axes.labelsize':30,'xtick.labelsize':25, 'ytick.labelsize':25 })
#        plt.rcParams.update({'font.size':18})
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
#        hist2.contour( levels = options2["contours"], colors = options2["colors"], linewidths = 2 )
        cs=plt.contour( hist2.x, hist2.y, hist2.content, levels = options2["contours"], colors = options2["colors"], linewidths = 2 )
        cs_sel=select_segments(cs.allsegs)
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
        plot_segments(axes,cs_sel,colors = options2["colors"])
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.2)
        plt.gcf().subplots_adjust(right=0.74)
        plt.savefig( fig_name( options1, filename ) + "_col_"+options2["mode"] + "_con.%s" % ext )


def select_segments(segs):
    sel_cs=[]
    for level in segs:
       sel_lev=[]
       for contour in level:
            if (len(contour)>5 and not contour_is_open(contour)) or contour_is_open(contour) :
                sel_lev.append(contour)
       sel_cs.append(sel_lev)
    return sel_cs

def contour_is_open(contour):
    a,b= contour[0], contour[-1]
    if (a[0]==b[0])and a[1]==b[1]:
        return False 
    else: 
        return True  




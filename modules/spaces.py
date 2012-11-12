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

    linestyles=['dotted','solid','-.']

    filling=['w','g','r']

    fs = [ r2m.RootFile(name) for name in filenames  ]
    for hname, options in histos.iteritems() :
        print hname
        hists = [f.get(hname) for f in fs ]

        cs_sels=[] 
        for hist, lst  in zip(hists, linestyles  ): # FIXME: should first plot the dotted, then the solid contour
            cs= plt.contour( hist.x, hist.y, hist.content, levels = options["contours"], colors = options["colors"], linewidths = 3, linestyles=lst )
            cs_sels.append(select_segments(cs.allsegs,hist,options))

        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':12,'axes.labelsize':30,'xtick.labelsize':25, 'ytick.labelsize':25 })
        axes = plt.axes()
        initialise_axes(axes,hists,options)

        for hist, cs_sel,lst, fill,name in zip(hists, cs_sels,linestyles,filling ,filenames ): 
            plot_segments(axes,cs_sel,options = options,linestyle=lst,filename=name)
            plot_minimum(hist,fill)

        plt.legend() 
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.2)
        print "Save to ", (fig_name( options, filenames[1] ) + "_overlay.%s" % ext)
        plt.savefig( fig_name( options, filenames[1] ) + "_overlay.%s" % ext )

def initialise_axes(axes,hists,options):
    # hists is a list with potentially only one element
#    try: hists[0]
#    except:TypeError , hists=[hists]
    xmins  =    [ hist.xedges[0]  for hist in hists ] 
    ymins  =    [ hist.yedges[0]  for hist in hists ]
    xmaxs  =    [ hist.xedges[-1] for hist in hists ]
    ymaxs  =    [ hist.yedges[-1] for hist in hists ]
    xmin, xmax, ymin, ymax = min(xmins), min(xmaxs), min(ymins), max(ymaxs)
    axes.set_xlabel( hists[0].xlabel )
    axes.set_ylabel( hists[0].ylabel )
    plt.axis( [xmin, xmax, ymin, ymax] )
    if options.get("xlog",None) is not None:
        axes.set_xscale('log')
    if options.get("ylog",None) is not None:
        axes.set_yscale('log')
    if options.get('yticks',None) is not None: 
        pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
    if options.get('xticks',None) is not None: 
        pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
    if options.get('title') is not None:    
        axes.set_title( options["title"] )

#def get_axis(hists):
def makeSingleSpacePlot( histos, filename, ext="png" ) :
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)

        cs=plt.contour( hist.x, hist.y, hist.content, levels = options["contours"], colors = options["colors"], linewidths = 2 )
        cs_sel=select_segments(cs.allsegs,hist,options)

        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':18})
        axes = plt.axes()
        initialise_axes(axes,[hist],options)

        if 'green_band' in options.keys():
            x_min, x_max, axis  = options['green_band']
            hv_axis={'x':'v','y':'h'}[axis]
            eval("plt.ax%sspan(%smin= x_min,%smax=x_max,color='#30c048')" % (hv_axis,axis,axis))

        plot_segments(axes,cs_sel,options= options)
        plot_minimum(hist,'g')

        print "Save to : ",(fig_name( options, filename ) + ".%s" % ext)
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )


def plot_segments(axes,cs,options,filename=None,linestyle='solid'):
    from matplotlib.path import Path
    import matplotlib.patches as patches
    from config.file_dict import file_dict
    colors=options["colors"]

#   prepare labels for the legend!!
    labels=[]
    for i, level in enumerate(cs):
        label = None
        if file_dict.get(filename):
            label = file_dict[filename]
            if options.get('labels') is not None:
                label=options["labels"][i]+label
        else:
            if options.get('labels') is not None:
                label=options['labels'][i]
        labels.append(label)

    for i, level in enumerate(cs):
        for j,cont in enumerate(level):
            verts=[]
            codes=[Path.MOVETO]
            for coor in cont:
                verts.append((coor[0] ,coor[1] )   )
            for vert in verts[1:]:
                codes.append(Path.LINETO)
            path = Path(verts, codes)
            if j ==0 :
                patch = patches.PathPatch(path,edgecolor=colors[i], facecolor='none', lw=2,linestyle=linestyle,label=labels[i])
            else:
                patch = patches.PathPatch(path,edgecolor=colors[i], facecolor='none', lw=2,linestyle=linestyle)
            axes.add_patch(patch)

def plot_minimum(hist,fill):
    y_i, x_i = find_minimum_2d(hist)
    plt.plot(hist.xedges[x_i], hist.yedges[y_i],marker='*',markeredgecolor='g', color=fill ,ls='', markersize=10)
    

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
        cs_sel=select_segments(cs.allsegs,hist2,options2)
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
        plot_segments(axes,cs_sel,options= options2)
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.2)
        plt.gcf().subplots_adjust(right=0.74)
        plt.savefig( fig_name( options1, filename ) + "_col_"+options2["mode"] + "_con.%s" % ext )


def select_segments(segs,hist,options):
    sel_cs=[]
    for level,level_z in zip(segs, options['contours']):
       sel_lev=[]
       for contour in level:
            if (len(contour)>5 and not contour_is_open(contour) and check_higher_values_exterior(contour,hist,level_z)) \
                or contour_is_open(contour) :
                sel_lev.append(contour)
       sel_cs.append(sel_lev)
    return sel_cs

def contour_is_open(contour):
    a,b= contour[0], contour[-1]
    if (a[0]==b[0])and a[1]==b[1]:
        return False 
    else: 
        return True  

def check_higher_values_exterior(contour,hist,level_z):
#    return True
#    return (check_right(contour,hist,level_z) and check_up(contour,hist,level_z) )
    return (check_right(contour,hist,level_z) and check_left(contour,hist,level_z))
#    check_up(contour,hist,level_z)

def check_up(contour,hist,level_z):
    xu,yu = get_upper_coordinates(contour)    

#    print xr, yu
    ymin=hist.yedges[0]
    ymax=hist.yedges[-1]
    nybins= float(len(hist.y))

    y_int = (ymax-ymin)/nybins

#    print x_int

    z = get_z_value(xu, yu-y_int ,hist)
    return (z< level_z) 

def check_left(contour,hist,level_z):
    xl,yl = get_farmost_left_coordinates(contour)    

#    print xl, yl
    xmin=hist.xedges[0]
    xmax=hist.xedges[-1]
    nxbins= float(len(hist.x))

    x_int = (xmax-xmin)/nxbins

    z = get_z_value(xl-x_int, yl,hist)
    return (z > level_z) 

def check_right(contour,hist,level_z):
    xr,yr = get_farmost_right_coordinates(contour)    

    #print xr, yr
    xmin=hist.xedges[0]
    xmax=hist.xedges[-1]
    nxbins= float(len(hist.x))

    x_int = (xmax-xmin)/nxbins

    z = get_z_value(xr+x_int, yr,hist)
    return (z > level_z) 

def get_farmost_left_coordinates(contour):
    xl, yl= 1.0e9, 1.0e9
    for i,point in enumerate(contour):
        if point[0] < xl:
            xl =point[0]
            yl =point[1]
    return xl, yl

def get_farmost_right_coordinates(contour):
    xr, yr= -1. , -1.
    for i,point in enumerate(contour):
        if point[0] > xr:
            xr =point[0]
            yr =point[1]
    return xr, yr

def get_upper_coordinates(contour):
    xu, yu= -1. , -1.
    for point in contour:
        if point[1] > yu:
            xu =point[0]
            yu =point[1]
    return xu, yu

def get_z_value(x,y,hist):
    nx=find_in_array(x,hist.xedges)
    ny=find_in_array(y,hist.yedges)
    z =  hist.content[ny][nx]
    return z

def find_in_array( value, array):
    n=-1
    for i, el in enumerate(array[:-1]):
        if (value > el ) and (value < array[i+1]):
            n=i
    return n

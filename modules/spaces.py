import matplotlib
import matplotlib.pyplot as plt
import pylab
import ROOT
import rootplot.root2matplotlib as r2m
from numpy import ma
import matplotlib.cm as cm

from math import sqrt
from math import floor
from math import ceil

from plotnames import fig_name
from plotnames import grid_name

from config.file_dict import file_dict

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

    linestyles=['dotted','solid','dotted']

    filling=['lightgreen','darkgreen','r']

    fs = [ r2m.RootFile(name) for name in filenames  ]
    for hname, options in histos.iteritems() :

        hists = [f.get(hname) for f in fs ]
        cs_sels=[] 

        for hist, lst  in zip(hists, linestyles  ): 
            cs= plt.contour( hist.x, hist.y, hist.content, levels = options["contours"], colors = options["colors"], linewidths = 3, linestyles=lst )
            cs_sels.append(select_segments(cs.allsegs,hist,options))

        fig, axes = initialise_axes_new(hists,options)

        for hist, cs_sel,lst, fill,name in zip(hists, cs_sels,linestyles,filling ,filenames ): 
            plot_segments(axes,cs_sel,options = options,linestyle=lst,filename=name)
            plot_minimum(hist,fill,'darkgreen')
        plot_legend(axes, options)

        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.2)

        print "Save to: ", (fig_name( options, filenames[1] ) + "_overlay.%s" % ext)
        plt.savefig( fig_name( options, filenames[1] ) + "_overlay.%s" % ext )

def initialise_axes_new(hists,options):
    fig = plt.figure( figsize=[10,7.5] )
    # FIXME: this is now assuming a fixed setup for all plot, but this could become plot type dependent.
    plt.rcParams.update({'axes.titlesize':30,'legend.fontsize':16,'axes.labelsize':35,'xtick.labelsize':25, 'ytick.labelsize':25 })
    axes = plt.axes()
    xmins  =    [ hist.xedges[0]  for hist in hists ] 
    ymins  =    [ hist.yedges[0]  for hist in hists ]
    xmaxs  =    [ hist.xedges[-1] for hist in hists ]
    ymaxs  =    [ hist.yedges[-1] for hist in hists ]
    xmin, xmax, ymin, ymax = min(xmins), min(xmaxs), min(ymins), max(ymaxs)
    axes.set_xlabel( hists[0].xlabel )
    axes.set_ylabel( hists[0].ylabel )
    plt.axis( [xmin, xmax, ymin, ymax] )
    if options.get("xlog") :
        axes.set_xscale('log')
    if options.get("ylog") :
        axes.set_yscale('log')
    if options.get('yticks') : 
        pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
    if options.get('xticks') : 
        pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
    return fig, axes

def initialise_axes(axes,hists,options,filename=None):
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
    if options.get("xlog") :
        axes.set_xscale('log')
    if options.get("ylog") :
        axes.set_yscale('log')
    if options.get('yticks') : 
        pylab.yticks(pylab.arange( ymin, ymax*1.001, options["yticks"] ) )
    if options.get('xticks') : 
        pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
    if options.get('title') :    
        if filename:
           # axes.set_title( file_dict.get(filename,{}).get('title'))
            title=file_dict.get(filename,{}).get('title')
            plt.text(0.5, 1.05, title, ha='center', fontsize=30,transform=axes.transAxes)


#def get_axis(hists):
def make_single_space_plot( histos, filename, ext="png" ) :
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        try:
            hist = f.get(hname)
        except TypeError:
            print "WARNING: skipping {} as not in ROOT file".format(hname)
            continue

        cs=plt.contour( hist.x, hist.y, hist.content, levels = options["contours"], colors = options["colors"], linewidths = 2 )
        cs_sel=select_segments(cs.allsegs,hist,options)

#        fig = plt.figure( figsize=[5,3.75] )
        fig = plt.figure( figsize=[10,7.5] )

        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.20)

#        plt.rcParams.update({ 'legend.fontsize':12})
        plt.rcParams.update({'axes.titlesize':30,'legend.fontsize':16,'axes.labelsize':30,'xtick.labelsize':25, 'ytick.labelsize':25 })
        axes = plt.axes()
        initialise_axes(axes,[hist],options,filename)

        if 'green_band' in options.keys():
            x_min, x_max, axis  = options['green_band']
            hv_axis={'x':'v','y':'h'}[axis]
            eval("plt.ax%sspan(%smin= x_min,%smax=x_max,color='#30c048')" % (hv_axis,axis,axis))

        if options.get('colz'): plot_colors(hist,options)
        plot_segments(axes,cs_sel,options= options)
        x,y =plot_minimum(hist,'gold','gold')
        plot_legend(axes, options)
        if options.get('pickle'):
            import pickle
            output = open('contours.pkl','wb')
            pickle.dump(cs_sel,output)
            out = open('bf.pkl','wb')
            pickle.dump([x,y],out)


#        add_logo(fig)
        print "Save to : ",(fig_name( options, filename ) + ".%s" % ext)
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )

def add_logo(fig):
#   FIXME: can be more automised!!!
    import matplotlib.image as mpimg
    img=mpimg.imread('mastercode.png')
#    fig.figimage(im)
    left, bottom, width, height = 0.15 , 0.75, 0.15, 0.1
    rect=[ left, bottom, width, height ]
    new_ax = fig.add_axes(rect,frame_on=False)
    new_ax.imshow(img)
    new_ax.set_xticks([])
    new_ax.set_yticks([])

def plot_colors(hist,options):

    Za=ma.array(hist.content)
    default=options.get('default',1e6)
    Zm=ma.masked_where(Za>default, Za) #FIXME: there must be a better way of doing this

    palette=plt.get_cmap(options.get('cmap','jet'))
    palette.set_bad(alpha=0.0)

    # xmin, xmax, ymin, ymax
    ext=[hist.xedges[0],hist.xedges[-1],hist.yedges[0], hist.yedges[-1]]

    # collecting arguments
    imshow_args={
            'interpolation' : 'nearest',
            'extent'        : ext,
            'aspect'        : 'auto',
            'origin'        : 'lower',
            'cmap'          : palette,
            }
    # the real function call
    plot = plt.imshow(Zm,**imshow_args)
    # also plot the bar
    plt.colorbar(plot)

    plt.clim( *options["zrange"] )

def plot_legend(axes, options):
    if options.get('legend'):
        position = options.get('lgd_position',1)
        npoints= options.get('lgd_npoints',1)

        hs, ls = axes.get_legend_handles_labels()

        #plt.legend([hs[0],hs[2],hs[1]],[ls[0],ls[2],ls[1]],loc=position,numpoints=npoints)
        plt.legend(hs,ls,loc=position,numpoints=npoints)
#        plt.legend(loc=position,numpoints=npoints) 

def plot_segments(axes,cs,options,filename=None,linestyle='solid'):
    from matplotlib.path import Path
    import matplotlib.patches as patches
    colors=options["colors"]

#   prepare labels for the legend!!
    labels=[]
    for i, level in enumerate(cs):
        label = None
        if file_dict.get(filename):
            label = file_dict[filename].get('label')
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

def plot_minimum(hist,fill,edgecolor=None):
    if edgecolor is None: edgecolor='g'
    y_i, x_i = find_minimum_2d(hist)
    plt.plot(hist.xedges[x_i], hist.yedges[y_i],marker='*',markeredgecolor=edgecolor, color=fill ,ls='', markersize=25,label=r"$\chi^2$ minimum")
    return hist.xedges[x_i], hist.yedges[y_i] 

def make_colour_contour_overlay(colour,contour,filename, ext="png"):
    f = r2m.RootFile(filename)
    for col,cont in zip(colour,contour) :
        hname1,  hname2=col[0],  cont[0]
        options1, options2=col[1] , cont[1]
        hist1 = f.get(hname1)
        hist2 = f.get(hname2)
        # get contours before initialising figure
        cs=plt.contour( hist2.x, hist2.y, hist2.content, levels = options2["contours"], colors = options2["colors"], linewidths = 2 )
        cs_sel=select_segments(cs.allsegs,hist2,options2)
        fig, axes = initialise_axes_new([hist1,hist2],options1)
        # plot colors
        plot_colors(hist1,options1)
#        hist1.colz()
#        plt.clim( *options1["zrange"] )
        # coloured plots should get a title
        if options1.get('title') :    
            axes.set_title( options1["title"] )
        # plot contours
        plot_segments(axes,cs_sel,options= options2)
        # adjust figure so that it looks nice
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.2)
        plt.gcf().subplots_adjust(right=0.74)
        #save
        print "Save to: ", fig_name( options1, filename ) + "_col_"+options2["mode"] + "_con.%s" % ext
        plt.savefig( fig_name( options1, filename ) + "_col_"+options2["mode"] + "_con.%s" % ext )


def select_segments(segs,hist,options):
    sel_cs=[]
    for level,level_z in zip(segs, options['contours']):
       sel_lev=[]
       for contour in level:
            check_contour=True
            if not contour_is_open(contour):
                if options.get("de_island") : check_contour = check_contour and check_higher_values_exterior(contour,hist,level_z)
            if options.get('minlength') : check_contour = check_contour and len(contour)>options.get('minlength')
            if check_contour:
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


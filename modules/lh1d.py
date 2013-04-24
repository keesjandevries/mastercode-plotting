import matplotlib
import pylab
import ROOT

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

import rootplot.root2matplotlib as r2m

from scipy import interpolate
from scipy.interpolate import spline

from plotnames import fig_name
from config.file_dict import file_dict

def find(f, seq):
    for i,item in enumerate(seq):
        if f(item) or i == (len(seq)-1) :
            return i

def get_xy_from_file(filename, delimiter=',', smoothing=None):
    data = np.genfromtxt(filename,delimiter=delimiter)
    x = data[:,0].tolist()
    y = data[:,1].tolist()
    if smoothing is not None:
        x_new =  np.linspace(x[0],x[-1],smoothing)
        y_smooth = spline(x,y,x_new)
        x = x_new
        y = y_smooth

    return x,y

def get_valid_segments( seq, minval, maxval ) :
    get_first = lambda val: val<maxval
    get_last  = lambda val: val>maxval
    
    segs = []
    stalactites =[]
    # find the first segment, then splice the list seq[lp+1:] and run again
    lp = 0
    fp = 0

    while fp < (len(seq)-1) and lp < (len(seq)-1) :
        fp = find( get_first, seq[lp:] ) + lp
        lp = fp + find( get_last, seq[fp:] )
        
        #FIXME: this does not provide for stalatites
        if lp-fp > 2 :
            segs.append( [fp-1,lp] )
        #segs.append( [fp-1,lp] )

        lp+=1
    if len(segs) == 0 :
        segs = [ [0,len(seq)] ]
    return segs

def get_raw_spline_from_hist(hist,options):
    
#    y, xs, patch  = hist.hist()
#    y, xs, patch  = hist.hist()
#    print y, xs
#    bin_centres=[]
#    for i, x in enumerate( xs[:-1]):
#        bin_centres.append((xs[i+1]+xs[i])/2. ) # FIXME: add log plot later
    bin_centres = hist.x
    y = hist.y
    
    y_temp=[]
    offset = options.get('offset',0)
    for y_val in y:
#            y_temp.append(y_val+1.838454)
#            y_temp.append(y_val+2.814454)
            y_temp.append(y_val+offset)

    #print bin_centres
#    return  bin_centres, y
    return  bin_centres, y_temp


def get_spline_from_hist(hist,options,smooth=1):
    x, y = get_raw_spline_from_hist(hist,options)
    ymin,ymax = options["zrange1d"]

    segs = get_valid_segments( y, ymin, ymax )
    x_final, y_final= [],[]
    for seg in segs :
 #       print y[seg[0]] , y[seg[1]],seg[0], seg[1]
        #if seg[0] (seg[1]) is not the first or the last bin, then set to the maximum value!
        if seg[0] > 0:
            y[seg[0]] = options["zrange1d"][1]
        if seg[1] < len(y)-1:
            y[seg[1]] = options["zrange1d"][1]
      #  print y[seg[0]] , y[seg[1]]

#        print x[seg[0]], x[seg[1]]
        tck = interpolate.splrep(x[seg[0]:seg[1]],y[seg[0]:seg[1]],s=smooth)
#        print tck
        xnew = np.arange(x[seg[0]],x[seg[1]],(x[seg[1]]-x[seg[0]])/200)
        ynew = interpolate.splev(xnew,tck,der=0)

#        if seg[0] > 0:
#            ynew[seg[0]] t= options["zrange1d"][1]
        if seg[1] < len(y)-1:
            ynew[-1] = options["zrange1d"][1]
#        else:
#            ynew[-1] = y[-1]


       # print ynew[seg[0]], ynew[-1]
#        else: 
#            ynew[-1]=ynew[-2]
        x_final.append(xnew)
        y_final.append(ynew)
    return x_final, y_final

def make_single_1d_overlay( histos, filenames, ext="png" ) : #FIXME: ugly, but it does the job poorly
    linestyles=['dotted','solid','-.']
    fs = [ r2m.RootFile(name) for name in filenames  ]
    for hname, options in histos.iteritems() :
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':12,'axes.labelsize':30,'xtick.labelsize':25, 'ytick.labelsize':25 })
        try:
            hists = [f.get(hname) for f in fs ]
        except ReferenceError: 
            print "ERROR: {} is not in one of the files".format(hname)
            continue
        xmins  =[ hist.xedges[0]  for hist in hists ] 
        xmaxs  =[ hist.xedges[-1] for hist in hists ]
        xmin, xmax = min(xmins), max(xmaxs)
        ymin, ymax = options["zrange1d"]

        
        r_splines=[]
        for  hist in  hists  :
            r_splines.append( get_raw_spline_from_hist(hist,options))

        fig = plt.figure( figsize=[10,7.5] )
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hist.xlabel )
        axes.set_ylabel( options.get("ytitle",None) )
        pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
        from config.file_dict import file_dict
        for rsp,lst,name in zip(r_splines,linestyles,filenames):
            (rxs,rys)  = rsp 
            plt.plot(rxs,rys,'b',linestyle=lst,linewidth=3,label=file_dict.get(name))

#        plt.legend()
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.15)

        print "Save to: ", fig_name( options, filenames[1] ) + "_overlay.%s" % ext 
        plt.savefig( fig_name( options, filenames[1] ) + "_overlay.%s" % ext )

def make_raw_smooth_overlays( r_s_histos, filename, ext="png" ) : #FIXME: ugly, but it does the job poorly
    f = r2m.RootFile(filename)
    linestyles=['dotted','solid','-.']
    for r_histo, s_histo in r_s_histos :
        r_hname,r_options=r_histo
        s_hname,s_options=s_histo
        fig = plt.figure( figsize=[10,7.5] )
        plt.rcParams.update({'font.size':25,'axes.labelsize':30 })
        try:
            r_hist,s_hist = f.get(r_hname) ,f.get(s_hname) 
        except:
            print "Failed to get {} or {} from {}".format(r_hname, s_hname, filename)
            continue
        xmin  = r_hist.xedges[0]   
        xmax  = r_hist.xedges[-1] 
        ymin, ymax = r_options["zrange1d"]

        
        r_splines=[ get_raw_spline_from_hist(r_hist,r_options), get_raw_spline_from_hist(s_hist,s_options)  ]

        fig = plt.figure( figsize=[10,7.5] )
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( r_hist.xlabel )
        axes.set_ylabel( r_options["ytitle"] )
        pylab.xticks(pylab.arange( xmin, xmax*1.001, r_options["xticks"] ) )
        for rsp,lst in zip(r_splines,linestyles):
            (rxs,rys)  = rsp 
            plt.plot(rxs,rys,'b',linestyle=lst,linewidth=1)
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.12)

        print "Saved to: ",(fig_name( r_options, filename ) + "_raw_smooth.%s" % ext)
        plt.savefig( fig_name( r_options, filename ) + "_raw_smooth.%s" % ext )


def make_single_1d_plot( histos, filename, ext="png" ) :
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
#        xmin,xmax = hist.xedges[0], hist.xedges[-1]
#        ymin,ymax = options["zrange1d"]
        rxs,rys= get_raw_spline_from_hist(hist,options)
        initialise_axes(hist,options,filename=filename)
        plt.plot(rxs,rys,'b',linestyle='solid',linewidth=3,zorder=2)
        if 'green_band' in options.keys():
            x_min, x_max  = options['green_band']
#            plt.axvspan(xmin= x_min,xmax=x_max,facecolor="#30c048", alpha = 0.4)
            plt.axvspan(xmin= x_min,xmax=x_max,color="#30c048",zorder=1)
        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.15)

        print "Save to: " , fig_name( options, filename ) + ".%s" % ext
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )

def get_band_collection(xs,ys,ymax=None):
    x_low = [x-1.5 for x in xs]
    x_high = [x+1.5 for x in xs]
    patches = []
    for i in range(len(xs)-1):
        y_1 = ys[i]
        y_2 = ys[i+1]
        x_low_1 = x_low[i]
        x_low_2 = x_low[i+1]
        x_high_1 = x_high[i]
        x_high_2 = x_high[i+1]
        if y_1 < ymax or y_2 < ymax:  
            poly_coords = [(x_low_1, y_1), (x_low_2, y_2), (x_high_2, y_2), (x_high_1, y_1)]
            patches.append(Polygon(poly_coords))

    return PatchCollection(patches,zorder=4,facecolors='#ce5e60',linewidths=1,edgecolors='#ce5e60')

def make_red_band_plot_raw( histos, filename, ext="png", data_file=None):
    f = r2m.RootFile(filename)
    xmin=85
    xmax=140
    for hname, options in histos.iteritems() :
        hist = f.get(hname)

        xs,ys=get_raw_spline_from_hist(hist,options)
        ax = initialise_axes(hist,options, xmin=xmin, xmax=xmax, xmin_offset=5)

        #draw the LEP exclusion
        if  hist.xedges[0] < 114.4:
            plt.axvspan(xmin= xmin,xmax=114.4,color="#FFFF00",zorder=0)
            plt.axvspan(xmin= 124,xmax=126,color="#00FF00",zorder=1)
            x_pos_lhc_label=0.67
#            print x_pos_lhc_label
            plt.figtext(x=0.15,y=0.2, s="LEP \nexcluded",zorder=2 )
            plt.figtext(x=x_pos_lhc_label,y=0.2, s="LHC ",zorder=2 )
        if hist.xedges[-1] > 130 or xmax > 130:
            plt.axvspan(xmin= 130,xmax=xmax,color="#DBBB88",zorder=1)
            plt.figtext(x=0.77,y=0.2, s="Theoretically\nInaccessible",zorder=2 )

        ymax = options["zrange1d"][1]
        collection = get_band_collection(xs,ys,ymax=ymax)
        ax.add_collection(collection) 

        plt.plot(xs,ys,'b',linestyle='solid',linewidth=3,zorder=5)
        model = filename.split('/')[-1].split('_')[0]
        data_file = { 'cmssm': 'cmssm_pre_lhc.csv', 'nuhm1': 'nuhm1_pre_lhc.csv' }[model]
        smoothing = { 'cmssm': 100, 'nuhm1': None }[model]

        if data_file:
            xf,yf = get_xy_from_file(filename=data_file,smoothing=smoothing)
            plt.plot(xf,yf,'b',linestyle='dashed',linewidth=3,zorder=4)

        plt.gcf().subplots_adjust(bottom=0.15)
        plt.gcf().subplots_adjust(left=0.12)

        print "Save to: ", fig_name( options, filename ) + "_raw.%s" % ext 
        plt.savefig( fig_name( options, filename ) + "_raw.%s" % ext )

#def make_red_band_plot_smooth( histos, filename, ext="png"):
#    f = r2m.RootFile(filename)
#    for hname, options in histos.iteritems() :
#        hist = f.get(hname)
#        sp =     get_spline_from_hist(hist,options,0)
#        (xnews,ynews)  = sp 
##        initialise_axes(hist,options)
#        for xnew, ynew in zip(xnews, ynews ) :
#            ys=ynew.tolist()
#            xs=xnew.tolist()
#            x_in, x_out = get_x_in_out_curve(xs,ys)
#            plt.fill_betweenx(ys,x_out, xs, facecolor="red",edgecolor='red')
#            plt.fill_betweenx(ys,xs, x_in,facecolor="red",edgecolor='red')
#            plt.plot(xs,ys,'b',linestyle='solid',linewidth=3)
#
#        print "Save to: ", fig_name( options, filename ) + "_smooth.%s" % ext 
#        plt.savefig( fig_name( options, filename ) + "_smooth.%s" % ext )

def get_x_in_out_curve(xs,ys):
    y_min_glob  = min(ys)
    x_min_glob  = xs[ys.index(min(ys))]
    x_in, x_out =[],[]
    for x in xs:
        if x < x_min_glob:
            x_in.append(min(x+1.5,x_min_glob))
            x_out.append(x-1.5)
        elif x == x_min_glob:
            x_in.append(x_min_glob)
            x_out.append(x_min_glob)
        elif x> x_min_glob:
            x_in.append(max(x-1.5,x_min_glob))
            x_out.append(x+1.5)
    return x_in, x_out

def initialise_axes(hist,options,xmin=None, xmax=None,ymin=None, ymax=None,filename=None, xmin_offset=0.):
        if xmin is None: xmin = hist.xedges[0]
        if xmax is None: xmax = hist.xedges[-1]
        if ymin is None and ymax is None:   ymin,ymax = options["zrange1d"]
        plt.figure()
#        plt.rcParams.update({'font.size':18,})
        fig = plt.figure( figsize=[10,7.5] )
#        plt.rcParams.update({'font.size':25,'axes.labelsize':30 })
        plt.rcParams.update({'axes.titlesize':30,'legend.fontsize':16,'axes.labelsize':35,'xtick.labelsize':25, 'ytick.labelsize':25 })
#        plt.rcParams.update({'font.size':25,'axes.labelsize':30 })
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( hist.xlabel )
        axes.set_ylabel( options["ytitle"] )
#        axes.set_title( "%s(%s)" % (options["title"], hist.xlabel) )
        pylab.xticks(pylab.arange( xmin+xmin_offset, xmax*1.001, options["xticks"] ) )
        pylab.yticks(pylab.arange( ymin, ymax*1.001, options.get('yticks') ) )
        if options.get('title') :    
            if filename:
            #    axes.set_title( file_dict.get(filename,{}).get('title'))
                title=file_dict.get(filename,{}).get('title')
                plt.text(0.5, 1.05, title, ha='center', fontsize=30,transform=axes.transAxes)
        return axes

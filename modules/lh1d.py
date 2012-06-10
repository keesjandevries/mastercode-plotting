import matplotlib
import matplotlib.pyplot as plt
import pylab
import ROOT
import rootplot.root2matplotlib as r2m

import numpy as np
from scipy import interpolate

from plotnames import fig_name

def find(f, seq):
    for i,item in enumerate(seq):
        if f(item) or i == (len(seq)-1) :
            return i

def get_valid_segments( seq, minval, maxval ) :
    get_first = lambda val: val<maxval
    get_last  = lambda val: val>maxval
    
    segs = []
    # find the first segment, then splice the list seq[lp+1:] and run again
    lp = 0
    fp = 0

    while fp < (len(seq)-1) and lp < (len(seq)-1) :
        fp = find( get_first, seq[lp:] ) + lp
        lp = fp + find( get_last, seq[fp:] )
        
        if lp-fp > 2 :
            segs.append( [fp-1,lp] )

        lp+=1
    if len(segs) == 0 :
        segs = [ [0,len(seq)] ]
    return segs

def make_single_1d_overlay( histos, filenames, ext="png" ) : #FIXME: ugly, but it does the job poorly
    i=0
    linestyles=['solid','dotted','-.']
    fs = [ r2m.RootFile(name) for name in filenames  ]
    for hname, options in histos.iteritems() :
        hists = [f.get(hname) for f in fs ]
        xmins  =[ hist.xedges[0]  for hist in hists ] 
        xmaxs  =[ hist.xedges[-1] for hist in hists ]
        xmin, xmax = min(xmins), max(xmaxs)
        ymin,ymax = options["zrange1d"]
        plt.figure()
        for h,lst in zip( hists, linestyles):
            y, x, patch  = h.hist()
            segs = get_valid_segments( y, ymin, ymax ) 
            for seg in segs :
                i += 1
                y[seg[0]] = options["zrange1d"][1]
                y[seg[1]] = options["zrange1d"][1]

                tck = interpolate.splrep(x[seg[0]:seg[1]],y[seg[0]:seg[1]],s=0)
                xnew = np.arange(x[seg[0]],x[seg[1]],(x[seg[1]]-x[seg[0]])/200)
                ynew = interpolate.splev(xnew,tck,der=0)
                ynew[-1] = options["zrange1d"][1]
                plt.plot(xnew,ynew,'b',linestyle=lst)
                plt.axis( [xmin, xmax, ymin, ymax] )
                axes = plt.axes()
                axes.set_xlabel( hist.xlabel )
                axes.set_ylabel( options["title"] )
                pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
                axes.set_title( "%s(%s)" % (options["title"], hist.xlabel) )
        plt.savefig( fig_name( options, filenames[0] ) + ".%s" % ext )


def makeSingle1DPlot( histos, filename, ext="png" ) :
    i=0
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
        xmin,xmax = hist.xedges[0], hist.xedges[-1]
        ymin,ymax = options["zrange1d"]
        y, x, patch  = hist.hist()
        
        segs = get_valid_segments( y, ymin, ymax )
        for seg in segs :
            i += 1
            y[seg[0]] = options["zrange1d"][1]
            y[seg[1]] = options["zrange1d"][1]

            tck = interpolate.splrep(x[seg[0]:seg[1]],y[seg[0]:seg[1]],s=0)
            xnew = np.arange(x[seg[0]],x[seg[1]],(x[seg[1]]-x[seg[0]])/200)
            ynew = interpolate.splev(xnew,tck,der=0)
            ynew[-1] = options["zrange1d"][1]
            plt.figure()
            plt.plot(xnew,ynew,'b')
            plt.axis( [xmin, xmax, ymin, ymax] )
            axes = plt.axes()
            axes.set_xlabel( hist.xlabel )
            axes.set_ylabel( options["title"] )
            pylab.xticks(pylab.arange( xmin, xmax*1.001, options["xticks"] ) )
            axes.set_title( "%s(%s)" % (options["title"], hist.xlabel) )
        plt.savefig( fig_name( options, filename ) + ".%s" % ext )

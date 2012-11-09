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
from lh1d import initialise_axes
from lh1d import get_raw_spline_from_hist


def make_grid_plot( spaces, histos, grid_size_x_y ,filename, ext="png" ) :
    print "Making grid plots:"

    sml_plot_size_x_y=[4,3]
    plt.rcParams.update({'font.size':8 })
    f = r2m.RootFile(filename)
    two_d_hists = [ f.get(two_d_hist) for two_d_hist in sorted(spaces.keys()) ]
    two_d_opts  = [ spaces[key] for key  in sorted(spaces.keys()) ]
    one_d_hists = [ f.get(one_d_hist) for one_d_hist in sorted(histos.keys()) ]
    one_d_opts  = [ histos[key] for key  in sorted(histos.keys()) ]
    fig = plt.figure(figsize=[grid_size_x_y[0]*(sml_plot_size_x_y[0]+1),grid_size_x_y[1]*(sml_plot_size_x_y[1]+1)])


    ax_list = []
    for i, (two_d_hist,two_d_opt) in enumerate(zip(two_d_hists,two_d_opts)) :
        print sorted(spaces.keys())[i]
        ax_list.append( fig.add_subplot(grid_size_x_y[1] , grid_size_x_y[0] , i+1  ))
        ax_list[-1].set_xlabel( two_d_hist.xlabel )
        ax_list[-1].set_ylabel( two_d_hist.ylabel )
        xmin, xmax = two_d_hist.xedges[0], two_d_hist.xedges[-1]
        ymin, ymax = two_d_hist.yedges[0], two_d_hist.yedges[-1]
        plt.axis([xmin, xmax, ymin, ymax])
#        two_d_hist.contour( levels=two_d_opt["contours"], colors = two_d_opt["colors"], linewidths=2 )
        two_d_hist.colz()
        plt.axis([xmin, xmax, ymin, ymax])
        plt.clim(two_d_opt["zrange"][0],two_d_opt["zrange"][1])
        pylab.yticks(pylab.arange(ymin, ymax, two_d_opt["yticks"]))
        pylab.xticks(pylab.arange(xmin, xmax, two_d_opt["xticks"]))
        ax_list[-1].set_title( two_d_opt["title"] )

    for j, (one_d_hist,one_d_opt) in enumerate(zip(one_d_hists,one_d_opts)) :
        print sorted(histos.keys())[j]
        ax_list.append( fig.add_subplot(grid_size_x_y[1] , grid_size_x_y[0] , i+j+2  ))
        rxs,rys= get_raw_spline_from_hist(one_d_hist,one_d_opt)
        xmin, xmax = one_d_hist.xedges[0], one_d_hist.xedges[-1]
        ymin,ymax = one_d_opt["zrange1d"]
        plt.axis( [xmin, xmax, ymin, ymax] )
        ax_list[-1].set_xlabel( one_d_hist.xlabel )
        ax_list[-1].set_ylabel( one_d_opt["title"] )
        ax_list[-1].set_title( "%s(%s)" % (one_d_opt["title"], one_d_hist.xlabel) )
        pylab.xticks(pylab.arange( xmin, xmax*1.001, one_d_opt["xticks"] ) )
        xmin,xmax = one_d_hist.xedges[0], one_d_hist.xedges[-1]
        ymin,ymax = one_d_opt["zrange1d"]
        plt.plot(rxs,rys,'b',linestyle='solid',linewidth=1)

    out_file_name=  grid_name( filename ) + ".%s" % ext
    print "saving to ", out_file_name
    plt.savefig( grid_name( filename ) + ".%s" % ext )

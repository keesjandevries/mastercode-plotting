import matplotlib
import matplotlib.pyplot as plt
import pylab
import ROOT
import rootplot.root2matplotlib as r2m

full_plot_size = [8,6]
sml_plot_size = [5,3]

def makeSingleSpacePlot( histos, filename ) :
    i=0
    f = r2m.RootFile(filename)
    for hname, options in histos.iteritems() :
        hist = f.get(hname)
        i += 1
        fig = plt.figure( figsize=[8,6] )
        xmin,xmax = options["xrange"]
        ymin,ymax = options["yrange"]
        plt.axis( [xmin, xmax, ymin, ymax] )
        axes = plt.axes()
        axes.set_xlabel( options["xlabel"] )
        axes.set_ylabel( options["ylabel"] )
        hist.contour( levels = options["contours"], colors = options["colors"], linewidths = 2 )
        hist.colz()
        plt.axis( [xmin, xmax, ymin, ymax] )
        plt.clim( *options["zrange"] )
        pylab.yticks(pylab.arange( ymin, ymax+0.1, options["yticks"] ) )
        pylab.xticks(pylab.arange( xmin, xmax+0.1, options["xticks"] ) )
        axes.set_title( options["title"] )
        plt.savefig("space_%d.png" % i )

def makeGridPlots( histos, filename ) :
    # old code : doesnt owrk
    f = r2m.RootFile(filename)
    hists = [ 
       f.get("data_histograms/iHist_1_2_chi2"),
       f.get("data_histograms/iHist_1_2_pval"),
       f.get("data_histograms/iHist_1_2_dchi"),
       f.get("data_histograms/iHist_1_4_chi2"),
       f.get("data_histograms/iHist_1_4_pval"),
       f.get("data_histograms/iHist_1_4_dchi"),
       f.get("data_histograms/iHist_4_2_chi2"),
       f.get("data_histograms/iHist_4_2_pval"),
       f.get("data_histograms/iHist_4_2_dchi"),
    ]

    fig = plt.figure(figsize=[16,12])

    titles = [ r"$\chi^{2}$", r"$P(\chi^{2},N_{DOF})$", r"$\Delta\chi^{2}$" ]

    # labelled by i
    mins = [ 20.0, 0.0, 0.0 ]
    maxs = [ 30.0, .20, 25. ]
    title = [ r"$\chi^{2}$", r"$P(\chi^{2},N_{DOF})$",r"$\Delta\chi^{2}$", ] 
    levels = [ [ 22.23, 25.99 ], [ 0.05, 0.10 ], [ 2.23, 5.99 ], ]
    colors = [ [ 'r', 'b' ],     [ 'r', 'b' ],   [ 'r', 'b' ], ]

    # labelled by j
    xaxis_labels= [ r"$m_{0} [GeV/c^{2}]$", r"$m_{0} [GeV/c^{2}]$", r"$\tan(\beta)$" ]
    yaxis_labels= [ r"$m_{1/2} [GeV/c^{2}]$", r"$\tan(\beta)$", r"$m_{1/2} [GeV/c^{2}]$" ]
    ranges = [ [0,1500,0,1500], [0,1500,0,60], [0,60,0,1500] ]

    ytick_steps = [ 500, 10, 500 ]
    xtick_steps = [ 500, 500, 10 ]

    ax_list = []
    for i in range(3) :
        for j in range(3) :
            ax_list.append( fig.add_subplot(3, 3, (j*3+1)+i  ))
            ax_list[-1].set_xlabel( xaxis_labels[j] )
            ax_list[-1].set_ylabel( yaxis_labels[j] )
            plt.axis(ranges[j])
            hists[i+j*3].contour( levels=levels[i], colors = colors[i], linewidths=2 )
            hists[i+j*3].colz()
            plt.axis(ranges[j])
            plt.clim(mins[i],maxs[i])
            pylab.yticks(pylab.arange(ranges[j][2], ranges[j][3]+1, ytick_steps[j]))
            pylab.xticks(pylab.arange(ranges[j][0], ranges[j][1]+1, xtick_steps[j]))


    for i in [0,3,6] :
        ax_list[i].set_title( titles[i/3] )

    #plt.show()
    plt.savefig("grid.png")

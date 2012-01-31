#! /usr/bin/env python


import matplotlib
#matplotlib.rcParams['figure.subplot.wspace'] = 0.0
#matplotlib.rcParams['figure.subplot.hspace'] = 0.0
import matplotlib.pyplot as plt
import pylab
import ROOT
import rootplot.root2matplotlib as r2m

f = r2m.RootFile("/home/hyper/Documents/mastercode_data/cmssm_test.root")

hists = [
            f.get("data_histograms/iHist_1_2_chi2"),
            f.get("data_histograms/iHist_1_2_pval"),
            f.get("data_histograms/iHist_1_2_dchi"),
        ]

fig = plt.figure(figsize=[18,5])

mins = [ 20.0, 0.0, 0.0 ]
maxs = [ 30.0, .20, 25. ]

title = [ r"$\chi^{2}$", r"$P(\chi^{2},N_{DOF})$",r"$\Delta\chi^{2}$", ] 
levels = [ [ 22.23, 25.99 ], [ 0.05, 0.10 ], [ 2.23, 5.99 ], ]
colors = [ [ 'r', 'b' ],     [ 'r', 'b' ],   [ 'r', 'b' ], ]
xaxis_label= r"$m_{0} [GeV/c^{2}]$"
yaxis_label= r"$m_{1/2} [GeV/c^{2}]$"

ax_list = []
for i in range(3) :
    ax_list.append( fig.add_subplot(1, 3, i+1 ) )
    ax_list[-1].set_xlabel( xaxis_label )
    ax_list[-1].set_ylabel( yaxis_label )
    #plt.axis([0,1000,0,1000])
    hists[i].contour( levels=levels[i], colors = colors[i], extent = (0,1500,0,1500), origin = None )
    hists[i].colz()
    plt.clim(mins[i],maxs[i])

#plt.show()
plt.savefig("test.png")

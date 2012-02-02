#! /usr/bin/env python


import matplotlib
import matplotlib.pyplot as plt
import pylab
import ROOT
import rootplot.root2matplotlib as r2m

#matplotlib.rcParams['figure.subplot.wspace'] = 0.0 # no space between subplots
#matplotlib.rcParams['figure.subplot.hspace'] = 0.0 # no space between subplots


f = r2m.RootFile("~/Documents/mastercode_data/recalc_out.root")

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
plt.savefig("test.png")

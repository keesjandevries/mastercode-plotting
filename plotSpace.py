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
            f.get("chi2_histograms/iHist_1_2_chi2"),
            f.get("chi2_histograms/iHist_1_4_chi2"),
            f.get("chi2_histograms/iHist_2_4_chi2"),
        ]

fig = plt.figure(figsize=[6,6])
for i in range(3) :
    fig.add_subplot(2, 3, i+1 )
    hists[i].colz()
    #plt.clim(20,30)
    fig.add_subplot(2, 3, i+4 )
    hists[i].contour()

plt.show()

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

fig = plt.figure(figsize=[8,5])

mins = [ 20.0, 0.0, 0.0 ]
maxs = [ 30.0, .20, 25. ]

for i in range(3) :
    fig.add_subplot(1, 3, i+1 )
    hists[i].colz()
    plt.clim(mins[i],maxs[i])

plt.show()
#plt.savefig("test.pdf")

import sys
sys.path.append( "../modules/" )
import plot_defaults as pd

histos = { 
            "data_histograms/iHist_1_2_chi2" : 
            {
                "title"  : pd.titles["chi2"]
                "xlabel" : pd.labels["m0"]
                "ylabel" : pd.labels["m12"] 
                "xrange" : [0,

  histo_list =  [ "data_histograms/iHist_1_2_chi2",
                  "data_histograms/iHist_1_2_pval",
                  "data_histograms/iHist_1_2_dchi",
                  "data_histograms/iHist_1_4_chi2",
                  "data_histograms/iHist_1_4_pval",
                  "data_histograms/iHist_1_4_dchi",
                  "data_histograms/iHist_4_2_chi2",
                  "data_histograms/iHist_4_2_pval",
                  "data_histograms/iHist_4_2_dchi"]

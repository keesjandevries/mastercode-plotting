from defaults.default_plots import getDefaults as pds

histos = { 
            "data_histograms/iHist_1_2_chi2" : pds("m0",  "m12", "chi2"),
            "data_histograms/iHist_1_2_pval" : pds("m0",  "m12", "pval"),
            "data_histograms/iHist_1_2_dchi" : pds("m0",  "m12", "dchi"),
            "data_histograms/iHist_1_4_chi2" : pds("m0",  "tanb","chi2"),
            "data_histograms/iHist_1_4_pval" : pds("m0",  "tanb","pval"),
            "data_histograms/iHist_1_4_dchi" : pds("m0",  "tanb","dchi"),
            "data_histograms/iHist_4_2_chi2" : pds("tanb","m12", "chi2"),
            "data_histograms/iHist_4_2_pval" : pds("tanb","m12", "pval"),
            "data_histograms/iHist_4_2_dchi" : pds("tanb","m12", "dchi"),
         }

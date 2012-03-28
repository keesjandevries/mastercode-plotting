#! /usr/bin/env python

titles = { "chi2": r"$\chi^{2}$", 
           "pval": r"$P(\chi^{2},N_{DOF})$", 
           "dchi": r"$\Delta\chi^{2}$" 
         }

labels = { "m0"   : r"$m_{0} [GeV/c^{2}]$",
           "m12"  : r"$m_{1/2} [GeV/c^{2}]$", 
           "tanb" : r"$\tan(\beta)$",
         }

clevels = { "dchi" : [2.23,5.99],
            "pval" : [0.05,0.10],
          }

def cLevelDelta( delta = 0.0 ) :
    return [ x+delta for x in clevels["dchi"] ] 

#! /usr/bin/env python

titles = { "chi2": r"$\chi^{2}$", 
           "pval": r"$P(\chi^{2},N_{DOF})$", 
           "dchi": r"$\Delta\chi^{2}$" 
         }

labels = { "m0"   : r"$m_{0} [GeV/c^{2}]$",
           "m12"  : r"$m_{1/2} [GeV/c^{2}]$", 
           "tanb" : r"$\tan(\beta)$",
         }

ranges = { "m0"   : [0, 2500],
           "m12"  : [0, 2500],
           "tanb" : [0, 60],
           "m0small"  : [0, 1500],
           "m12small" : [0, 1500],
         }

ticks = { "m0"   : 500,
          "m12"  : 500,
          "tanb" : 10,
        }

colors = [ 'r', 'b' ]

zrange = { "pval" :  [0., 0.2],
           "dchi" :  [0., 20.],
           "chi2" :  [20., 45.],
         }

clevels = { "dchi" : [2.23,5.99],
            "pval" : [0.05,0.10],
          }

def cLevelDelta( delta = 0.0 ) :
    return [ x+delta for x in clevels["dchi"] ] 

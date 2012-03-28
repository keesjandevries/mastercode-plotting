import plotting_defaults as pd

def getDefaults( xaxis, yaxis, mode ) :
    return eval("dict(%s%sBase.items() + %sBase.items())" % ( xaxis, yaxis, mode ) )

m0m12Base = {
                "xlabel"   : pd.labels["m0"],
                "ylabel"   : pd.labels["m12"],
                "xrange"   : pd.ranges["m0small"],
                "yrange"   : pd.ranges["m12small"] ,
                "xticks"   : pd.ticks["m0"],
                "yticks"   : pd.ticks["m12"],
            }

m0tanbBase = {
                "xlabel"   : pd.labels["m0"],
                "ylabel"   : pd.labels["tanb"],
                "xrange"   : pd.ranges["m0small"],
                "yrange"   : pd.ranges["tanb"] ,
                "xticks"   : pd.ticks["m0"],
                "yticks"   : pd.ticks["tanb"],
             }

tanbm12Base = {
                "xlabel"   : pd.labels["tanb"],
                "ylabel"   : pd.labels["m12"],
                "xrange"   : pd.ranges["tanb"],
                "yrange"   : pd.ranges["m12small"] ,
                "xticks"   : pd.ticks["tanb"],
                "yticks"   : pd.ticks["m12"],
              }


# lots of replications : need sto be done more intelligently
chi2Base = {
                "title"    : pd.titles["chi2"],
                "contours" : pd.cLevelDelta(20.),
                "colors"   : pd.colors,
                "zrange"   : pd.zrange["chi2"]
           }

pvalBase = {
                "title"    : pd.titles["pval"],
                "contours" : pd.clevels["pval"],
                "colors"   : pd.colors,
                "zrange"   : pd.zrange["pval"]
           }

dchiBase = {
                "title"    : pd.titles["dchi"],
                "contours" : pd.clevels["dchi"],
                "colors"   : pd.colors,
                "zrange"   : pd.zrange["dchi"]
           }

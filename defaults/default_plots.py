import plotting_defaults as pd

def getDefaults( mode, *axes ) :
    axes_format = "%s"*len(axes)
    format_string = "dict(" + axes_format + "Base.items() +%sBase.items())"
    return eval( format_string % tuple( list(axes) + [mode] ) )

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

neu1Base = {
             "xlabel" : pd.labels["neu1"],
             "xrange" : pd.ranges["neu1"],
             "xticks" : pd.ticks["neu1"],
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
                "zrange"   : pd.zrange["dchi"],
                "zrange1d" : pd.zrange["dchi1d"]
           }

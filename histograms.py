import ROOT as r
import MCchain as MCC
import plot_options as po
from collections import defaultdict

# not sure how many import levels is efficient in python
def get_hist_dict( d ) :
    hd = defaultdict(list)
    for rfile in d.keys() :
        hnames = []
        for rdir in d[rfile].keys() :
            for hname in d[rfile][rdir] :
                hnames.append( "%s/%s" % ( rdir, hname ) )
        f = r.TFile.Open( rfile )
        r.gROOT.cd()
        for hn in hnames :
            hd[rfile].append( f.Get( hn ).Clone() )
        f.Close()
    return hd


def get_filled_hists( hdict, tree_props ) :
    p_hists = []
    for rfile in hdict.keys() :
        chain = MCC.MCchain( rfile, tree_props["Chi2TreeName"],
            tree_props["ContribTreeName"], tree_props["Chi2BranchName"],
            tree_props["ContribBranchName"] )
        nentries = chain.GetEntries()
        for h in hdict[rfile] :
            nbinsx = h.GetNbinsX()
            xmax = h.GetXaxis().GetXmax()
            xmin = h.GetXaxis().GetXmin()
            xbins = h.GetXaxis().GetXbins().GetArray()

            nbinsy = h.GetNbinsY()
            ymax = h.GetYaxis().GetXmax()
            ymin = h.GetYaxis().GetXmin()
            ybins = h.GetYaxis().GetXbins().GetArray()

            # basically our histogram isn't getting fully described
            # it means we have to get:
            #   - binning from original histogram
            #   - can be done with the xbins and ybins arrays above but there's
            #   a buffer indexing error

            print "[ %f, %f ] :: [ %f, %f ]" % ( xmin, xmax, ymin, ymax )
            
            title = "%s;%s;%s" % ( h.GetTitle(), h.GetXaxis().GetTitle(),
            h.GetYaxis().GetTitle() )

            p_hists.append( r.TH2D( h.GetName() + "_chi2", title, nbinsx,
                xmin, xmax, nbinsy, ymin, ymax ) )

            nbins = nbinsx * nbinsy
            po.set_hist_properties( p_hists[-1] )

            for i in range( 0, nbins+1 ) :
                entry = int( h.GetBinContent(i) )
                content = -1
                if entry > 0 :
                    chain.GetEntry(entry)
                    content = chain.chi2vars[0]
                p_hists[-1].SetBinContent( i, content )
    return p_hists

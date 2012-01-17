#! /usr/bin/env python

import ROOT as r
from array import array

class MCchain( object ) :
    def __init__( self, fname, chi2name = "chi2tree" , \
        contribname = "contribtree", branch_name = "vars",
        contrib_branch_name = "vars" ) :
        self.tree_name = chi2name
        self.contrib_name = contribname
        self.chi2_state, self.contrib_state =  self.check_file( fname )
        self.init_chains(fname)
        self.setup_branches(branch_name,contrib_branch_name)

    def add_file( self, fname ) :
        c2s, cbs = self.check_file( fname )
        self.chi2_state    = self.chi2_state    and cbs
        self.contrib_state = self.contrib_state and c2s

        if self.chi2_state:
            self.chi2chain.Add(fname)
        if self.contrib_state :
            self.contribchain.Add(fname)

        self.nentries = self.chi2chain.GetEntries()

    def Add( self, l ) :
        for f in l :
            self.add_file(f)

    def init_chains( self, fname) :
        if self.chi2_state :
            self.chi2chain = r.TChain(self.tree_name)    
            self.chi2chain.Add(fname)
            self.chi2chain.SetCacheSize(0)
            if self.contrib_state :
                self.contribchain = r.TChain(self.contrib_name)
                self.contribchain.Add(fname)
                self.contribchain.SetCacheSize(0)

    def setup_branches( self, branch_name, contrib_branch_name ) :
        self.nentries = self.chi2chain.GetEntries()
        if self.contrib_state :
            self.chi2chain.AddFriend(self.contribchain)
        self.nTotVars = self.chi2chain.GetLeaf(branch_name).GetLen()
        self.chi2vars = array('d',[0]*self.nTotVars)
        self.chi2chain.SetBranchAddress(branch_name,self.chi2vars)
        if self.contrib_state :
            self.contribvars = array('d',[0]*self.nTotVars)
            self.contribchain.SetBranchAddress(contrib_branch_name,self.contribvars)

    def check_file( self, fname ) :
        tf = r.TFile(fname)

        chi2tree  = tf.Get(self.tree_name)
        conttree  = tf.Get(self.contrib_name)

        contrib_state = conttree  is not None
        chi2_state    = chi2tree  is not None

        return chi2_state,contrib_state

    def GetEntry( self, entry ) :
        read = 0
        if self.chi2_state :
            read = self.chi2chain.GetEntry(entry)
        else :
            print "No main tree available to source entries"
        return read

    def GetEntries( self ) :
        n_entries = -1
        if self.chi2_state :
            n_entries = self.chi2chain.GetEntries()
        else :
            "No valid entries"
        return n_entries

    def GetBranchLength( self ) :
        return self.nTotVars

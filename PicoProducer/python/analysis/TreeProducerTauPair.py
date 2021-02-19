# Author: Izaak Neutelings (June 2020)
# Description: Produce generic tree for tau analysis
# Sources:
#   https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Synchronisation
#   https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
from ROOT import TH1D
from TreeProducer import TreeProducer


class TreeProducerTauPair(TreeProducer):
  
  def __init__(self, filename, module, **kwargs):
    """Class to create and prepare a custom output file & tree."""
    super(TreeProducerTauPair,self).__init__(filename,module,**kwargs)
    #print "Loading TreeProducerTauPair for %r"%(filename)
    
    
    #############
    #   EVENT   #
    #############
    
    self.addBranch('run',                 'i')
    self.addBranch('lumi',                'i')
    self.addBranch('evt',                 'i')
    self.addBranch('data',                '?', module.isdata)
    
    self.addBranch('npv',                 'i', title="number of offline primary vertices")
    self.addBranch('npv_good',            'i')
    self.addBranch('rho',                 'f', title="fixedGridRhoFastjetAll")
    self.addBranch('metfilter',           '?', title="recommended metfilters")
    
    if module.ismc:
      # https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/plugins/NPUTablesProducer.cc
      self.addBranch('npu',               'i', -1, title="number of in-time pu interactions added (getPU_NumInteractions -> nPU)")
      self.addBranch('npu_true',          'i', -1, title="true mean number of Poisson distribution (getTrueNumInteractions -> nTrueInt)")
      self.addBranch('NUP',               'i', -1, title="number of partons for stitching (LHE_Njets)")
    
    
    ##############
    #   WEIGHT   #
    ##############
    
    if module.ismc:
      self.addBranch('weight',            'f', 1., title="weight combining others (to reduce selection string length)")
      self.addBranch('genweight',         'f', 1.)
      self.addBranch('trigweight',        'f', 1.)
      if not module.dotight:
        self.addBranch('trigweightUp',    'f', 1.)
        self.addBranch('trigweightDown',  'f', 1.)
      self.addBranch('puweight',          'f', 1., title="pileup up reweighting")
      self.addBranch('zptweight',         'f', 1., title="Z pT reweighting")
      self.addBranch('ttptweight',        'f', 1., title="top pT reweighting")
      self.addBranch('btagweight',        'f', 1.)
      self.addBranch('prefireweight',     'f', 1.)
      self.addBranch('prefireweightUp',   'f', 1.)
      self.addBranch('prefireweightDown', 'f', 1.)
    elif module.isembed:
      self.addBranch('genweight',         'f', 1.)
      self.addBranch('trackweight',       'f', 1.)
    
    
    ############
    #   JETS   #
    ############
    
    self.addBranch('njets',               'i', title="number of jets (pT > 30 GeV, |eta| < 4.7)")
    self.addBranch('njets50',             'i', title="number of jets (pT > 50 GeV, |eta| < 4.7)")
    self.addBranch('ncjets',              'i', title="number of central jets (|eta| < 2.4)")
    self.addBranch('nfjets',              'i', title="number of forward jets (2.4 < |eta| < 4.7)")
    self.addBranch('nbtag',               'i', title="number of b tagged jets (pT > 30 GeV, |eta| < 2.7)")
    
    self.addBranch('jpt_1',               'f', title="pT of leading jet")
    self.addBranch('jeta_1',              'f', title="eta of leading jet")
    self.addBranch('jphi_1',              'f', title="phi of leading jet")
    self.addBranch('jdeepb_1',            'f', title="DeepCVS score of leading jet")
    self.addBranch('jpt_2',               'f', title="pT of subleading jet")
    self.addBranch('jeta_2',              'f', title="eta of subleading jet")
    self.addBranch('jphi_2',              'f', title="phi of subleading jet")
    self.addBranch('jdeepb_2',            'f', title="DeepCVS score of subleading jet")
    
    self.addBranch('bpt_1',               'f', title="pT of leading b jet")
    self.addBranch('beta_1',              'f', title="eta of leading jet")
    self.addBranch('bpt_2',               'f', title="pT of leading jet")
    self.addBranch('beta_2',              'f', title="eta of leading jet")
    
    self.addBranch('met',                 'f')
    self.addBranch('metphi',              'f')
    
    if module.ismc:
      self.addBranch('genmet',            'f', -1)
      self.addBranch('genmetphi',         'f', -9)
    
    
    #############
    #   OTHER   #
    #############
    
    self.addBranch('mt_1',                'f', title="PF transverse mass with first lepton")
    self.addBranch('mt_2',                'f', title="PF transverse mass with second lepton")
    self.addBranch('m_vis',               'f', title="invariant mass of visibile ditau system")
    self.addBranch('pt_ll',               'f', title="pT of visibile ditau system")
    self.addBranch('dR_ll',               'f', title="DeltaR of visibile ditau system")
    self.addBranch('dphi_ll',             'f', title="DeltaPhi of visibile ditau system")
    self.addBranch('deta_ll',             'f', title="DeltaEta of visibile ditau system")
    self.tree.SetAlias("m_ll","m_vis")
    self.tree.SetAlias("mvis","m_vis")
    
    self.addBranch('pzetavis',            'f', title="projection of visible ditau momentums onto bisector (zeta)")
    self.addBranch('pzetamiss',           'f', title="projection of MET onto zeta axis")
    self.addBranch('dzeta',               'f', title="pzetamiss-0.85*pzetavis")
    self.addBranch('chi',                 'f', title="exp|y_2-y_1|")
    
    self.addBranch('dilepton_veto',       '?')
    self.addBranch('extraelec_veto',      '?')
    self.addBranch('extramuon_veto',      '?')
    self.addBranch('lepton_vetoes',       '?')
    self.addBranch('lepton_vetoes_notau', '?')
    
    if module.ismc:
      self.addBranch('m_moth',            'f', -1, title="generator mother mass (Z boson, W boson, top quark, ...)")
      self.addBranch('pt_moth',           'f', -1, title="generator mother pT (Z boson, W boson, top quark, ...)")
    


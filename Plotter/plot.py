#! /usr/bin/env python
# Author: Izaak Neutelings (August 2020)
# Description: Simple plotting script for pico analysis tuples
#   ./plot.py -c mutau -y 2018
from config.samples import *
from TauFW.Plotter.plot.utils import LOG as PLOG


def plot(sampleset,channel,parallel=True,tag="",outdir="plots",era="",pdf=False):
  """Test plotting of SampleSet class for data/MC comparison."""
  LOG.header("plot")
  
  # SELECTIONS
  #baseline  = "q_1*q_2<0 && iso_1<0.15 && idDecayModeNewDMs_2 && idDeepTau2017v2p1VSjet_2>=16 && idDeepTau2017v2p1VSe_2>=2 && idDeepTau2017v2p1VSmu_2>=8 && !lepton_vetoes_notau &&metfilter"
  #zttregion = "%s && mt_1<60 && dzeta>-25 && abs(deta_ll)<1.5"%(baseline)

  inclusive = "(q_1*q_2<0)"
  inclusive_cr_qcd = inclusive.replace("q_1*q_2<0","q_1*q_2>0") # inverting the opposite-sign requirement of the mutau pair into a same-sign requirment                             
  #general_cuts = "(iso_1<0.1)&&(pt_1>26.0)&&(pt_2>20.0)&&(eta_1>-2.1)&&(eta_1<2.1)&&(eta_2>-2.3)&&(eta_2<2.3)&&!lepton_vetoes_notau&&metfilter"                                    
  #general_cuts='iso_1<0.1 && pt_1>26.0 && pt_2>20.0 && abs(eta_1)<2.1 && abs(eta_2)<2.3 && idDecayModeNewDMs_2 && idDeepTau2017v2p1VSjet_2>=16 && idDeepTau2017v2p1VSe_2>=1&&idDeepTau2017v2p1VSmu_2>=1  && q_1*q_2<0 && !lepton_vetoes_notau && metfilter'
  general_cuts='q_1*q_2<0 && iso_1<0.1 && pt_1>26.0 && pt_2>20.0 && abs(eta_1)<2.1 && abs(eta_2)<2.3 && idDecayModeNewDMs_2 && idDeepTau2017v2p1VSjet_2>=16 &&idDeepTau2017v2p1VSmu_2>=1 && !lepton_vetoes_notau && metfilter'

  mvis_cuts1 = "(m_vis>60) && (m_vis < 120) && (mt_2 < 60) && (idDeepTau2017v2p1VSe_2 >= 16 )"
  mvis_cuts2 = "(m_vis>60) && (m_vis < 120) && (mt_2 < 60) && (idDeepTau2017v2p1VSe_2 >= 32 )" 
  mvis_cuts3 = "(m_vis>60) && (m_vis < 120) && (mt_1 < 60) && (idDeepTau2017v2p1VSe_2 >= 1 )"#VVVLose                                                                               
  mvis_cuts4 = "(m_vis>60) && (m_vis < 120) && (mt_1 < 60) && (idDeepTau2017v2p1VSe_2 >= 4 )"#VLose                                                                                 
  mvis_cuts5 = "(m_vis>60) && (m_vis < 120) && (mt_1 < 60) && (idDeepTau2017v2p1VSe_2 >= 16 )"#Medium                                                                               
  mvis_cuts6 = "(m_vis>60) && (m_vis < 120) && (mt_1 < 60) && (idDeepTau2017v2p1VSe_2 >= 64 )"#VTight                                                                               

  id_cuts3 = "(idDeepTau2017v2p1VSe_2 >= 1 )"#VVVLose                                                                                            
  id_cuts4 = "(idDeepTau2017v2p1VSe_2>=4)"#VLose                                                                                                   
  id_cuts5 = "(idDeepTau2017v2p1VSe_2>=16)"#Medium                                                                                                 
  id_cuts6 = "(idDeepTau2017v2p1VSe_2>=64)"#VTight                                                                                                 

  DTM_cuts1="(idDeepTau2017v2p1VSe_2>=16)&&(eta_2>-1.448)&&(eta_2<1.448)"
  DTM_cuts2="(idDeepTau2017v2p1VSe_2<16)&&(eta_2>-1.448)&&(eta_2<1.448)"
  DTM_cuts3="(idDeepTau2017v2p1VSe_2>=16)&&((eta_2<-1.556)||(eta_2>1.556))"
  DTM_cuts4="(idDeepTau2017v2p1VSe_2<16)&&((eta_2<-1.556)||(eta_2>1.556))"

  mt1_cuts= "(mt_1 < 60)"

  inclusive = inclusive.replace(" ","")
  general_cuts = general_cuts.replace(" ","")
  mvis_cuts1 = mvis_cuts1.replace(" ","")
  mvis_cuts2 = mvis_cuts2.replace(" ","")
  mvis_cuts3 = mvis_cuts3.replace(" ","")
  mvis_cuts4 = mvis_cuts4.replace(" ","")
  mvis_cuts5 = mvis_cuts5.replace(" ","")
  mvis_cuts6 = mvis_cuts6.replace(" ","")

  id_cuts3 = id_cuts3.replace(" ","")
  id_cuts4 = id_cuts4.replace(" ","")
  id_cuts5 = id_cuts5.replace(" ","")
  id_cuts6 = id_cuts6.replace(" ","")

  mt1_cuts = mt1_cuts.replace(" ","")
  DTM_cuts1 = DTM_cuts1.replace(" ","")
  DTM_cuts2 = DTM_cuts2.replace(" ","")
  DTM_cuts3 = DTM_cuts3.replace(" ","")
  DTM_cuts4 = DTM_cuts4.replace(" ","")

  tot_cuts1 = general_cuts + "&&" + mvis_cuts1
  tot_cuts1 = tot_cuts1.replace(" ","")
  tot_cuts2 = general_cuts + "&&" + mvis_cuts2
  tot_cuts2 = tot_cuts2.replace(" ","")

  tot_cuts3 = general_cuts + "&&" + mvis_cuts3
  tot_cuts3 = tot_cuts3.replace(" ","")
  tot_cuts4 = general_cuts + "&&" + mvis_cuts4
  tot_cuts4 = tot_cuts4.replace(" ","")
  tot_cuts5 = general_cuts + "&&" + mvis_cuts5
  tot_cuts5 = tot_cuts5.replace(" ","")
  tot_cuts6 = general_cuts + "&&" + mvis_cuts6
  tot_cuts6 = tot_cuts6.replace(" ","")

  totid_cuts3 = general_cuts + "&&" + id_cuts3
  totid_cuts3 = totid_cuts3.replace(" ","")
  totid_cuts4 = general_cuts + "&&" + id_cuts4
  totid_cuts4 = totid_cuts4.replace(" ","")
  totid_cuts5 = general_cuts + "&&" + id_cuts5
  totid_cuts5 = totid_cuts5.replace(" ","")
  totid_cuts6 = general_cuts + "&&" + id_cuts6
  totid_cuts6 = totid_cuts6.replace(" ","")

  tot_mt1_cuts1 = general_cuts + "&&" + mt1_cuts
  tot_mt1_cuts1 = tot_mt1_cuts1.replace(" ","")

  DTM_tot_cuts1 = general_cuts + "&&" + DTM_cuts1
  DTM_tot_cuts1 = DTM_tot_cuts1.replace(" ","")
  DTM_tot_cuts2 = general_cuts + "&&" + DTM_cuts2
  DTM_tot_cuts2 = DTM_tot_cuts2.replace(" ","")
  DTM_tot_cuts3 = general_cuts + "&&" + DTM_cuts3
  DTM_tot_cuts3 = DTM_tot_cuts3.replace(" ","")
  DTM_tot_cuts4 = general_cuts + "&&" + DTM_cuts4
  DTM_tot_cuts4 = DTM_tot_cuts4.replace(" ","")

#Selections
  selections = [
    #Sel('baseline, no DeepTauVSjet',baseline.replace(" && idDeepTau2017v2p1VSjet_2>=16","")),
    #Sel('baseline',baseline),
    #Sel('zttregion',repkey(zttregion,WP=16)),
    Sel('kinematic sel.',general_cuts),
    #Sel('tot_PuppiMET_DTMedium',tot_cuts1),                                                                                                                                        
    #Sel('tot_PuppiMET_DTTight',tot_cuts2),                                                                                                                                         
    #Sel('tot_PFMET_DTVVVL',tot_cuts3),                                                                                                                                             
    #Sel('tot_PFMET_DTVL',tot_cuts4),                                                                                                                                               
    #Sel('tot_PFMET_DTMedium',tot_cuts5),                                                                                                                                           
    #Sel('tot_PFMET_DTVTight',tot_cuts6),                                                                                                                                           
    #Sel('id_VSjM-VSeVVVL',totid_cuts3),
    #Sel('id_VSjM-VSeVL',totid_cuts4),
    #Sel('id_VSjM-VSeM',totid_cuts5),
    #Sel('id_VSjM-VSeVT',totid_cuts6),
    #Sel('inclusive',inclusive),                                                                                                                                                    
    #Sel('inclusive_cr_qcd',inclusive_cr_qcd),                                                                                                                                      
    #Sel('DTM1_VSjM-VSeM',DTM_tot_cuts1),                                                                                                                                           
    #Sel('DTM2_VSjM-VSeM',DTM_tot_cuts2),                                                                                                                                           
    #Sel('DTM3_VSjM-VSeM',DTM_tot_cuts3),                                                                                                                                           
    #Sel('DTM4_VSjM-VSeM',DTM_tot_cuts4),                                                                                                                                          
    #Sel('mt1_VSjM',tot_mt1_cuts1),   
  ]
  
  # VARIABLES
  variables = [
     Var('m_vis',  11,  60, 120),
     #Var('m_vis',  1,  60, 120),                                                                                                                                                   
     Var('pt_1',  "Muon pt",    40,  35, 120, ctitle={'etau':"Electron pt",'tautau':"Leading tau_h pt",'emu':"Electron pt"}),
     Var('pt_2',  "tau_h pt",   40,  20, 120, ctitle={'tautau':"Subleading tau_h pt",'emu':"Muon pt"}),
     Var('eta_1', "Electron eta",   30, -3, 3, ctitle={'etau':"Electron eta",'tautau':"Leading tau_h eta",'emu':"Electron eta"},ymargin=1.6,pos='T',ncols=2),
     Var('eta_2', "tau_h eta",  30, -3, 3, ctitle={'etau':"Tau eta",'tautau':"Subleading tau_h eta",'emu':"Muon eta"},ymargin=1.6,pos='T',ncols=2),
     Var('m_vis',  40,  0, 200),                                                                                                                                                
     Var('mt_1',  "mt(e,MET)", 40,  0, 200),                                                                                                                
     Var('mt_2',  "mt(e,PuppiMET)", 40,  0, 200),                                                                                                         
     Var("jpt_1",  29,   10,  300, veto=[r"njets\w*==0"]),                                                                                                
     Var("jpt_2",  29,   10,  300, veto=[r"njets\w*==0"]),                                                                                                  
     Var("jeta_1", 53, -5.4,  5.2, ymargin=1.6,pos='T',ncols=2,veto=[r"njets\w*==0"]),
     Var("jeta_2", 53, -5.4,  5.2, ymargin=1.6,pos='T',ncols=2,veto=[r"njets\w*==0"]),     
     Var('njets',   8,  0,   8),
     Var('met',    50,  0, 150),                                                                                                                                                   
     Var('puppimetpt', "PuppiMET"  , 50,  0, 150),                                                                                                                                 
     Var('pt_ll',   "p_{T}(mutau_h)", 25, 0, 200, ctitle={'etau':"p_{T}(etau_h)",'tautau':"p_{T}(tau_htau_h)",'emu':"p_{T}(emu)"}),                                                
     Var('dR_ll',   "DR(mutau_h)",    30, 0, 6.0, ctitle={'etau':"DR(etau_h)",'tautau':"DR(tau_htau_h)",'emu':"DR(emu)"}),                                                         
     Var('deta_ll', "deta(mutau_h)",  20, 0, 6.0, ctitle={'etau':"deta(etau_h)",'tautau':"deta(tautau)",'emu':"deta(emu)"},logy=True,pos='TRR'), #, ymargin=8, logyrange=2.6       
     Var('dzeta',  56, -180, 100, pos='L;y=0.88',units='GeV'),                                                                                                                     
     Var("pzetavis", 50,    0, 200 ),                                                                                                                                              
     Var('rawDeepTau2017v2p1VSjet_2', "rawDeepTau2017v2p1VSjet", 100, 0.0, 1, ncols=2,pos='L;y=0.85',logy=True,ymargin=2.5),
     Var('rawDeepTau2017v2p1VSjet_2', "rawDeepTau2017v2p1VSjet", 20, 0.80, 1, fname="$VAR_zoom",ncols=2,pos='L;y=0.85'),
     Var('rawDeepTau2017v2p1VSe_2',   "rawDeepTau2017v2p1VSe",   100, 0.0, 1, fname="$VAR",ncols=2,ymin=1.0, logy=True,pos='L;y=0.85'),
     Var('rawDeepTau2017v2p1VSe_2',   "rawDeepTau2017v2p1VSe",   30, 0.70, 1, fname="$VAR_zoom",ncols=2,logy=True,pos='L;y=0.85'),
     Var('rawDeepTau2017v2p1VSmu_2',  "rawDeepTau2017v2p1VSmu",  100, 0.0, 1, fname="$VAR",ncols=2,logy=True,logyrange=4,pos='L;y=0.85'),
     Var('rawDeepTau2017v2p1VSmu_2',  "rawDeepTau2017v2p1VSmu",  20, 0.80, 1, fname="$VAR_zoom",ncols=2,logy=True,logyrange=4,pos='L;y=0.85'),
     Var('npv',    40,    0,  80 ),     
  ]
  
  # PLOT
  outdir   = ensuredir(repkey(outdir,CHANNEL=channel,ERA=era))
  exts     = ['png','pdf'] if pdf else ['png'] # extensions
  for selection in selections:
    stacks = sampleset.getstack(variables,selection,method='QCD_OSSS',parallel=parallel)
    fname  = "%s/$VAR_%s-%s-%s$TAG"%(outdir,channel,selection.filename,era)
    text   = "%s: %s"%(channel.replace('mu',"#mu").replace('tau',"#tau_{h}"),selection.title)
    for stack, variable in stacks.iteritems():
      #position = "" #variable.position or 'topright'
      stack.draw()
      stack.drawlegend() #position)
      stack.drawtext(text)
      stack.saveas(fname,ext=exts,tag=tag)
      stack.close()
  

def main(args):
  channels = args.channels
  eras     = args.eras
  parallel = args.parallel
  pdf      = args.pdf
  outdir   = "plots/$ERA"
  tag      = ""
  fname    = "$PICODIR/$SAMPLE_$CHANNEL$TAG.root"
  for era in eras:
    for channel in channels:
      setera(era) # set era for plot style and lumi-xsec normalization
      sampleset = getsampleset(channel,era,fname=fname)
      plot(sampleset,channel,parallel=parallel,tag="",outdir=outdir,era=era,pdf=pdf)
  

if __name__ == "__main__":
  import sys
  from argparse import ArgumentParser
  argv = sys.argv
  description = """Simple plotting script for pico analysis tuples"""
  parser = ArgumentParser(prog="plot",description=description,epilog="Good luck!")
  parser.add_argument('-y', '--era',     dest='eras', nargs='*', choices=['2016','2017','2018','UL2017'], default=['2017'], action='store',
                                         help="set era" )
  parser.add_argument('-c', '--channel', dest='channels', nargs='*', choices=['mutau','etau'], default=['mutau'], action='store',
                                         help="set channel" )
  parser.add_argument('-s', '--serial',  dest='parallel', action='store_false',
                                         help="run Tree::MultiDraw serial instead of in parallel" )
  parser.add_argument('-p', '--pdf',     dest='pdf', action='store_true',
                                         help="create pdf version of each plot" )
  parser.add_argument('-v', '--verbose', dest='verbosity', type=int, nargs='?', const=1, default=0, action='store',
                                         help="set verbosity" )
  args = parser.parse_args()
  LOG.verbosity = args.verbosity
  PLOG.verbosity = args.verbosity
  main(args)
  print "\n>>> Done."
  

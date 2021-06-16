###WIP###
ERA=2016
OUTDIR=coutFR_$ERA
mkdir $OUTDIR
apath=/afs/cern.ch/work/l/lvigilan/TauWork/CMSSW_8_1_0/src/

cd /afs/cern.ch/work/l/lvigilan/TauWork/CMSSW_8_1_0/src/
eval `scramv1 runtime -sh`
cd - 
#templateFittingETauFR zee_fr_m_vis_eta0to1.448_et-2016.inputs.root VLoose | tee ./zee_fr_m_vis_eta0to1.448_et-2016.inputs.txt
#text2workspace.py -m 90 -P TauFW.Fitter.ETauFR.zttmodels:ztt_eff --PO "eff=0.0491043" ./input/2016/ETauFR/VVTight_eta1.56to2.3.txt -o  WorkSpaceVLooseLt1p460.root
#text2workspace.py -m 90 -P HiggsAnalysis.ETauFR.zttmodels:ztt_eff --PO "0.002589471" ./input/2016/ETauFR/VVVTight_eta0to1.46.txt -o  WorkSpaceVVVTightLt1p46.root
text2workspace.py -m 90 -P HiggsAnalysis.ETauFR.zttmodels:ztt_eff --PO "0.00189732462718" ./input/2016/ETauFR/VVTight_eta1.56to2.3.txt -o  WorkSpaceVVTightLt2p300.root
#combine -m 90  -M FitDiagnostics --robustFit=1 --expectSignal=1.0 --rMin=0.7 --rMax=1.5 --cminFallbackAlgo "Minuit2,0:1" -n "" WorkSpaceVVTightLt1p46.root | tee ./$OUTDIR/ScaleVVTightLt1p46.txt
#combine -m 90  -M FitDiagnostics --robustFit=0 --expectSignal=1.0 --rMin=0.0 --rMax=3.0 --cminFallbackAlgo "Minuit2,0:1" -n "" WorkSpaceVVTightLt1p46.root | tee ./$OUTDIR/ScaleVVTightLt1p46.txt
combine -m 90  -M FitDiagnostics --robustFit=1 --expectSignal=1.0 --rMin=0.0 --rMax=3.0 --cminFallbackAlgo "Minuit2,0:1" -n "" WorkSpaceVVTightLt2p300.root | tee ./$OUTDIR/ScaleVVTightLt2p300.txt
#./compare.py -a fitDiagnostics.root | tee ./$OUTDIR/VVTightLt1p46Pull.txt
./compare.py -a fitDiagnostics.root | tee ./$OUTDIR/VVTightLt2p300Pull.txt
#./compare.py -a fitDiagnostics.root | tee ./$OUTDIR/VVTightLt1p46Pull.txt
#PostFitShapesFromWorkspace -o ETauFRVVTightLt1p46_PostFitShape.root -m 90 -f fitDiagnostics.root:fit_s --postfit --sampling --print -d zee_fr_m_vis_eta0to1.46_et-2016.inputs.txt -w WorkSpaceVVTightLt1p46.root
#PostFitShapesFromWorkspace -o ETauFRVVTightLt1p46_PostFitShape.root -m 90 -f fitDiagnostics.root:fit_s --postfit --sampling --print -d ./input/2016/ETauFR/VVTight_eta0to1.46.txt -w WorkSpaceVVTightLt1p46.root
PostFitShapesFromWorkspace -o ETauFRVVTightLt2p300_PostFitShape.root -m 90 -f fitDiagnostics.root:fit_s --postfit --sampling --print -d ./input/2016/ETauFR/VVTight_eta1.56to2.3.txt -w WorkSpaceVVTightLt2p300.root

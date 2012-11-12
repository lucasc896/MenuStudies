{
	gROOT->ProcessLine(".X ~/trigger_studies/temp/CMSSW_5_3_1/src/UserCode/L1TriggerDPG/macros/initL1Analysis.C");
	gROOT->ProcessLine(".X ~/trigger_studies/temp/CMSSW_5_3_1/src/UserCode/L1TriggerDPG/macros/upgrade/style_macro.C");
	cout << "Loading Upgrade Analysis Macro" << endl;
	gROOT->ProcessLine(".L ~/trigger_studies/temp/CMSSW_5_3_1/src/UserCode/L1TriggerDPG/macros/upgrade/UpgradeAnalysis_12.C+");
	UpgradeAnalysis_12 a;
	a.OpenWithList("inputFiles/inputFiles_ZBHPF1_UP_2012HPF_45_v3.txt");
	Int_t nLumis = gROOT->ProcessLine("a->FillDistros(-1,92,0,10045, 45, \"lumiStuff/getLumi_out_pixCorrLumi_45PU_stdCorr.txt\",1)");
	//Int_t nLumis = 143; //for use with 45PU ntuples
//	gROOT->ProcessLine("a->MakeRatePlots(92,0,10045, nLumis, 45, \"getLumi_out_pixCorrLumi_45PU_stdCorr.txt\")");
}

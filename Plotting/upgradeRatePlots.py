#!/usr/bin/env python
# encoding: utf-8
"""
upgradeRatePlots.py

Created by Chris Lucas on 2012-10-10.
Copyright (c) 2012 University of Bristol. All rights reserved.
"""

from sys import argv
from ratePlottingUtils import *


r.gROOT.SetBatch(True)

if len(argv)<2:
	print "Please specify a PU scenario, e.g. './upgradeRatePlots.py <PU>"
	sys.exit()

if argv[1] == "66":
	inFileName = "../out_files/output_0-10066.root"
	outFileName = "ratePlots_66PU.pdf"
	puScen = 66
elif argv[1] == "45":
	inFileName = "../out_files/output_0-10045.root"
	outFileName = "ratePlots_45PU.pdf"
	puScen = 45

print "\n\n*************************************"
print " > Making Plots for %dPU Scenario < "%(puScen)
print "*************************************\n"


rFile = r.TFile.Open(inFileName)
print "* Input File: %s\n"%(inFileName)

histList = {
#		"jets":(["combJets_1_rate",
#				"combJets_2_rate",
#				"combJets_3_rate",
#				"combJets_4_rate",]),
#
#		"jetsEr":(["combJetsEr_1_rate",
#				"combJetsEr_2_rate",
#				"combJetsEr_3_rate",
#				"combJetsEr_4_rate",]),
#
#		"jetsUp":(["up_towerJet_1_rate",
#				"up_towerJet_2_rate",
#				"up_towerJet_3_rate",
#				"up_towerJet_4_rate",]),
#
#		"combEG":(["combEG_1_rate",
#				"combEG_2_rate",
#				"combEG_3_rate",
#				"combEG_4_rate",]),
#		
#		"combEGUp":(["up_combEG_1_rate",
#				"up_combEG_2_rate",
#				"up_combEG_3_rate",
#				"up_combEG_4_rate",]),
#
#		"enSums":(["ETT_rate",
#				"ETM_rate",
#				"HTT_rate",
#				"HTM_rate",]),
#
#		"isoEG":(["isoEG_1_rate",
#			"isoEG_2_rate",
#			"isoEG_3_rate",
#			"isoEG_4_rate",]),
#
#		"isoEGUp":(["up_isoEm_1_rate",
#			"up_isoEm_2_rate",
#			"up_isoEm_3_rate",
#			"up_isoEm_4_rate"]),
#
#		"nonIsoEGUp":(["up_nonIsoEm_1_rate",
#			"up_nonIsoEm_2_rate",
#			"up_nonIsoEm_3_rate",
#			"up_nonIsoEm_4_rate"]),
#
#		"tau":(["tau_1_rate",
#			"tau_2_rate",],),
#
#		"isoTauUp":(["up_isoTau_1_rate",
#			"up_isoTau_2_rate",
#			"up_isoTau_3_rate",
#			"up_isoTau_4_rate"]),		
#
#		"nonIsoTauUp":(["up_nonIsoTau_1_rate",
#			"up_nonIsoTau_2_rate",
#			"up_nonIsoTau_3_rate",
#			"up_nonIsoTau_4_rate"]),
#
#		"combTauUp":(["up_combTau_1_rate",
#			"up_combTau_2_rate",
#			"up_combTau_3_rate",
#			"up_combTau_4_rate",]),
##
##		"muonHi":(["muon_hi_1_rate",
##			"muon_hi_2_rate",
##			"muon_hi_3_rate",
##			"muon_hi_4_rate",]),
#
#		"crossTrig1":(["DoubleJetEtar_rate",
#			"SingleMuonEtar_rate",]),
#
#		"crossTrig2":(["doubleEGCross_rate",
#			"doubleMuCross_rate",
#			"EGMuCross_rate",
#			"MuEGCross_rate",
#			"MuJetCross_rate",]),
#
		"jetCompare":(["cenpTauJets_1_rate",
			"cenpTauJets_2_rate",
			"cenpTauJets_3_rate",
			"cenpTauJets_4_rate",],
			["up_towerJet_1_rate",
			"up_towerJet_2_rate",
			"up_towerJet_3_rate",
			"up_towerJet_4_rate",]),

		"isoEGCompare:":(["isoEG_1_rate",
			"isoEG_2_rate",
			"isoEG_3_rate",
			"isoEG_4_rate",],
			["up_isoEm_1_rate",
			"up_isoEm_2_rate",
			"up_isoEm_3_rate",
			"up_isoEm_4_rate"],),

		"crossTrigCompare":(["doubleEGCross_rate",
			"EGMuCross_rate",
			"MuEGCross_rate",],
			["up_doubleEGCross_rate",
			"up_EGMuCross_rate",
			"up_MuEGCross_rate"],),

		"tauCompare":(["tau_1_rate",
			"tau_2_rate",],
			["up_combTau_1_rate",
			"up_combTau_2_rate"],),

}

c1 = Print(outFileName)
c1.DoPageNum = False
c1.open("SLHC L1 Trigger Rate Plots - ZBHPF1 @ %sPU"%puScen)
c1.SetGrid(True)
c1.SetLog('y', True)

for key,hists in sorted(histList.items()):
	rawHist=[]
	rawUpHist=[]
	print "\n * Making plot %s *"%(key) 

	if "tuple" in str(type(hists)):
		# contains an norm/upgrade comparison
		for h, uh in zip(hists[0],hists[1]):
			rawHist.append(rFile.Get(h))
			rawUpHist.append(rFile.Get(uh))
		a = RatePlot(hists=rawHist, upHists=rawUpHist)	
	elif "list" in str(type(hists)):
		# contains no comparison
		for h in hists:
			rawHist.append(rFile.Get(h))
		a = RatePlot(hists=rawHist)

	#a.Debug = True
	a.PUScen = puScen

	c1.PrintCanvas( a.MakeRatePlot() )

	del a

c1.close()

# +++ Print Specific Rates +++ #

menu45 = {
	"SingleEG34":["combEG_1_rate",34.],
	"SingleIsoEG27er2p17":["isoEG_1_rate",27.],
	"DoubleEG16:9":["doubleEGCross_rate",16.],
	"SingleMu120":["muon_hi_1_rate",120.],
	"DoubleMu13Open":["doubleMuCross_rate", 13.],
	"EGMu15:5":["EGMuCross_rate", 15.],
	"MuEG13:8":["MuEGCross_rate", 13.],
	"SingleJet165":["combJets_1_rate",165.],
	"DoubleJet85Er3":["combJetsEr_2_rate",85.],
	"QuadJet60":["combJets_4_rate", 60.],
	"DoubleTau52Er2p17":["tau_2_rate",52.],
	"ETM50":["ETM_rate",50.],
	"HTT340":["HTT_rate",340.],
}

menu66 = {
	"SingleEG34":["combEG_1_rate",37.],
	"SingleIsoEG27er2p17":["isoEG_1_rate",27.],
	"DoubleEG16:9":["doubleEGCross_rate",16.],
	"SingleMu120":["muon_hi_1_rate",120.],
	"DoubleMu13Open":["doubleMuCross_rate", 13.],
	"EGMu15:5":["EGMuCross_rate", 15.],
	"MuEG13:8":["MuEGCross_rate", 13.],
	"SingleJet165":["combJets_1_rate",192.],
	"DoubleJet85Er3":["combJetsEr_2_rate",92.],
	"QuadJet60":["combJets_4_rate", 72.],
	"DoubleTau52Er2p17":["tau_2_rate",50.],
	"ETM50":["ETM_rate",60.],
	"HTT340":["HTT_rate",550.],
}

if puScen == 45:
	rateDict = menu45
	rateFileName = "rateVals_45PU.txt"
elif puScen == 66:
	rateDict = menu66
	rateFileName = "rateVals_66PU.txt"

textFile = open(rateFileName, 'w')

textFile.write("+++ Trigger Rates - %dPU +++\n\n"%puScen)

for key, val in rateDict.items():
		rate = GetRateVal(rFile.Get(val[0]),val[1])
		text ="%s\t\t%f \pm %f\n"%(key, rate[0], rate[1])
		textFile.write(text)


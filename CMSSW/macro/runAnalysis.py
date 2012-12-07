#!/usr/bin/env python
# encoding: utf-8
"""
runAnalysis.py

Created by Chris Lucas on 2012-12-06.
Copyright (c) 2012 University of Bristol. All rights reserved.
"""

import ROOT as r


def switches():

   mySwitches={
         "nEvts":1000,
         "isData":[0, 1][0],
         "sampPU":[45, 50, 66][1],
         "doUpgrade":[0, 1][0],
   }

   return mySwitches

def inFiles():

   inFile = ""

   if switches()["isData"]:
      if switches()["sampPU"]==66:
         inFile = "inputFiles/inputFiles_ZBHPF1_UP_2012HPF_66_v3.txt"
   else:
      if switches()["sampPU"]==50:
         inFile = "inputFiles/inputFiles_MC_Neut_Pt_2to20_PostLS1_v1_realShort.txt"

   return inFile

def runDetails():

   runFile=""

   if switches()["isData"]:
      if switches()["sampPU"]==66:
         runFile = "lumiStuff/getLumi_out_pixCorrLumi_66PU_stdCorr.txt"
      elif switches()["sampPU"]==45:
         runFile = "lumiStuff/getLumi_out_pixCorrLumi_45PU_stdCorr.txt"

   return runFile


#### MAIN PROGRAM ####


print ">>> Loading L1 Analysis Macro"
r.gROOT.ProcessLine(".X ~/trigger_studies/temp/CMSSW_5_3_1/src/UserCode/L1TriggerDPG/macros/initL1Analysis.C")
r.gROOT.ProcessLine(".L ~/trigger_studies/temp/CMSSW_5_3_1/src/UserCode/L1TriggerDPG/macros/upgrade/UpgradeAnalysis_12.C+")

r.gROOT.ProcessLine("UpgradeAnalysis_12 a(data=%s, samplePU=%d, mcNotes=\"%s\")"%
      (switches()["isData"],
      switches()["sampPU"],
      inFiles()[22:-4]))

r.gROOT.ProcessLine("a.OpenWithList( \"%s\" )"%inFiles())

r.gROOT.ProcessLine("a.FillDistros(%d, \"%s\", %d)"%
   (switches()["nEvts"],
   runDetails(),
   switches()["doUpgrade"]))

r.gROOT.ProcessLine(".q")

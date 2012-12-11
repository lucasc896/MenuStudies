#!/usr/bin/env python
# encoding: utf-8
"""
ratePlottingUtils.py

Created by Chris Lucas on 2012-10-10.
Copyright (c) 2012 University of Bristol. All rights reserved.
"""

import sys
import os
import ROOT as r
import math


def GetRateVal(h1=None, thresh=0):
  ibin = h1.FindBin(thresh)
  return h1.GetBinContent(ibin), h1.GetBinError(ibin)


class RatePlot(object):
  """Rate plot producer"""
  def __init__(self, hists = None, upHists = []):
    super(RatePlot, self).__init__()
    self.hists = hists
    self.upHists = upHists
    self.listColors = [r.kBlack, r.kRed, r.kBlue, r.kGreen, r.kYellow-2, r.kMagenta]
    self.xLower = 0
    self.xUpper = 1
    self.xRebin = 1
    self.Debug = False
    self.DoGrid = True
    self.PUScen = 0
    self.numPlots = len(hists) + len(upHists)
    self.lg = r.TLegend()
    self.c1 = r.TCanvas()
    self.SetStyle()

  def MakeRatePlot(self):
    """docstring for MakeRatePlot"""
    self.c1.SetLogy()

    if not self.DoGrid: c1.SetGrid(kFALSE)

    self.MakeLegend()

    ctr=0
    for h, kCol in zip(self.hists, self.listColors):
      if self.Debug: print "*** Hist: ", h
      if ctr==0:
        h.Draw()
        h.GetYaxis().SetRangeUser(0.01,100000)
        h.GetYaxis().SetLabelSize(0.04)
        h.GetXaxis().SetTitleSize(0.04)
      h.SetLineColor(kCol)
      h.SetFillColor(0)
      h.Rebin(self.xRebin)
      h.DrawCopy("histsame")

      if self.xUpper != 1:
        h.GetXaxis().SetRangeUser(self.xLower, self.xUpper)
      #h.DrawCopy("same")
      #h.SetFillColor(r.kViolet)
      #h.Draw("same")

      self.lg.AddEntry(h, h.GetTitle(), "L")

      if self.Debug:
        print "Color", kCol
        print "Counter", ctr

      ctr+=1
    
    if self.Debug: print "*** Upgrade Hist List:", self.upHists

    for uh, kCol in zip(self.upHists, self.listColors):
      if self.Debug: print "*** Upgrade Hist: ", uh
      
      uh.SetLineColor(kCol)
      uh.SetLineStyle(2)
      uh.SetFillColor(0)
      uh.DrawCopy("histsame")
      uh.SetFillColor(r.kViolet)
      uh.Draw("same")
      self.lg.AddEntry(uh, uh.GetTitle(), "L")

    self.lg.Draw()

    if self.Debug: print "*** Canvas: ", self.c1


    return self.c1
  

  def SetStyle(self):
    """docstring for SetStyle"""
    r.gStyle.SetOptStat(0)
    r.gStyle.SetOptTitle(0)
    pass


  def MakeLegend(self):
    """docstring for MakeLegend"""
    if self.numPlots <= 6:
      self.lg = r.TLegend(0.55, 0.7, 0.89, 0.89)
    elif self.numPlots > 6:
      self.lg = r.TLegend(0.55, 0.65, 0.89, 0.89)

    if self.PUScen != 0:
      self.lg.SetHeader(str(self.PUScen)+"PU Scenario")

    self.lg.SetFillColor(0)
    self.lg.SetFillStyle(0)
    self.lg.SetLineColor(0)
    self.lg.SetLineStyle(0)



class Print(object):
  """docstring for printPDF"""
  def __init__(self, Fname):
    super(Print, self).__init__()
    self.canvas = r.TCanvas()
    self.DoPageNum = True
    self.fname = Fname
    # self.rfile = r.TFile(self.fname[:-4]+".root",'RECREATE')
    self.pageCounter = 1
    self.open()


  def toFile(self,ob,title):
    """docstring for toFile"""
    # self.rfile.cd()
    # ob.SetName(title)
    # ob.SetTitle(title)
    # ob.Write()
    # ob = None
    pass

  def cd(self):
    """docstring for cd"""
    self.canvas.cd()
    pass


  def open(self, frontText = "<none>"):
    """docstring for open"""
    tpt1 = r.TText(0.07, 0.26, frontText)
    tpt2 = r.TText(0.07, 0.2, "Chris Lucas")
    tpt1.Draw()
    tpt2.Draw()
    self.canvas.Print(self.fname+"[")
    r.gPad.SetRightMargin(0.15)
    r.gPad.SetLeftMargin(0.15)
    r.gPad.SetTopMargin(0.1)
    r.gPad.SetBottomMargin(0.2)   

    pass


  def close(self):
    """docstring for close"""
    # self.rfile.Write()
    # self.rfile.Close()
    self.canvas.Print(self.fname+"]")
    pass


  def Clear(self):
    """docstring for Clear"""
    self.canvas.Clear()
    pass

  def SetLog(self,axis,BOOL):
    """docstring for SetLog"""
    if 'x' in axis:
      if BOOL:
        self.canvas.SetLogx()
      else:
        self.canvas.SetLogx(r.kFALSE)
    if 'y' in axis:
      if BOOL:
        self.canvas.SetLogy()
      else:
        self.canvas.SetLogy(r.kFALSE)
    pass

  def SetGrid(self,BOOL):
    """docstring for SetGrid"""
    if BOOL:
      self.canvas.SetGrid()
    else:
      self.canvas.SetGrid(r.kFALSE)
    pass


  def Print(self):
    """docstring for Print"""
    num = r.TLatex(0.95,0.01,"%d"%(self.pageCounter))
    num.SetNDC()
    if self.DoPageNum: num.Draw("same")
    # self.canvas.SetGridx()
    # self.canvas.SetGridy()
    self.canvas.Print(self.fname)
    self.pageCounter += 1
    pass

  def PrintCanvas(self, c1):
    """docstring for PrintCanvas"""
    num = r.TLatex(0.95,0.01,"%d"%(self.pageCounter))
    num.SetNDC()
    if self.DoPageNum: num.Draw("same")
    c1.Print(self.fname)
    self.pageCounter += 1
    pass


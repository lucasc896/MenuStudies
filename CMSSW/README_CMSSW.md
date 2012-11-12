MenuStudies - CMSSW
===========

##Basic Intro
This code is based upon the L1TriggerDPG root analysis macro, found [here](http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/L1TriggerDPG/macros/).

## Recipe
The CMSSW environment is setup using the following:

```
scram p CMSSW CMSSW_5_3_3_patch2
cd CMSSW_5_3_3_patch2/src
cmsenv
cvs co UserCode/L1TriggerDPG
cvs co UserCode/L1TriggerUpgrade
```

Place the UpgradeAnalysis code into the L1TriggerDPG code:

```
cd UserCode/L1TriggerDPG/macros
mkdir upgrade
cd upgrade
<MORE>
```

Build your CMSSW framework:

```
cd $CMSSW_BASE/src
scram b -j 4
```

## Instructions

The code is run using the following executable macro:

```
root -l runAna_66_upgrade.C
```

_Note: a similar file for the 45PU scenario can be used._

Within this macro various parameters can be changed wrt the running of the macro.

## Additional information
###getLumi.py

This script is used to get the run lumi details file used in the main analysis macro. It takes the run json as input and calculates "LS\nIntLumi\nInstLumi\nPU" for each LS.

It is run using the following recipe:

```
FIXME: Add recipe for getLumi.py
```
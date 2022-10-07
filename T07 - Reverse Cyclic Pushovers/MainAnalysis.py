"""
An alternative to haveing three seperate files, this main analyiss can run all 
of the input analyses out of one file.
"""


import openseespy.opensees as op
import numpy as np

import functions.ModelFunctions as mf
import functions.AnalysisFunctions as af
import functions.RecorderFunctions as rf
import functions.PlotFunctions as pf

# =============================================================================
# Define Variables
# =============================================================================

pushoverLcDispName  = 'Pushover_Lc_Disp'
pushoverDcName      = 'Pushover_Dc'
pushoverArcName     = 'Pushover_Arc'

runAnalysisLcD = False
runAnalysisDcF = True
runAnalysisArc = False

loadProtocol = [0.001547,  0.00221, 0.003315, 0.00442, 0.00663, 0.00884, 0.01326,
                0.01768,   0.02652, 0.03978,  0.05967, 0.0884,  0.1326,  0.1768, 0.221, 
                0.3315,    0.4199,  0.4862]
Nrepeat     = 3*np.ones_like(loadProtocol, int)

# =============================================================================
# Load control with Disp
# =============================================================================

op.wipe()
if runAnalysisLcD == True:
    
    # Build Model
    mf.getSections()
    mf.buildModel()
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverLcDispName, pushoverLcDispName)
    time, LF = af.CyclicAnalysisLc(0.3)
    op.wipe()
    
    # Plot Analysis
    pf.plotPushover(pushoverLcDispName, pushoverLcDispName)
    
# =============================================================================
# Disp control with force
# =============================================================================

op.wipe()
if runAnalysisDcF == True:
    # Build Model
    mf.getSections()
    mf.buildModel()
        
    # Run Analysis
    rf.getPushoverRecorders(pushoverDcName, pushoverDcName)
    af.CyclicAnalysisDcL(loadProtocol, Nrepeat)
    # af.PushoverDcF(0.1)
    op.wipe()
    
    # Plot Analysis
    u, F = pf.plotPushover(pushoverDcName, pushoverDcName)
    
    
# =============================================================================
# 
# =============================================================================
    
op.wipe()
if runAnalysisArc == True:
    
    
    # Build Model
    mf.getSections()
    mf.buildModel()
        
    # Run Analysis
    rf.getPushoverRecorders(pushoverDcName, pushoverDcName)
    # af.CyclicAnalysisDc(int(NAnalysisSteps[2]))
    # af.PushoverArc(0.1)
    af.CyclicAnalysisArc(0.3, 0.00001)
    op.wipe()
    
    # Plot Analysis
    pf.plotPushover(pushoverDcName, pushoverDcName)
    
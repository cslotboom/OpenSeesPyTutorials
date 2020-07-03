

import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np


import ModelFunctions as mf
import AnalysisFunctions as af
import RecorderFunctions as rf
import PlotFunctions as pf

# =============================================================================
# Define Variables
# =============================================================================

pushoverLcForceName = 'Pushover_Lc_Force'
pushoverLcDispName = 'Pushover_Lc_Disp'
pushoverDcForceName = 'Pushover_Dc_Force'


runAnalysisLcF = False
runAnalysisLcD = True
runAnalysisDcF = False

NAnalysisSteps = np.array([208, 5000, 5000])

# =============================================================================
# Load control with force
# =============================================================================

op.wipe()
if runAnalysisLcF == True:
    
    
    # Build Model
    mf.getSections()
    mf.buildModel()
    
    # opp.plot_model()    
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverLcForceName, pushoverLcForceName)
    af.PushoverLcF(int(NAnalysisSteps[0]))
    op.wipe()
    
    # Plot Analysis
    pf.plotPushover(pushoverLcForceName, pushoverLcForceName)

# =============================================================================
# Load control with Disp
# =============================================================================

op.wipe()

if runAnalysisLcD == True:
    
    
    # Build Model
    mf.getSections()
    mf.buildModel()
    
    # opp.plot_model()    
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverLcDispName, pushoverLcDispName)
    af.PushoverLcD(int(NAnalysisSteps[1]))
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
    
    # opp.plot_model()    
    
    # Run Analysis
    rf.getPushoverRecorders(pushoverDcForceName, pushoverDcForceName)
    af.PushoverDcF(int(NAnalysisSteps[2]))
    op.wipe()
    
    # Plot Analysis
    pf.plotPushover(pushoverDcForceName, pushoverDcForceName)
    

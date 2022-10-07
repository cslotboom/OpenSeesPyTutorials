import openseespy.opensees as op
import numpy as np

import functions.ModelFunctions as mf
import functions.AnalysisFunctions as af
import functions.RecorderFunctions as rf
import functions.PlotFunctions as pf

# =============================================================================
# Define Variables
# =============================================================================
m = 1
mm = 0.001

pushoverLcDispName  = 'Pushover_Lc_Disp'
dmax    = 0.3*m
du      = 0.00001*m

# =============================================================================
# Load control with Disp
# =============================================================================

op.wipe()

# Build Model
mf.getSections()
mf.buildModel()

# Run Analysis
rf.getPushoverRecorders(pushoverLcDispName, pushoverLcDispName)
time, LF = af.CyclicAnalysisLc(dmax)
op.wipe()

# Plot Analysis
pf.plotPushover(pushoverLcDispName, pushoverLcDispName)
    
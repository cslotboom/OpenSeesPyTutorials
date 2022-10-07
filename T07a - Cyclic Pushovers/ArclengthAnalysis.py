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

pushoverArcName     = 'Pushover_Arc'
dmax    = 0.3*m
du      = 0.00001*m

# =============================================================================
# Run Analysis
# =============================================================================

op.wipe()
   
# Build Model
mf.getSections()
mf.buildModel()
    
# Run Analysis
rf.getPushoverRecorders(pushoverArcName, pushoverArcName)

af.PushoverArc(0.1)
af.CyclicAnalysisArc(dmax, du)
op.wipe()

# Plot Analysis
pf.plotPushover(pushoverArcName, pushoverArcName)
    
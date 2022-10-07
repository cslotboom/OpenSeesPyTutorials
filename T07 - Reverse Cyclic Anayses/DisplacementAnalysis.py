import openseespy.opensees as op
import numpy as np

import functions.ModelFunctions as mf
import functions.AnalysisFunctions as af
import functions.RecorderFunctions as rf
import functions.PlotFunctions as pf

# =============================================================================
# Define Variables
# =============================================================================

pushoverDcName      = 'Pushover_Dc'

loadProtocol = [0.001547,  0.00221, 0.003315, 0.00442, 0.00663, 0.00884, 0.01326,
                0.01768,   0.02652, 0.03978,  0.05967, 0.0884,  0.1326,  0.1768, 0.221, 
                0.3315,    0.4199,  0.4862]
Nrepeat      = 3*np.ones_like(loadProtocol, int)


# =============================================================================
# Disp control with force
# =============================================================================

op.wipe()

# Build Model
mf.getSections()
mf.buildModel()
    
# Run Analysis
rf.getPushoverRecorders(pushoverDcName, pushoverDcName)

# af.PushoverDcF(0.1)
af.CyclicAnalysisDcL(loadProtocol, Nrepeat)
op.wipe()

# Plot Analysis
u, F = pf.plotPushover(pushoverDcName, pushoverDcName)

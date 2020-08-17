import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np


import ModelFunctions as mf
import AnalysisFunctions as af

# =============================================================================
# Load control with Disp
# =============================================================================

op.wipe()

# Build Model
mf.getSections()
mf.buildModel()

# Run Analysis
af.PushoverLcD(0.05)

op.wipe()

# =============================================================================
# Animation outputs
# =============================================================================





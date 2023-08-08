import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp


import ModelFunctions as mf
import AnalysisFunctions as af



# =============================================================================
# Load control with Disp
# =============================================================================

op.wipe()

# Build Model
mf.getSections()
mf.buildModel()

# Show Model
# opp.plot_model('node', 'elements')

# Create Database
Model = 'Cantilever'
LoadCase = 'PushoverLcD'
opp.createODB(Model, LoadCase)

eleNumber = 1
sectionNumber = 1
opp.saveFiberData2D(Model, LoadCase, eleNumber, sectionNumber)

# Run Analysis
af.PushoverLcD(0.05)

out = op.eleResponse(1, 'section', '1', 'fiberData')

op.wipe()

opp.plot_fiberResponse2D(Model, LoadCase, eleNumber, sectionNumber)
opp.plot_fiberResponse2D(Model, LoadCase, eleNumber, sectionNumber, InputType='strain')

#
ani = opp.animate_fiberResponse2D(Model, LoadCase, eleNumber, sectionNumber)


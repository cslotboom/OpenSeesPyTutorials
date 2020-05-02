# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:38:22 2020

@author: Christian
"""

import openseespy.opensees as op


# =============================================================================
# Units
# =============================================================================

m = 1
N = 1
Pa = 1

inches = 0.0254*m
ft = 12*inches
kip = 4.45*10**3*N
Ksi = 6.89*10**6*Pa


def GetSections(E):
    # remove existing model
    op.wipe()
    
    # set modelbuilder
    op.model('basic', '-ndm', 2, '-ndf', 3)
    
    # define materials
    op.uniaxialMaterial("Elastic", 1, E)


def GetModel(A1, A2):
    
    x1 = 0.
    y1 = 0.
    
    x2 = 12.*ft
    y2 = 0.
    
    x3 = 14.*ft
    y3 = 0.
    
    x4 = 6.*ft
    y4 = 8.*ft

    # create nodes
    op.node(1, x1, y1)
    op.node(2, x2, y2)
    op.node(3, x3, y3)
    op.node(4, x4, y4)
    
    
    # set boundary condition
    op.fix(1, 1, 1, 1)
    op.fix(2, 1, 1, 1)
    op.fix(3, 1, 1, 1)
    op.fix(4, 0, 0, 1)
    
    # define elements
    # op.element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
    op.element("Truss", 1, 1, 4, A1, 1)
    op.element("Truss", 2, 2, 4, A2, 1)
    op.element("Truss", 3, 3, 4, A2, 1)


def GetRecordersPushover(AnalysisName):
    # Record Results
    op.recorder('Node', '-file',AnalysisName + "_NodeDisp.out", '-time', '-node', 4, '-dof', 1,2,3,'disp')
    op.recorder('Node', '-file', AnalysisName + "_Reaction.out", '-time', '-node', 1,2,3, '-dof', 1,2,3,'reaction')
    op.recorder('Element', '-file', AnalysisName + "_Elements.out",'-time','-ele', 1,2,3, 'forces')



def RunPushoverAnalysis(Px,Py):


    # create TimeSeries
    op.timeSeries("Linear", 1)
    
    # create a plain load pattern
    op.pattern("Plain", 1, 1)
    
    # Create the nodal load - command: load nodeID xForce yForce
    op.load(4, Px, Py, 0.)
    
    # create SOE
    op.system("BandSPD")
    # create DOF number
    op.numberer("RCM")
    # create constraint handler
    op.constraints("Plain")
    
    # create integrator
    op.integrator("LoadControl", 1.0)
    
    # create algorithm
    op.algorithm("Newton")
    
    # create analysis object
    op.analysis("Static")
    
    # perform the analysis
    op.initialize() 
    
    
    ok = op.analyze(1)
    
    
    # op.wipe()


def RunGravityAnalysis(Py):


    # create TimeSeries
    op.timeSeries("Linear", 1)
    
    # create a plain load pattern
    op.pattern("Plain", 1, 1)
    
    # Create the nodal load - command: load nodeID xForce yForce
    op.load(4, 0, Py, 0.)
    
    # create SOE
    op.system("BandSPD")
    # create DOF number
    op.numberer("RCM")
    # create constraint handler
    op.constraints("Plain")
    
    # create integrator
    op.integrator("LoadControl", 1.0)
    
    # create algorithm
    op.algorithm("Newton")
    
    # create analysis object
    op.analysis("Static")
    
    # perform the analysis
    op.initialize() 
    
    
    ok = op.analyze(1)
    
    
    # op.wipe()







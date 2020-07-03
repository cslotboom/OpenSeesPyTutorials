

import openseespy.opensees as op

N = 1
kN = 1000*N
m = 1


def PushoverLcF(Nsteps):
    
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1.*kN
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.load(ControlNode, dForce, 0., 0.)
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("LoadControl", 1.0)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-11, 50)
    
    # Run Analysis
    
    op.record()
    ok = op.analyze(Nsteps)


def PushoverLcD(Nsteps):
    
    ControlNode = 4
    ControlNodeDof = 1
    du = 0.00001*m
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.sp(ControlNode, ControlNodeDof, du)
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("LoadControl", .1)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    
    # Run Analysis
    
    op.record()

    ok = op.analyze(Nsteps)
    nn = 0     
        
    
    
    
def PushoverDcF(Nsteps):
    
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1.*kN
    du = 0.00001*m
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.load(ControlNode, dForce, 0., 0.)
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("DisplacementControl", ControlNode, ControlNodeDof, du)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-11, 50)
    
    # Run Analysis
    
    op.record()
    
    ok = op.analyze(Nsteps)

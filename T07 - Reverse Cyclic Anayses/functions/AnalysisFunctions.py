import openseespy.opensees as op
import random
N = 1
kN = 1000*N
m = 1


def analysisLoopBasic(ok, nn, Size):
    """
    The load control analysis loop.
    """
    
    if ok != 0:
        print("Trying 5 times smaller timestep at load factor", nn)
        op.integrator("LoadControl", Size/5)
        ok = op.analyze(1)

    if ok != 0:
        print("Trying 20 times smaller timestep at load factor", nn)
        op.integrator("LoadControl", Size/20)
        ok = op.analyze(1)        
        
    if ok != 0:
        print("Trying 80 times smaller timestep at load factor", nn)
        op.integrator("LoadControl", Size/80)
        ok = op.analyze(1)       
        
    if ok != 0:
        print("Trying 160 times smaller timestep at load factor", nn)
        op.integrator("LoadControl", Size/160)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 200 interations at load factor", nn)
        op.test('NormDispIncr', 1.*10**-8, 200)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying ModifiedNewton at load factor", nn)
        op.algorithm("ModifiedNewton")
        op.test('NormDispIncr', 1.*10**-8, 200)
        ok = op.analyze(1)

    op.test('NormDispIncr', 1.*10**-8, 50)
    op.integrator("LoadControl", Size)
    op.algorithm("Newton")
    return ok

def analysisLoopDisp(ok, nn, dx, ControlNode, ControlNodeDof):
    """
    The displacement control analysis loop.
    """
    
    if ok != 0:
        print("Trying 5 times smaller timestep at step", nn)
        op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx/5)
        ok = op.analyze(1)

    if ok != 0:
        print("Trying 20 times smaller timestep at step", nn)
        op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx/20)
        ok = op.analyze(1)        
        
    if ok != 0:
        print("Trying 80 times smaller timestep at step", nn)
        op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx/80)
        ok = op.analyze(1)       
        
    if ok != 0:
        print("Trying 160 times smaller timestep at step", nn)
        op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx/160)
        ok = op.analyze(1)

    if ok != 0:
        print("Trying 1000 times smaller timestep at step", nn)
        op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx/1000)
        ok = op.analyze(1)

                
    if ok != 0:
        print("Trying ModifiedNewton at load factor", nn)
        op.algorithm("ModifiedNewton")
        op.test('NormDispIncr', 1.*10**-6, 200)
        ok = op.analyze(1)

    op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx)
    op.algorithm("Newton")
    op.test('NormDispIncr', 1.*10**-10, 50)
    return ok


def analysisLoopArc(ok, nn, Size):
    scaleF = 0 # the force scale 
    if ok != 0:
        print("Trying 5 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/5, scaleF / 5)
        op.integrator("ArcLength", Size/5, scaleF)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 20 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/20, scaleF / 20)
        op.integrator('ArcLength', Size/20, scaleF)
        ok = op.analyze(1)        
        
    if ok != 0:
        print("Trying 80 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/80, scaleF / 80)
        op.integrator('ArcLength', Size/80, scaleF)
        ok = op.analyze(1)        
        
    if ok != 0:
        print("Trying 160 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/160, scaleF / 160)
        op.integrator('ArcLength', Size/160, scaleF)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 1000 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/1000, scaleF / 1000)
        op.integrator('ArcLength', Size/1000, scaleF)
        ok = op.analyze(1)

    if ok != 0:
        print("Trying increasing the number of iterations to 200", nn)
        op.test('NormDispIncr', 1.*10**-8, 200)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 5000 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/1000, scaleF / 1000)
        op.integrator('ArcLength', Size/5000, scaleF)
        ok = op.analyze(1)
        
    if ok != 0:
        print("Trying 20000 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/1000, scaleF / 1000)
        op.integrator('ArcLength', Size/20000, scaleF)
        ok = op.analyze(1)

        
    if ok != 0:
        print("Trying 500000 times smaller timestep at load factor", nn)
        # op.integrator('ArcLength', Size/50000, scaleF / 50000)
        op.integrator('ArcLength', Size/500000, scaleF)
        # op.integrator('ArcLength', Size/160, scaleF)
        ok = op.analyze(1)
                
    if ok != 0:
        print("Trying 200 interations at load factor", nn)
        op.test('NormDispIncr', 1.*10**-8, 200)
        ok = op.analyze(1)
                    
    # if ok != 0:
    #     print("Trying ModifiedNewton at load factor", nn)
    #     op.algorithm("ModifiedNewton")
    #     op.test('NormDispIncr', 1.*10**-8, 200)
    #     ok = op.analyze(1)
        
    op.test('NormDispIncr', 1.*10**-12, 50)
    op.integrator('ArcLength', Size, scaleF)
    op.algorithm("Newton")
    # op.algorithm('Broyden')

    return ok


# =============================================================================
# Load Control Analysis Types
# =============================================================================


def PushoverLcF(Nsteps):

    """
    Load control with force - not super useful because it can't get pas the load peak'
    """    

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
    op.test('NormDispIncr', 1.*10**-10, 50)
    
    # Run Analysis
    
    op.record()
    ok = op.analyze(Nsteps)


def PushoverLcD(dispMax, du = 0.00001*m):
    
    """
    Load control with displacement - easy to understand but will not preserve the initial load distribution if
    multiple 'sp' constraints are used on the structure.
    """        
    
    ControlNode = 4
    ControlNodeDof = 1
    
    # Define time series
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.sp(ControlNode, ControlNodeDof, du) # we will linearly increase increase displacement this step size
    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("LoadControl", 1)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    
    # Run Analysis
    op.record()
    StepSize = .1
    nn = 0
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1)
        
        if ok != 0:
            ok = analysisLoopBasic(ok, nn, StepSize)
            
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break
        nn =+ 1
                
    print()
    print("# Analysis Complete #")
    

def CyclicAnalysisLc(dispMax, fileName = 'protocols/Ganey_small.thf'):
    
    """
    Load control with displacement - easy to understand but will not preserve the initial load distribution if
    multiple 'sp' constraints are used on the structure.
    """             
    
    ControlNode = 4
    ControlNodeDof = 1
    du = 1.0*m
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    op.timeSeries('Path',3,  '-dt', 1.0, '-filePath', fileName ,  '-factor',  1.,  '-prependZero')
    
    # define loads
    op.pattern('Plain',1 , 3)
    op.sp(ControlNode, ControlNodeDof, du)
    
    
    StepSize = .1
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("LoadControl", StepSize, 1, StepSize, StepSize*100)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")
    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    
    # Run Analysis
    op.record()
    print('start')
    nn = 0
    times = []
    LF = []
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1.)
        # print(op.getTime())
        if ok != 0:
            ok = analysisLoopBasic(ok, nn, StepSize)
            
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break
        
        nn += 1
        times.append(op.getTime())
        LF.append(op.getLoadFactor(1))   
        
    print()
    print("# Analysis Complete #")
    return times, LF



# =============================================================================
# Displacement Control Analyses
# =============================================================================

def PushoverDcF(dispMax, du = 0.0002*m):
    
    """
    Displacement control with force. More finicky that force control but will handle most situations thrown at it.
    """            
    
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1*kN
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    # op.timeSeries('Linear', 2)
    
    # define loads
    op.pattern('Plain',1 , 1)
    op.load(ControlNode, dForce, 0., 0.)
    # op.sp(ControlNode, ControlNodeDof, du)

    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    # op.integrator("DisplacementControl", ControlNode, ControlNodeDof, du, 10, du/10000)
    op.integrator('DisplacementControl', ControlNode, ControlNodeDof, du, 10, du/100, du*10)    
    
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")
    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    
    # Run Analysis
    op.record()   
    nn = 0
    times = []
    LF = []    
    
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1.)
        
        # nn+=1
        if ok != 0:
            ok = analysisLoopDisp(ok, nn, du, ControlNode, ControlNodeDof)
        
        
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break            
            
        nn += 1
        times.append(op.getTime())
        LF.append(op.getLoadFactor(1))


def PushoverDcD(dispMax, du = 0.0001*m):
    
    """
    Displacement control with displacement. More finicky that force controll but will handle most situations thrown at it.
    Can capture load deterioration.
    """        
   
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1*kN
    
    # Define time series
    #  timeSeries('Constant', tag, '-factor', factor=1.0)
    op.timeSeries('Constant',1)
    
    # define loads
    op.pattern('Plain',1 , 1)
    # op.load(ControlNode, dForce, 0., 0.)
    op.sp(ControlNode, ControlNodeDof, 1.0)

    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator("DisplacementControl", ControlNode, ControlNodeDof, du, 10, du/10000)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    
    # Run Analysis
    op.record()   
    nn = 0
    times = []
    LF = []    
    
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1.)
            
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break            
            
        nn += 1
        times.append(op.getTime())
        LF.append(op.getLoadFactor(1))




def CyclicAnalysisDcL(loadProtocol = [0.02,0.05], Nrepeat = [2,2], dx = 0.0001*m):
    
    """
    Displacement control with displacement. More finicky that force controll but will handle most situations thrown at it.
    Can capture load deterioration.
    Figures out what change in force is needed to get a specific input
    """      
    
    ControlNode = 4
    ControlNodeDof = 1
    dForce = 1*kN # the reference load
    
    # Define time series
    op.timeSeries('Constant',1)

    # define loads
    op.pattern('Plain',1 , 1)
    op.load(ControlNode, dForce, 0., 0.)    
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")
    # Create Test
    op.test('NormDispIncr', 1.*10**-10, 50)
    
    # Run Analysis
    op.record()
    print('start')
    nn = 0
    for x, Ncycle in zip(loadProtocol, Nrepeat):
        
        # If the load protocol uses, then upate this term with 
        for ii in range(Ncycle):            
            op.integrator('DisplacementControl', ControlNode, ControlNodeDof, dx, 10, dx/1000, dx*10)
            while (op.nodeDisp(ControlNode, ControlNodeDof) < x):
                ok = op.analyze(1)
                nn+=1
                if ok != 0:
                    ok = analysisLoopDisp(ok, nn, dx, ControlNode, ControlNodeDof)
                if ok != 0:
                    print('Ending analysis')
                    op.wipe()
                    return
                
            # The negative cycle.
            op.integrator('DisplacementControl', ControlNode, ControlNodeDof, -dx, 10, -dx*10, -dx/1000)
            while (op.nodeDisp(ControlNode, ControlNodeDof) > -x):
                ok = op.analyze(1)
                nn+=1
                if ok != 0:
                    ok = analysisLoopDisp(ok, nn, -dx, ControlNode, ControlNodeDof)                
                
                if ok != 0:
                    print('Ending analysis')
                    
                    op.wipe()
                    return 
            print(x)
    print()
    print("# Analysis Complete #")

# =============================================================================
# Archlength
# =============================================================================
        
def PushoverArc(dispMax, darc= 0.001*m):
    
    ControlNode = 4
    ControlNodeDof = 1
    # dForce = 1*kN
    dForce = 1000
    
    # Define time series
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    
    # define loads
    op.pattern('Plain',1 , 2)
    op.sp(ControlNode, ControlNodeDof, darc)
    # op.sp(ControlNode, ControlNodeDof, dForce)

    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator('ArcLength', darc,  0.)
    # create algorithm
    op.algorithm("Newton")
    # create analysis object
    op.analysis("Static")

    # Create Test
    op.test('NormDispIncr', 1.*10**-8, 50)
    # Run Analysis
    op.record()
    nn = 0
    times = []
    LF = []    
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1.)
        print(op.nodeDisp(ControlNode, ControlNodeDof))
    
        if ok != 0:
            ok = analysisLoopArc(ok, nn, darc)
    
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break            
            
        nn += 1
        times.append(op.getTime())
        LF.append(op.getLoadFactor(1))
        




def CyclicAnalysisArc(dispMax, darc=0.00001*m, fileName = 'protocols/Ganey_smaller.thf'):
    
    ControlNode = 4
    ControlNodeDof = 1
    du = 1.0*m
    
    # Define time series
    op.timeSeries('Constant',1)
    op.timeSeries('Linear', 2)
    op.timeSeries('Path', 3, '-dt', 1.0, '-filePath',  fileName,  '-factor',  1.0,  '-prependZero')
    
    # define loads
    op.pattern('Plain',1 , 3)
    op.sp(ControlNode, ControlNodeDof, du)
    
    # Define Analysis Options
    # create SOE
    op.system("BandGeneral")
    # create DOF number
    op.numberer("Plain")
    # create constraint handler
    op.constraints("Transformation")
    # create integrator
    op.integrator('ArcLength', darc, 0.)
    # op.integrator('ArcLength', darc, 1)
    # create algorithm
    op.algorithm("Newton")
    # op.algorithm("ModifiedNewton")
    # create analysis object
    op.analysis("Static")
    # Create Test
    op.test('NormDispIncr', 1.*10**-12, 50)
    # op.test('NormUnbalance ', 1.*10**-10, 50)
    
    # Run Analysis
    op.record()
    print('start')
    nn = 0
    times = []
    LF = []
    changed =False
    while(op.nodeDisp(ControlNode, ControlNodeDof) < dispMax  ):       
    
        ok = op.analyze(1.)
        
        if ok != 0:
            ok = analysisLoopArc(ok, nn, darc)
            
        if ok != 0:
            print("Analysis failed at load factor:", nn)
            break
        
        nn += 1
        times.append(op.getTime())
        LF.append(op.getLoadFactor(1))   
        
    print()
    print("# Analysis Complete #")
    return times, LF

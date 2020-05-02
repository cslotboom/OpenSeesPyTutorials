# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 22:36:18 2020

@author: Christian

In this tutorial I overview how to use functions and OpenSeesPy. I show how to 


"""


import openseespy.opensees as op
from ModelFunctions import (GetSections,GetModel,GetRecordersPushover, 
                            RunPushoverAnalysis, RunGravityAnalysis)

import numpy as np

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


# =============================================================================
# Input Variables
# =============================================================================

A1 = 10.*inches**2
A2 = 5*inches**2

E = 3000*Ksi

Px = 100*kip
Py = -50*kip



# =============================================================================
# Run Analysis
# =============================================================================

analyisName = 'Pushover'

GetSections(E)
GetModel(A1,A2)
GetRecordersPushover(analyisName)
RunPushoverAnalysis(Px,Py)



analyisName = 'Gravity'

GetSections(E)
GetModel(A1,A2)
GetRecordersPushover(analyisName)
RunGravityAnalysis(Py)



# =============================================================================
# Area Optimization Analysis
# =============================================================================

targetDisp = -0.0075*m

lowerBound = 1*inches**2
upperBound = 20*inches**2

Narea = 20
trialAreas = np.linspace(lowerBound,upperBound,Narea)
outputDisp = np.zeros([Narea,Narea])


for ii, A1 in enumerate(trialAreas):
    for jj, A2 in enumerate(trialAreas):
        GetSections(E)
        GetModel(A1,A2)
        RunGravityAnalysis(Py)
        
        outputDisp[ii,jj] = op.nodeDisp(4,2)
        
        
        op.wipe()
        


shiftOutput = np.abs(outputDisp - targetDisp)
[[MinIndexA1] ,[MinIndexA2] ] = np.where(shiftOutput == np.min(shiftOutput))


A1Optimal = trialAreas[MinIndexA1]
A2Optimal = trialAreas[MinIndexA2]





analyisName = 'Optimal_Area_Analysis_'
GetSections(E)
GetModel(A1Optimal, A2Optimal)
GetRecordersPushover(analyisName)
RunPushoverAnalysis(Px,Py)

op.wipe()


# =============================================================================
# Run unknown number of analyses
# =============================================================================

# Redefine areas
A1 = 10.*inches**2
A2 = 5*inches**2

# Define target values
targetDisp = 0.001*m
growthRate = 1.01
tol = 10**-6

# Define the analysis name
AnalysisName = "Optimal_MOE_Pushover_"

# Run an inital Analysis 
GetSections(E)
GetModel(A1, A2)
GetRecordersPushover(AnalysisName)
RunGravityAnalysis(Py)

# Find the optimal E for our analysis
ii = 0
while ( abs(targetDisp - op.nodeDisp(4,1)) > tol ):
    
    print(op.nodeDisp(4,1))
    
    # Choose a new E
    if op.nodeDisp(4,1) < targetDisp:
        E = E/growthRate
    else:
        E = E*growthRate
    
    # Run a new analysis
    op.wipe()
    GetSections(E)
    GetModel(A1, A2)
    RunGravityAnalysis(Py)
    
    

    ii +=1

op.wipe()  

# Run analysis on Optimal Parameter
GetSections(E)
GetModel(A1, A2)
GetRecordersPushover(AnalysisName)
RunPushoverAnalysis(Px, Py)   
op.wipe()





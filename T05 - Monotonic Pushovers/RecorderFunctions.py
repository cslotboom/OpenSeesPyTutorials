



import openseespy.opensees as op

def getPushoverRecorders(OuputDirName, AnalysisName):
    
    baseName = OuputDirName + '\\' + AnalysisName
    
    op.recorder('Node', '-file', baseName + '_Top_Dsp.out', '-time', '-nodeRange', 4,4, '-dof', 1,2,3, 'disp')
    op.recorder('Node', '-file', baseName + '_Reactions.out', '-time', '-nodeRange', 1,1, '-dof', 1,2,3, 'reaction')
    
    
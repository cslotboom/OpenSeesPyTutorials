import matplotlib.pyplot as plt
import numpy as np



def plotPushover(OuputDirName, AnalysisName):
    
    baseName = 'outputs\\' + OuputDirName + '\\' + AnalysisName
    dispFileName = baseName + '_Top_Dsp.out'
    reactionFileName = baseName + '_Reactions.out'
    
    Disp = np.loadtxt(dispFileName, delimiter= ' ')
    Reactions = np.loadtxt(reactionFileName, delimiter= ' ')
    
    x = Disp[:, 1]
    shear = -Reactions[:, 1]
    
    
    fig, ax = plt.subplots()
    plt.plot(x, shear)
    
    return Disp, Reactions
    


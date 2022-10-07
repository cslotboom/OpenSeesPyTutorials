

import hysteresis as hys
import numpy as np

datay = np.loadtxt('Ganey_20.csv')
datax = np.arange(len(datay))

dataxy = np.column_stack([datax, datay])
dataHys = hys.Hysteresis(dataxy)

# dataHys.setReversalPoints()
dataHys.setReversalIndexes()

dataHys.recalculateCycles()
dataHys.setPeaks()
dataHys.plot(plotPeaks=True)

peaks = dataHys.getPeakxy()[:,1]

dumbyValues = np.ones_like(peaks)

curve = hys.Hysteresis([peaks, dumbyValues])
curve.cycles
newHys = hys.resampleDx(curve, 0.0001)
# hys.resampledx(curve, )


np.savetxt('Ganey_smaller.csv', newHys.x)
# curve.plotLoadProtocol()
# hysteresis.createProtocol(MonotonicProtocol, loadProtocolNcycles)



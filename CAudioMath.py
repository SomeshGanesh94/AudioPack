import numpy as np

class CAudioMath(object):

	def __init__(self):
		pass

	def convertToDB(self, signal):
		dBdata = 20 * np.log10(signal)
		return dBdata

	def shiftAboveZero(self, signal):
		minValue = float(abs(min(signal)) + 2)
		# minValue = 65536.
		shiftedValue = np.asarray([a + minValue + 1e-7 for a in signal])/minValue
		return shiftedValue

	def normalizeAudio(self, signal):
		maxValue = float(max(abs(signal)))
		newValue = signal/maxValue
		return newValue

	def getMovAvg(self, signal, windowSize = 200):
		sumVal = np.cumsum(signal, dtype=float)
		sumVal[windowSize:] = sumVal[windowSize:] - sumVal[:-windowSize]
		return sumVal[windowSize - 1:] / windowSize
from CAudioMath import *

class CAudioAlgo(object):

	def __init__(self):
		self.oAudioMath = CAudioMath()

	def getClicks(self, signal, windowSize=275, threshold=7, lookback=350, futureLook = 50):
		numSamples = len(signal)
		clicks = np.zeros(numSamples)
		clickIndices=[]

		movAvgSignal = self.oAudioMath.getMovAvg(signal, windowSize=350)

		for i in range(numSamples - futureLook):
			simMovAvg = movAvgSignal[i + futureLook - lookback]
			std = np.nanstd(signal[i:i+windowSize])
			maxValue = np.max(signal[i:i+windowSize])
			minValue = np.min(signal[i:i+windowSize])
			indexMax = np.argmax(signal[i:i+windowSize])
			indexMin = np.argmin(signal[i:i+windowSize])

			if(maxValue > simMovAvg + std * threshold):
				clickIndices.append(i+indexMax)
				clicks[i+indexMax] = 1
			elif(minValue < simMovAvg - std * threshold):
				clickIndices.append(i+indexMin)
				clicks[i+indexMin] = 1

		return clicks, clickIndices
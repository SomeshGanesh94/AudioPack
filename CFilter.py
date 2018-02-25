
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import numpy as np

class CFilter(object):

	def __init__(self):
		pass

	def getButterBandpassCoefficients(self, f1, f2, fs, order=10):
		low_freq = float(f1 * 2 / fs)
		high_freq = float(f2 * 2 / fs)
		return np.asarray(butter(order, [low_freq, high_freq], btype='band'))

	def applyFilter(self, signal, coefficients):
		return lfilter(coefficients[0], coefficients[1], signal)

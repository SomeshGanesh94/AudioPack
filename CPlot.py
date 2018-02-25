"""Plot class
"""
import matplotlib.pyplot as plt 


class CPlot(object):

	def __init__(self):
		pass

	def timePlot(self, signal, xlabel='Samples', ylabel='Amplitude', title='Time domain'):
		plt.figure()
		plt.plot(signal)
		plt.title(title)
		plt.ylabel(ylabel)
		plt.xlabel(xlabel)
		plt.tight_layout()
		plt.show()

	def clicksWithSignal(self, signal, clicks, xlabel='Samples', ylabel='Amplitude', title='Clicks in time domain'):
		plt.figure()
		plt.subplot(211)
		plt.plot(signal)
		plt.tight_layout()

		plt.subplot(212)
		plt.plot(clicks)
		plt.tight_layout()
		plt.show()



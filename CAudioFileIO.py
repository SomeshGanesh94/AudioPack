"""Audio file IO class
"""
import numpy as np
from scipy.io.wavfile import read
import aifc
from os.path import splitext

class CAudioFileIO(object):

	def __init__(self):
		self.data = np.zeros(())
		self.sampleRate = None
		self.fileExtension = None

	def setData(self, data):
		self.data = data

	def getData(self):
		return self.data

	def setSampleRate(self, sampleRate):
		self.sampleRate = sampleRate

	def getSampleRate(self):
		return self.sampleRate

	def getFileExtension(self):
		return self.fileExtension

	def setAudioObject(self, newObject):
		self = newObject

	def getAudioObject(self):
		return object

	def readAudio(self, filePath):
		fileName, fileExtension = splitext(filePath)
		self.fileExtension = fileExtension

		if self.fileType == '.wav':
			self.sampleRate, self.data = read(filePath)

		elif self.fileType == '.aif':
			file = aifc.open(filePath)
			self.sampleRate = file.getframerate()
			numFrames = file.getnframes()
			self.data = file.readframes(numFrames)
			file.close()

		elif self.fileType == '.pcm':
			rawData = np.memmap(filePath, dtype='h', mode='r')
			self.data = np.asarray(rawData)

		else:
			raise AttributeError("Invalid file type")



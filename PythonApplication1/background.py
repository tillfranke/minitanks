
import pygame
import time
import numpy.random as random
import numpy as np
class Mountain():
	def __init__(self,size):
		(X,Y) = size
		self.SIZE=size
		rise = random.normal(0.5, size = X/2)
		fall = random.normal(-0.5, size=X/2) 
		self.terrain = np.cumsum(np.concatenate([rise,fall])) + Y/10
	def draw(SCREEN):
		(X,Y) = self.SIZE
		for x in range(X):
			
		
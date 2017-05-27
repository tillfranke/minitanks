
import pygame
import time
import numpy.random as random
import numpy as np
from pprint import pprint
class Mountain():
	def __init__(self,size):
		(X,Y) = size
		self.SIZE=size
		rise = random.normal(0.5, size = int(X/2))
		fall = random.normal(-0.5, size = int(X/2)) 
		self.terrain = Y-(np.cumsum(np.concatenate([rise,fall])) + Y/10).astype(int)
		self.color = np.ones(3,int) * random.randint(90,127) # gray

	def render(self):
		bg = pygame.Surface(self.SIZE)
		(X,Y) = self.SIZE
		for x in range(X):
			pprint((x,self.terrain[x]),)
			pygame.draw.line(bg,self.color,(x,Y),(x,self.terrain[x]))
		return bg
		
import pygame
from math import pi,sin,cos
import numpy.random as random
from tank import SIZE as TANKSIZE, SIZE2 as TANKSIZE2
import time
SIZE=8
SIZE2=int(SIZE/2)
G=9.81
PI180 = pi/180
DWIND=0.1 # speed change from 1 m/s wind
class Shell(object):
	"""description of class"""
	def __init__(self,tank, wind):
		self.tank = tank
		alpha = self.tank.alpha * PI180 # convert to radians
		v0 = self.tank.v0
		self.wind = wind
		self.color=(0,128,0)
		self.dx = cos(alpha) * v0 * self.tank.direction
		self.dy = sin(alpha) * v0
		print("dx=",self.dx," dy=",self.dy)
		self.x0 = self.tank.x+ TANKSIZE2
		self.y0 = self.tank.y-TANKSIZE
		self.surface = pygame.Surface([SIZE,SIZE])
		pygame.draw.circle(self.surface, self.color, (SIZE2,SIZE2), SIZE2-1)
	def animate(self, screen, mountain, t):
		(X,Y) = screen.get_size()
		dx = self.dx - t*DWIND*self.wind
		dy = self.dy - t* G
		x = int(self.x0 + t*dx)
		y = int(self.y0 - t*dy)
		terrain=mountain.terrain[x]
		print("dt=",t," x=",x," y=",y, "terrain=",terrain," dx=",dx," dy=",dy)
		screen.blit(self.surface, (x,y))
		if  (0 <= y + SIZE2 <= terrain) and (0 <= x+SIZE2 < X ):
			return True
		else:
			if (y+SIZE2 >= terrain):
				self.explode(x,y,screen)
			return False
		return True

	def explode(self, x,y, screen):
		explosion_time = 0
		ESIZE=150
		explosion_image = pygame.Surface((ESIZE,ESIZE))
		explosion_image.fill(pygame.color.Color("white"))
		explosion_image.set_colorkey(pygame.color.Color("white"))
		rect = explosion_image.get_rect()
		rect.center = (x,y)
		for i in range(200):
			print("explode({} @ ({},{})".format(i,x,y))
			explosion_color = (random.randint(100,255),0,0,random.randint(100,150))
			explosion_radius = random.randint(0, 30) + 2
			explosion_position = (random.randint(-15,15) + ESIZE//2  , random.randint(-15,15) + ESIZE//2)
			pygame.draw.circle(explosion_image, explosion_color, explosion_position, explosion_radius)
			screen.blit(explosion_image,(x-ESIZE//2,y-ESIZE//2))
			pygame.display.flip()


import pygame


SIZE=20
SIZE2=int(SIZE/2)
(LEFT,RIGHT)=(1,-1)
class Tank(object):
	"""description of class"""
	def __init__(self, x, direction, mountain):
		assert direction in (LEFT,RIGHT)
		self.direction = direction
		self.x = x
		self.y = int(mountain.terrain[x-SIZE2:x+SIZE2 ].mean())
		self.alpha = 45
		self.v0 = 100
		self.health = 100
		mountain.terrain[x-SIZE2:x+SIZE2 ] = self.y+1
	def draw(self, screen):
		s = pygame.Surface([SIZE,SIZE])
		pygame.draw.line(s,(127,0,0),(0, SIZE-1),(SIZE-1,SIZE-1),2)
		screen.blit(s,(self.x-SIZE2, self.y-SIZE) )


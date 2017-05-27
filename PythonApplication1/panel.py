import pygame
LETTERSIZE=30
FONT='comicsansms'
class Panel(object):
	"""description of class"""
	def __init__(self, tank):
		self.font = pygame.font.Font(pygame.font.match_font(FONT), LETTERSIZE)
		self.tank = tank
		self.color = (128, 128+tank.direction*50, 128-tank.direction*50) 
	def draw(self, wind, screen):
		text="v0={} α={} w={}".format(self.tank.v0, self.tank.alpha, wind)
		s = self.font.render(text, True, self.color)
		xpos = screen.get_width()/2 
		xpos -= s.get_width() + LETTERSIZE if self.tank.direction < 0 else - LETTERSIZE
		screen.blit(s, (xpos,10))
	def handle(self,e):
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_UP:
				self.tank.v0 += 5
			if e.key == pygame.K_DOWN:
				self.tank.v0 -= 5
			if e.key == pygame.K_LEFT:
				self.tank.alpha += 5
			if e.key == pygame.K_RIGHT:
				self.tank.alpha -= 5



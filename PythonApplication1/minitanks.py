import pygame 
import time
from background  import Mountain
from tank import Tank, LEFT, RIGHT
from shell import Shell
import numpy.random as random
from panel import Panel

FPS=60

X=800
Y=600

def main():
	CLOCK = None
	SIZE=(X,Y)

	pygame.init()
	SCREEN = pygame.display.set_mode(SIZE)
	CLOCK = pygame.time.Clock()

	SIZE=pygame.display.get_surface().get_size()
	background = Mountain(SIZE)
	tanks = [ Tank(int(X * (0.5 - 0.4*(max(-1, min(1,random.normal(direction)) )))), direction, background) for direction in (LEFT,RIGHT)]
	bg = background.render()
	print("blitting background")


	wind = random.randint(-10,10)
	running = True
	player = 0
	while running:
		t = tanks[player]
		print("blitting tank  ",t.direction, " x=",t.x, " y=",t.y)
		wind += random.randint(-2,2)
		t.draw(bg)
		panel = Panel(t)
		aiming = True
		while running and aiming:
			for e in  pygame.event.get():
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:
						running = False
					if e.key == pygame.K_SPACE:
						aiming = False
				panel.handle(e)
			SCREEN.blit(bg,(0,0))
			panel.draw( wind, SCREEN)
			pygame.display.flip()

		if running:
			dt = 0
			s = Shell(t, wind = 10)
			shot = True
			while shot:
				SCREEN.blit(bg,(0,0))
				shot = s.animate(SCREEN,background, dt)
				pygame.display.flip()
				dt += 0.05
				CLOCK.tick(FPS)
			player = 1 - player


	pygame.display.quit()

if __name__ == "__main__":
	main()

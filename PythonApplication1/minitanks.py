import pygame 
import time
from background  import Mountain
X=800
Y=600
SIZE=(X,Y)
CLOCK = None
SCREEN = None

FPS=30
def main():
	pygame.init()
	global SCREEN
	SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	SIZE=pygame.display.get_surface().get_size()
	SCREEN = pygame.display.set_mode(SIZE)
	background = Mountain(SCREEN,SIZE)



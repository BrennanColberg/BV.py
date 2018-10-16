# module imports
import pygame
import math
# other files in project
from entities import *
from colors import *

# game variables
objects = set()
objects.add(Ship(10, 10))

# starting game
done = False
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()

# game loop
while not done:
	# TPS/FPS rate
	clock.tick(60)
	# quitting test loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	# game logic
	for item in objects:
		for child in item.children:
			child.tick()
		item.tick()
	# clearing screen
	screen.fill(WHITE)
	# drawing code!
	for item in objects:
		for child in item.children:
			child.render(screen)
		item.render(screen)
	# displaying drawing
	pygame.display.flip()

# stop game
pygame.quit()
# module imports
import pygame
import math
# other files in project
from entities import *
from colors import *

# game variables
objects = set()
objects.add(Player([0, 0], [1, 0.5]))

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
	
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			for item in objects:
				item.keyInput(event, True)
		elif event.type == pygame.KEYUP:
			for item in objects:
				item.keyInput(event, False)

	# game logic
	for item in objects:
		for child in item.children:
			child.tick()
		item.tick()
	
	# clear screen
	screen.fill(WHITE)
	# render objects
	for item in objects:
		for child in item.children:
			child.render(screen)
		item.render(screen)
	# display new screen
	pygame.display.flip()

# stop game
pygame.quit()
# module imports
import pygame
import math
# other files in project
from entities import *
from colors import *
import renderer

# game variables
objects = set()
# init player
player = Player([100, 100], 0, 3)
objects.add(player)
renderer.center = player.pos
# add blob
objects.add(Blob([0, 0], 10))

# starting game
done = False
pygame.init()
size = (700, 500)
renderer.screen = pygame.display.set_mode(size)
renderer.offset = [350, 250]
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
	renderer.screen.fill(WHITE)
	# render objects
	for item in objects:
		for child in item.children:
			child.render()
		item.render()
	# display new screen
	pygame.display.flip()

# stop game
pygame.quit()
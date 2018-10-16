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
	# quitting test loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	# game logic
	for item in objects:
		item.tick()
		for child in item.children:
			child.tick()
	# clearing screen
	screen.fill(WHITE)
	# drawing code!
	for item in objects:
		item.render(screen)
		for child in item.children:
			child.render(screen)
	# displaying drawing
	pygame.display.flip()
	# delaying
	clock.tick(60)

# stop game
pygame.quit()
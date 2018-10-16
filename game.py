import pygame
import math

pygame.init()

done = False
RED = (255, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()

x, y = 10, 10

while not done:
	# quitting test loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# game logic
	x += 2
	y += 1
	
	# clearing screen
	screen.fill(WHITE)
	# drawing code!
	pygame.draw.rect(screen, RED, [x, y, 30, 40])
	# displaying drawing
	pygame.display.flip()
	
	# delaying!
	clock.tick(60)

pygame.quit()
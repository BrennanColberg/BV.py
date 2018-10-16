import pygame
from colors import * 

class Ship:
	
	x = 0
	y = 0
	
	def __init__(self, x, y):
		self.x = x;
		self.y = y;
		pass
	
	def tick(self):
		self.x += 1
		self.y += 2
		pass
	
	def render(self, screen):
		pygame.draw.rect(screen, GREEN, [self.x, self.y, 40, 40], 0)
		pass
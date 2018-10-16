import pygame
import random
from colors import * 

class Entity:
	
	# things connected to entity that die with it (projectiles, etc)
	children = set()
	# position
	x = 0
	y = 0
	
	def __init__(self, x, y):
		self.x = x;
		self.y = y;
		
	def tick(self):
		pass
	def render(self, screen):
		pass

class Ship(Entity):
	
	def __init__(self, x, y):
		Entity.__init__(self, x, y)
	
	def tick(self):
		self.x += 1
		self.y += 2
		if random.random() < 0.1:
			self.fire(random.uniform(1, 5), random.uniform(-0.1, 0.1))
		
	def render(self, screen):
		pygame.draw.rect(screen, GREEN, [int(self.x), int(self.y), 40, 40], 0)
		
	def fire(self, vx, vy):
		self.children.add(Projectile(self, vx, vy))

class Projectile(Entity):
	
	vx = 0
	vy = 0
	
	def __init__(self, parent, vx, vy):
		Entity.__init__(self, parent.x, parent.y)
		self.vx = vx
		self.vy = vy
		
	def tick(self):
		self.x += self.vx
		self.y += self.vy
		
	def render(self, screen):
		pygame.draw.circle(screen, RED, [int(self.x), int(self.y)], 5, 1)

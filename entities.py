import pygame
import math
import random
from colors import * 

class Entity:
	
	# things connected to entity that die with it (projectiles, etc)
	children = set()
	# position
	pos = [0, 0] # x, y
	vel = [0, 0] # heading, speed
	
	def __init__(self, pos, vel):
		self.pos = pos;
		self.vel = vel;
		
	def keyInput(self, event, pressed):
		pass
	
	def tick(self):
		heading = self.vel[0]
		speed = self.vel[1]
		self.pos[0] += speed * math.cos(heading)
		self.pos[1] += speed * math.sin(heading)
		
	def render(self, screen):
		pass
	

class Ship(Entity):
		
	def fire(self, speed):
		self.children.add(Projectile(self, speed))
		
		
class Player(Ship):
	
	def keyInput(self, event, pressed):
		if pressed:
			if event.key == pygame.K_SPACE:
				self.fire(4)
	
	def render(self, screen):
		x = int(self.pos[0])
		y = int(self.pos[1])
		rect = pygame.Rect(x, y, 20, 20)
		pygame.draw.rect(screen, RED, rect)
		

class Projectile(Entity):
	
	def __init__(self, parent, speed):
		pos = parent.pos.copy()
		vel = parent.vel.copy()
		vel[1] = speed
		Entity.__init__(self, pos, vel)
		
	def render(self, screen):
		x = int(self.pos[0])
		y = int(self.pos[1])
		pygame.draw.circle(screen, RED, (x, y), 5, 1)

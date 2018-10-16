import pygame
import math
import random
# other project sources
import renderer
from colors import * 


class Entity:
	
	# things connected to entity that die with it (projectiles, etc)
	children = set()
	# position
	pos = [0, 0] # x, y
	heading = 0
	speed = 0
	
	def __init__(self, pos, heading, speed):
		self.pos = pos
		self.heading = heading
		self.speed = speed
		
	def keyInput(self, event, pressed):
		pass
	
	def tick(self):
		self.pos[0] += self.speed * math.cos(self.heading)
		self.pos[1] += self.speed * math.sin(self.heading)
		
	def render(self):
		pass
	
class Blob(Entity):
	
	size = None
	
	def __init__(self, pos, size):
		Entity.__init__(self, pos, 0, 0)
		self.size = size
		
	def render(self):
		pygame.draw.circle(renderer.screen, GREEN, renderer.screenCoords(self.pos), 10)

class Ship(Entity):
		
	def fire(self, speed):
		self.children.add(Projectile(self, speed))
		
		
class Player(Ship):
	
	def keyInput(self, event, pressed):
		if pressed:
			if event.key == pygame.K_SPACE:
				self.fire(4)
				
	def tick(self):
		
		# points velocity towards mouse position
		mousepos = renderer.worldCoords(pygame.mouse.get_pos())
		dx = self.pos[0] - mousepos[0]
		dy = self.pos[1] - mousepos[1]
		self.heading = math.atan2(dy, dx) + math.pi
		
		# parent calculations (physics etc)
		Entity.tick(self)
	
	def render(self):
		pos = renderer.screenCoords(self.pos)
		rect = pygame.Rect(pos, [20, 20])
		pygame.draw.rect(renderer.screen, RED, rect)
		

class Projectile(Entity):
	
	def __init__(self, parent, speed):
		pos = parent.pos.copy()
		speed += parent.speed
		heading = parent.heading
		Entity.__init__(self, pos, heading, speed)
		
	def render(self):
		pygame.draw.circle(renderer.screen, BLUE, renderer.screenCoords(self.pos), 5, 1)

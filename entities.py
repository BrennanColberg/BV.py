import pygame
import math
import random
from shapely.geometry import Polygon, box
# other project sources
import renderer
from colors import * 


class Entity:
	
	# things connected to entity that die with it (projectiles, etc)
	children = set()
	# display
	shape = None
	size = 10
	color = RED
	stroke = 0
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
		if self.shape != None:
			renderer.draw(self.pos, self.heading, 
						  self.shape, self.size, self.color, self.stroke)
	
class Blob(Entity):
	
	def __init__(self, pos, size):
		Entity.__init__(self, pos, 0, 0);
		# rendering
		self.size = 15
		self.shape = Polygon([
			(1, 0),
			(0, -1),
			(-1, 0),
			(0, 1)
		])

		
class Ship(Entity):
		
	def fire(self, speed):
		self.children.add(Projectile(self, speed))
		
		
class Player(Ship):
	
	def __init__(self, pos, heading, speed):
		Entity.__init__(self, pos, heading, speed)
		# rendering
		self.size = 15
		self.color = BLUE
		self.stroke = 5
		self.shape = Polygon([
			(1, 0),
			(-1, 1),
			(-1, -1)
		])
	
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
		

class Projectile(Entity):
	
	def __init__(self, parent, speed):
		# kinematics
		self.pos = parent.pos.copy()
		self.heading = parent.heading
		self.speed += parent.speed + speed
		# rendering
		self.size = 3
		self.color = BLUE
		self.shape = box(-1, -0.1, 1, 0.1)

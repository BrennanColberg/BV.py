import pygame
from shapely import affinity

screen = None
center = [0, 0]
offset = [0, 0]

def screenCoords(pos):
	x = int(pos[0] - center[0] + offset[0])
	y = int(pos[1] - center[1] + offset[1])
	return [x, y]

def worldCoords(pos):
	x = int(pos[0] + center[0] - offset[0])
	y = int(pos[1] + center[1] - offset[1])
	return [x, y]

def draw(pos, angle, polygon, size, color, width=0):
	polygon = affinity.rotate(polygon, angle, 'centroid', True)
	polygon = affinity.scale(polygon, size, size, size, 'centroid')
	pointlist = list(polygon.exterior.coords)
	centroid = polygon.centroid
	for i, point in enumerate(pointlist):
		screenPoint = screenCoords([
			point[0] - centroid.x + pos[0],
			point[1] - centroid.y + pos[1]
		])
		pointlist[i] = (screenPoint[0], screenPoint[1])
	pygame.draw.polygon(screen, color, pointlist, width)
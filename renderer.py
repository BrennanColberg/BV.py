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
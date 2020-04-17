from obstacle import Obstacle

class Map:
	def __init__(self, width, height):
		row = [0] * (width + 1)
		map = []
		for i in range(height + 1):
			map.append(row)
			
		self.map = map
		self.width = width
		self.height = height
		
		self.obstacles = []
		
	def add_obstacle(self, x, y):
		self.map[x][y] = 1
		self.obstacles.append(Obstacle(x, y))
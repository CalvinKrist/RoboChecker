class Obstacle:
	counter = 0
	def __init__(self, x, y):
		# Numeric location of the obstacle
		self.xVal = x
		self.yVal = y
		
		# String labels for the obstacles x and y variables
		self.x = "ox" + str(Obstacle.counter)
		self.y = "oy" + str(Obstacle.counter)
		Obstacle.counter += 1
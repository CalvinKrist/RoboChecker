from map import Map
from obstacle import Obstacle

class LabelGenerator:

	# The names of the variables for robot position
	x = "x2"
	y = "y2"
	
	# Names of width and height variables
	w = "w"
	h = "h"
	
	# Takes in a map, which is a 2D array where each value is
	# either 0 (passable) or 1 (impassable). 
	# Grid is accessed using x,y formatting.
	# 
	# Possible positions are assumed to be 1 indexed
	def __init__(self):
		self.x = LabelGenerator.x
		self.y = LabelGenerator.y
		
		self.w = LabelGenerator.w
		self.h = LabelGenerator.h
		
	# Returns a label showing if its possible to traverse
	# a certain path. Calculated by checking if each delta 
	# along the path is valid
	#
	# Path: list of delta tuples, eg [(dx1, dy1), (dx2, dy2)]
	def isPathValid(self, path):
		label = "(" + self.isDeltaValid(path[0][0], path[0][1]) + ")"
		del path[0]
		
		for delta in path:
			label += " & (" + self.isDeltaValid(delta[0], delta[1]) + ")"
			
		return label
		
	# Returns a label for if the 
	# point (x+dx, y+dy) is in bounds.
	# If width=10, height=10, 
	# assumes (10,10) is valid and (0,0) isn't
	def isDeltaValid(self, dx, dy):
		if(dx > 0):
			numXMovement = self.w + "-" + self.x
			canMoveX = numXMovement + " >= " + str(abs(dx))
		else:
			numXMovement = self.x + str(dx)
			if(dx == 0):
				numXMovement = self.x
			canMoveX = numXMovement + " > 0"
		
		if(dy > 0):
			numYMovement = self.h + "-" + self.y
			canMoveY = numYMovement + " >= " + str(abs(dy))
		else:
			numYMovement = self.y + str(dy)
			if(dy == 0):
				numYMovement = self.y
			canMoveY = numYMovement + " > 0"
		
		return "(" + canMoveX + ") & (" + canMoveY + ")" 
		
	# Used to generate an equation for avoiding obstacles
	# on the map when a certain path is followed
	#
	# Obstacles are grid values of 1
	# The path is a list of tuples in the form [(dx1, dy1), (dx2, dy2)...]
	def getObstacleAvoidanceEq(self, map, path):
		if len(map.obstacles) == 0:
			return "true"

		path_equations = []
		for delta in path:
			xOff = ""
			if delta[0] > 0:
				xOff = "+" + str(delta[0])
			elif delta[0] < 0:
				xOff = str(delta[0])
				
			yOff = ""
			if delta[1] > 0:
				yOff = "+" + str(delta[1])
			elif delta[1] < 0:
				yOff = str(delta[1])
				
			terms = []
			for obstacle in map.obstacles:
				xTerm = self.x + xOff + "=" + obstacle.x
				yTerm = self.y + yOff + "=" + obstacle.y
				term  = "!(" + xTerm + " & " + yTerm + ")"
				terms.append(term)
				
			pathEq = terms[0]
			del terms[0]
			for term in terms:
				pathEq += " & " + term
				
			path_equations.append(pathEq)
				
		eq = path_equations[0]
		del path_equations[0]
		for path_eq in path_equations:
			eq += " & " + path_eq
			
		return eq
			

if __name__ == "__main__":
	gen = LabelGenerator()
	
	print(gen.isDeltaValid(2, 4))
	# (w-x2 >= 2) & (h-y2 >= 4)
	print(gen.isDeltaValid(-2, 4))
	# (x2-2 > 0) & (h-y2 >= 4)
	print(gen.isDeltaValid(-2, -4))
	# (x2-2 > 0) & (y2-4 > 0)
	print(gen.isDeltaValid(2, -4))
	# (w-x2 >= 2) & (y2-4 > 0)
	
	path = [(1, 2), (4, 5), (7, 8)]
	print(gen.isPathValid(path))
	# ((w-x2 >= 1) & (h-y2 >= 2)) & ((w-x2 >= 4) & (h-y2 >= 5)) & ((w-x2 >= 7) & (h-y2 >= 8))

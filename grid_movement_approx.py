import math 
from label_generator import LabelGenerator
from map import Map
import copy

# Returns 'number' precomputed angles
# evenly distributed between [0 and 2pi)
def get_angles(number):
	inc = (2 * math.pi) / (number)
	
	vals = []
	for i in range(0, number):
		vals.append(i * inc)
		
	return vals
	
# Given an angle and a move speed, calculates rounded delta 
# over x and y returns a (dx, dy), where dx and dy have been 
# rounded to tile size. Value assume standard cartesian plane.
# 
# angle: an angle in radians
# move_speed: speed in number of tiles, eg 10 = 10 tiles
def calculte_delta(angle, move_speed):

	dx = move_speed * math.cos(angle)
	dy = move_speed * math.sin(angle)
			
	# Round each variable to the nearest whole number / tile
	if(dx >= 0):
		dx = math.floor(dx + 0.5)
	else:
		dx = math.ceil(dx - 0.5)
	if(dy >= 0):
		dy = math.floor(dy + 0.5)
	else:
		dy = math.ceil(dy - 0.5)
	
	return (dx, dy)
	
class GridMovementApproximation:
	counter = 0
	def __init__(self, angle, move_speed, map):
		self.name = "A" + str(GridMovementApproximation.counter)
		GridMovementApproximation.counter += 1
		
		self.angle = angle
		self.speed = move_speed
		self.delta = calculte_delta(angle, move_speed)
		
		# Calculate approximate list of tiles we pass through
		# if the delta is applied by checking tiles for every
		# move speed lest than move_speed, adding them all to
		# a set
		self.passed = set()
		for i in range(1, move_speed):
			delta = calculte_delta(angle, i)
			self.passed.add(delta)
			
		if self.delta in self.passed:
			self.passed.remove(self.delta)
			
		self.labelGenerator = LabelGenerator()
		
		path = list(self.passed.copy())
		path.append(self.delta)
		
		self.moveFormula = "move" + self.name
		self.moveForumaText = "formula move" + self.name + " = " + self.labelGenerator.isPathValid(copy.copy(path)) + ";"
		
		self.obstacleFormula = "collide" + self.name
		self.obstacleFormulaTest = "formula collide" + self.name + " = " + self.labelGenerator.getObstacleAvoidanceEq(map, copy.copy(path)) + ";"
			
	def __str__(self):
		out =  "name: " + self.name + "\n"
		out += "angle: " + str(self.angle) + "\n"
		out += "speed: " + str(self.speed) + "\n"
		out += "delta: " + str(self.delta) + "\n"
		out += "passed: " + str(self.passed) + "\n"
		out += "label: " + self.moveForumaText + "\n"
		out += "obstacle formula: " + self.obstacleFormulaTest + "\n";
		return out

if __name__ == "__main__":
	angles = get_angles(4)
	
	map = Map(10, 10)
	map.add_obstacle(0, 9)
	map.add_obstacle(1, 9)
	
	approximations = []
	for angle in angles:
		approximations.append(GridMovementApproximation(angle, 1, map))
		
	for approx in approximations:
		print(approx)
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
		
		# Calculate the path for the movement
		delta_list = []
		for i in range(1, move_speed + 1):
			delta = calculte_delta(angle, i)
			delta_list.append(delta)
			
		self.path = []
		x = 0
		y = 0
		for i in range(len(delta_list)):
			delta = delta_list[i]
			self.path.append((delta[0] - x, delta[1] - y))
			x = delta[0]
			y = delta[1]
			
		self.labelGenerator = LabelGenerator()
		
		self.move_formulas = {}
		i = 0
		for delta in self.path:
			moveFormula = "move" + self.name + str(i)
			moveForumaText = "formula " + moveFormula + " = " + self.labelGenerator.isDeltaValid(delta[0], delta[1]) + ";"
			self.move_formulas[moveFormula] = moveForumaText;
			i+=1
		
		self.obstacle_formulas = {}
		i = 0
		for delta in self.path:
			path_copy = list(self.path.copy())
			obstacleFormula = "collide" + self.name + str(i)
			obstacleFormulaTest = "formula " + obstacleFormula + " = " + self.labelGenerator.getObstacleAvoidanceEq(map, [path_copy[i]]) + ";"
			self.obstacle_formulas[obstacleFormula] = obstacleFormulaTest;
			i += 1
			
	def __str__(self):
		out =  "name: " + self.name + "\n"
		out += "angle: " + str(self.angle) + "\n"
		out += "speed: " + str(self.speed) + "\n"
		out += "delta: " + str(self.delta) + "\n"
		out += "path: " + str(self.path) + "\n"
		out += "move formulas: " + str(self.move_formulas) + "\n"
		out += "obstacle formulas: " + str(self.obstacle_formulas) + "\n"
		return out

if __name__ == "__main__":
	angles = get_angles(7)
	
	map = Map(10, 10)
	#map.add_obstacle(0, 9)
	#map.add_obstacle(1, 9)
	
	approximations = []
	for angle in angles:
		approximations.append(GridMovementApproximation(angle, 4, map))
		
	for approx in approximations:
		print(approx)
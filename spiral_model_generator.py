#spiral approximation
from label_generator import LabelGenerator
from coverage_tracker import CoverageTracker
from grid_movement_approx import GridMovementApproximation
from map import *
import copy
import sys
from model_generator import ModelGenerator

import math 
from archimedean_spiral import ArchimedeanSpiral, Point



class SpiralModelGenerator(ModelGenerator):

 
 
 # No changes thus far
	def __init__(self, map, num_angles=4, move_speed=1, tracker=None):
		super().__init__(map, num_angles, move_speed, tracker)
		


	def __str__(self):
		model = "mdp\n\n"

		model += "//CONSTANTS\n"
		model += "const int " + LabelGenerator.w + " = " + str(self.map.width) + ";\n"
		model += "const int " + LabelGenerator.h + " = " + str(self.map.height) + ";\n\n"

		model += "//Formulas for checking if movement along an angle is in bounds\n"
		for approx in self.approximations:
			for formula_name, formula in approx.move_formulas.items():
				model += formula + "\n";
			model += "\n"
		model += "\n"
		
		model += "//Formula for checking if movement along an angle collides with obstacles\n"
		for approx in self.approximations:
			for formula_name, formula in approx.obstacle_formulas.items():
				model += formula + "\n";
			model += "\n"
		model += "\n"

		model += "module spiral_robot\n\n"

		#Add model states and variables
		states =  LabelGenerator.x + " : [1.." + str(self.map.width) + "] init " + str(self.map.spawn_x) +	"; // robot x position\n"
		states += LabelGenerator.y + " : [1.." + str(self.map.height) + "] init " + str(self.map.spawn_y) + "; // robot y position\n"
		states += "dir : [0.." + str(len(self.approximations)-1) + "] init 1; // possible robot directions\n"
		states += "spiral : [0.." + str(math.floor(self.map.width * self.map.height/2)) + "] init 0; //step of spiral\n"
		states += "mode: bool init true; //robot is spiralling: T is yes, F is random\n"
		states += "diameter : [0.." + str(self.map.width) +"] init 0; // diamter of current spiral or left to go before spiralling\n"
		states += "counter : [0.." + str(self.speed) +"] init 0; // if the robot is moving\n"
		
		states += "\n"
		
		states+= "//switching to spiral mode"
		states+= "[] (diameter=0 & !mode) -> 1 : (mode'= true); \n \n"
		
		# Setup main coverageTest variable to add to transitions
		coverageTest = ""
		if(self.tracker != None):
			states += "//Add tracking variables:\n"
			states += self.tracker.variables
			coverageTest = "checkLoc=0 & "

#&checkLoc=0 & dir=15 & moveA150 & collideA150
		states += "// Movement transitions when robot can move in random mode\n"
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			# Add boolean state specifier for enterng 'move' mode
			#states += "[] (dir=" + str(i) + " & " + list(approx.move_formulas.keys())[0] + " & " + list(approx.obstacle_formulas.keys())[0] + ") -> 1 : (counter'=0);\n"
			
			# Add state specifiers for each stage of movement
			for j in range(self.speed):
				states += "[] (diameter>0 & !mode &"+coverageTest+"dir=" + str(i) + " & " + list(approx.move_formulas.keys())[j] + " & " + list(approx.obstacle_formulas.keys())[j] + " & counter=" + str(j) + ") -> 1 : (counter'=mod(counter+1,"+str(self.speed)+")) & (diameter'=diameter-1) & "
			
				# Add how x state changes
				delta = approx.path[j]
				states += "(" + LabelGenerator.x + "'=" + LabelGenerator.x;
				if delta[0] > 0:
					states += "+" + str(delta[0])
				elif delta[0] < 0:
					states += "-" + str(abs(delta[0]))
				# Add how y state changes
				states += ") & (" + LabelGenerator.y + "'=" + LabelGenerator.y;
				if delta[1] > 0:
					states += "+" + str(delta[1])
				elif approx.delta[1] < 0:
					states += "-" + str(abs(delta[1]))
				# Set tracking variable if tracking
				if self.tracker != None:
					states+=") & (checkLoc'=1"
				states += ");\n"
			states += "\n"
		if self.tracker != None:
			states += "\n// Update coverage if checking for location\n"
			states += self.tracker.transitions




		states+= "//Movement transitions when robot can move and is in spiral mode\n"
		total_travelled=0.0
		step=0
		spiral_path =[]
		diameter_list=[]
		last_point = Point(0,0)
		calc=ArchimedeanSpiral()
		while(True):
			angle = calc.computeAngle(total_travelled)
			point=calc.computePoint(angle)
			total_travelled+=1
			if(point.x>self.map.width/2 or point.y > self.map.height/2):
				break;
			x_change = math.floor(point.x -last_point.x)
			y_change = math.floor(point.y -last_point.y)
			spiral_path.append((x_change,y_change));
			diameter_list.append(2 * math.ceil( point.distance(Point(0,0))))
			last_point = Point(last_point.x + x_change, last_point.y + y_change)
			step+=1
		
		spiral_approx = GridMovementApproximation( 0xdeadbeef, 10, self.map, delta_list=spiral_path)
		
		
		
		for i in range(len(list(spiral_approx.move_formulas.keys()))):
			states +="[] (mode & spiral=" + str(i) + " &" + list(spiral_approx.move_formulas.keys())[i] + " & " + list(spiral_approx.obstacle_formulas.keys())[i] +") -> 1: (spiral'=spiral+1) & (x2' = x2 +" + str(spiral_path[i][0]) + ") & (y2' = y2 +" + str(spiral_path[i][1]) + ") & (diameter'=" + str(diameter_list[i]) + ");\n"
		
		
		
 
		
		states += "\n// Movement transitions when robot can't move\n"
		prob = "1 / " + str(len(self.approximations))
		transition = prob + " : (dir'=0)"
		for i in range(1, len(self.approximations)):
			transition += " + " + prob + " : (dir'=" + str(i) + ") & (counter'=0)"
		
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			
			# Add boolean state specifier
			for j in range(self.speed):
			#need to account for whether we are at diameter or not
				states += "[] ("+coverageTest+"dir=" + str(i) + " & counter=" + str(j) + " & !(" + list(approx.move_formulas.keys())[j] + " & " + list(approx.obstacle_formulas.keys())[j] + ")) -> "
				states += transition + "& (mode'=false);\n"
			# If movement is done, set counter to 0 and continue
			# states += "[] (dir=" + str(i) + " & counter=" + str(self.speed) + ") -> (counter'=0);"
			states += "\n"



		for line in states.split("\n"):
			model += "\t" + line + "\n"

		model += "endmodule"

		# Add obstacle models
		obstacles = copy.copy(map.obstacles)
		count = 0
		for obstacle in obstacles:
			model += "\nmodule obstacle" + str(count) + "\n"
			count += 1
			model += "\t" + obstacle.x + " : int init " + str(obstacle.xVal) + ";\n"
			model += "\t" + obstacle.y + " : int init " + str(obstacle.yVal) + ";\n"
			model += "endmodule"

		# Reward for tracking where the robot has gone
		if self.tracker != None:
			model+= "\n"+self.tracker.rewards
			
		model += "//Formulas for checking if B movement along an angle is in bounds\n"
		
		for formula_name, formula in spiral_approx.move_formulas.items():
			model += formula + "\n";
		model += "\n"

		
		model += "//Formula for checking if B movement along an angle collides with obstacles\n"

		for formula_name, formula in spiral_approx.obstacle_formulas.items():
			model += formula + "\n";
		model += "\n"


		return model
		
if __name__ == "__main__":	
	if len(sys.argv) < 2:
		print("Please specify a map - 1, 2, or 3")
		exit(1)

	map_index = sys.argv[1]
	map = get_map_1()
	if map_index == "1":
		map = get_map_1()
	elif map_index == "2":
		map = get_map_2()
	elif map_index == "3":
		map = get_map_3()
	else:
		map = Map(10, 10)
		
	# coverage
	track = CoverageTracker(map)

	model = SpiralModelGenerator(map, num_angles=25, move_speed=10, tracker=track)
	print(model)
	


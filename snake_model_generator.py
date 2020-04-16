from grid_movement_approx import GridMovementApproximation, get_angles
from label_generator import LabelGenerator
from random_model_generator import RandomModelGenerator
from map import Map
import copy

class SnakeModelGenerator(RandomModelGenerator):

    # No changes thus far
	def __init__(self, map, num_angles=4, move_speed=1, goal_speed = 1):
		super().__init__(map, num_angles, move_speed)
		self.goal_speed = 1

	
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
		
		model += "module random_robot\n\n"
		
		#Add model states and variables
		states =  LabelGenerator.x + " : [1.." + str(self.map.width) + "] init 1; // robot x position\n"
		states += LabelGenerator.y + " : [1.." + str(self.map.height) + "] init 1; // robot y position\n"
		states += "dir : [0.." + str(len(self.approximations)-1) + "] init 1; // possible robot directions\n"
		states += "goal : [0.." + str(len(self.approximations)-1) + "] init 0; // Robot goal direction\n"
		states += "prevDir : [0.." + str(len(self.approximations)-1) + "] init 0; // Robot's previous direction after turning to goal\n"
		#states += "moving : [0..1] init 0; // if the robot is moving\n"
		states += "counter : [0.." + str(self.speed) +"] init 0; // if the robot is moving\n"
		states += "justTurned : [0..1] init 0; // 1 if the robot just turned into goal state\n"
		states += "\n"
		
		states += "// Movement transitions when robot can move, same as rand except !dir=goal\n"
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			# Add boolean state specifier for enterng 'move' mode
			#states += "[] (dir=" + str(i) + " & " + list(approx.move_formulas.keys())[0] + " & " + list(approx.obstacle_formulas.keys())[0] + ") -> 1 : (counter'=0);\n"
			
			# Add state specifiers for each stage of movement
			for j in range(self.speed):
				states += "[] (dir=" + str(i) + " & !(dir=goal & counter>="+str(self.goal_speed)+") & " + list(approx.move_formulas.keys())[j] + " & " + list(approx.obstacle_formulas.keys())[j] + " & counter=" + str(j) + ") -> 1 : (counter'=counter+1) & "
			
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
				states += ");\n"
			states += "\n"
		
		states += "\n// Movement transitions when dir != goal and can't/end of move\n"
		prob = "1 / " + str(len(self.approximations))
		# Fully random transition not needed right now
		transition = prob + " : (dir'=0)"
		for i in range(1, len(self.approximations)):
			transition += " + " + prob + " : (dir'=" + str(i) + ") & (counter'=0)"
		
		# For transitions when moving in direction != goalDirection, 
		# and hit obstacle: turn to direction = goal direction
		# if not hitting obstancle after full move, keep going
		direction_check = "!(dir = goal)"
		transition_to_goal = "1 : (prevDir' = dir) & (dir' = goal) & (counter' = 0)"
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			
			# Add boolean state specifier
			for j in range(self.speed):
				states += "[] (dir=" + str(i) + " & "+direction_check+" & counter=" + str(j) + " & !(" + list(approx.move_formulas.keys())[j] + " & " + list(approx.obstacle_formulas.keys())[j] + ")) -> "
				states += transition_to_goal + ";\n"
			# If movement is done, set counter to 0 and continue
			states += "[] (dir=" + str(i) + " & "+direction_check+" & counter=" + str(self.speed)+") -> (counter'=0);"
			states += "\n"
		
		states += "\n// Movement transitions when dir == goal and can't/end of move\n"
		# For transitions when moving in direction == goalDirection 
		# you hit a wall or obstacle or end movement , then turn to 
		# move in direction opposite prevDirection
		# Goal_speed is how long snake will travel in direction of 
		# goal before turning
		direction_check = "(dir = goal)"
		for g in range(len(self.approximations)):
			approx = self.approximations[g];
			for i in range(len(self.approximations)):
				next_direction = (i+len(self.approximations)//2) %len(self.approximations)
				next_prev_dir = (g+len(self.approximations)//2) %len(self.approximations)
				transition_next_dir = "1 : (dir' = "+str(next_direction)+") & (counter' = 0)"

				# Add boolean state specifier
				# Max speed in direction of goal is 1
				# If run into something when moving in direction of goal, change goals
				for j in range(self.goal_speed):
					states += "[] (goal="+str(g)+" & prevDir=" + str(i) + " & "+direction_check+" &  counter=" + str(j) + " & !(" + list(approx.move_formulas.keys())[j] + " & " + list(approx.obstacle_formulas.keys())[j] + ")) -> "
					states += transition_next_dir+"& (goal' = "+str(next_direction)+") & (prevDir' = "+str(g)+");\n"
				# If movement towards goal is done, turn to opposite 
				# direction of previous path
				states+="[] (goal="+str(g)+" & prevDir=" + str(i) + " & "+direction_check+ " & counter=" + str(self.goal_speed) + ") ->"
				states += transition_next_dir + ";\n"



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
		
		return model
	

if __name__ == "__main__":
	map = Map(10, 10)
	#map.add_obstacle(2,9)
	#map.add_obstacle(8, 4)
 
	model = SnakeModelGenerator(map, num_angles=4, move_speed=8, goal_speed=1)
	print(model)
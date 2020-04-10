from grid_movement_approx import GridMovementApproximation, get_angles
from label_generator import LabelGenerator
from map import Map
import copy
	
class RandomModelGenerator:

	def __init__(self, map, num_angles=4, move_speed=1):
		angles = get_angles(num_angles)
		
		self.approximations = []
		for angle in angles:
			self.approximations.append(GridMovementApproximation(angle, move_speed, map))
			
		self.map = map
	
	def __str__(self):
		model = "mdp\n\n"
		
		model += "//CONSTANTS\n"
		model += "const int " + LabelGenerator.w + " = " + str(self.map.width) + ";\n"
		model += "const int " + LabelGenerator.h + " = " + str(self.map.height) + ";\n\n"
		
		model += "//Formula for checking if movement along an angle is in bounds\n"
		for approx in self.approximations:
			model += approx.moveForumaText + "\n";
		model += "\n"
		
		model += "//Formula for checking if movement along an angle collides with obstacles\n"
		for approx in self.approximations:
			model += approx.obstacleFormulaTest + "\n";
		model += "\n"
		
		model += "module random_robot\n\n"
		
		states =  LabelGenerator.x + " : [1.." + str(self.map.width) + "] init 1; // robot x position\n"
		states += LabelGenerator.y + " : [1.." + str(self.map.height) + "] init 1; // robot y position\n"
		states += "dir : [0.." + str(len(self.approximations)-1) + "] init 0; // possible robot directions\n"
		states += "\n"
		
		states += "// Movement transitions when robot can move\n"
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			# Add boolean state specifier
			states += "[] (dir=" + str(i) + " & " + approx.moveFormula + " & " + approx.obstacleFormula + ") -> 1 : "
			# Add how x state changes
			states += "(" + LabelGenerator.x + "'=" + LabelGenerator.x;
			if approx.delta[0] > 0:
				states += "+" + str(approx.delta[0])
			elif approx.delta[0] < 0:
				states += "-" + str(abs(approx.delta[0]))
			# Add how y state changes
			states += ") & (" + LabelGenerator.y + "'=" + LabelGenerator.y;
			if approx.delta[1] > 0:
				states += "+" + str(approx.delta[1])
			elif approx.delta[1] < 0:
				states += "-" + str(abs(approx.delta[1]))
			states += ");\n"
			
		states += "\n// Movement transitions when robot can't move\n"
		prob = "1 / " + str(len(self.approximations))
		transition = prob + " : (dir'=0)"
		for i in range(1, len(self.approximations)):
			transition += " + " + prob + " : (dir'=" + str(i) + ")"
		
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			
			# Add boolean state specifier
			states += "[] (dir=" + str(i) + " & !(" + approx.moveFormula + " & " + approx.obstacleFormula + ")) -> "
			states += transition + ";\n"
		
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
	map.add_obstacle(9, 1)
	map.add_obstacle(8, 4)
		
	model = RandomModelGenerator(map, num_angles=8, move_speed=4)
	print(model)
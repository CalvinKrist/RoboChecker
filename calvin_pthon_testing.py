from grid_movement_approx import GridMovementApproximation, get_angles
from label_generator import LabelGenerator
	
class ModelGenerator:

	def __init__(self, map, num_angles, move_speed):
		angles = get_angles(num_angles)
		
		self.approximations = []
		for angle in angles:
			self.approximations.append(GridMovementApproximation(angle, move_speed))
			
		self.height = len(map)
		self.width = len(map[0])
	
	def __str__(self):
		model = "mdp\n\n"
		
		model += "//CONSTANTS\n"
		model += "const int " + LabelGenerator.w + " = " + str(self.width) + ";\n"
		model += "const int " + LabelGenerator.h + " = " + str(self.height) + ";\n\n"
		
		model += "//Formula for checking if the robot can move along each angle\n"
		for approx in self.approximations:
			model += approx.moveForumaText + "\n";
		model += "\n"
		
		model += "module random_robot\n\n"
		
		states =  LabelGenerator.x + " : [1.." + str(self.width) + "] init 1; // robot x position\n"
		states += LabelGenerator.y + " : [1.." + str(self.height) + "] init 1; // robot y position\n"
		states += "dir : [0.." + str(len(self.approximations)-1) + "] init 0; // possible robot directions\n"
		states += "\n"
		
		states += "// Movement transitions when robot can move\n"
		for i in range(len(self.approximations)):
			approx = self.approximations[i];
			# Add boolean state specifier
			states += "[] (dir=" + str(i) + " & " + approx.moveFormula + ") -> 1 : "
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
			states += "[] (dir=" + str(i) + " & !" + approx.moveFormula + ") -> "
			states += transition + ";\n"
		
		for line in states.split("\n"):
			model += "\t" + line + "\n"
		
		model += "endmodule"
		
		return model
	

if __name__ == "__main__":
	width = 10
	height = 25
	
	row = [0] * width
	map = []
	for i in range(height):
		map.append(row)
		
	model = ModelGenerator(map, 8, 10)
	print(model)
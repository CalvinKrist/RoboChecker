import math 
from label_generator import LabelGenerator
from map import Map
import copy

class CoverageTracker:
	def __init__(self, map, track_obstacles=False):
		self.map = map
		self.xVar = LabelGenerator.x
		self.yVar = LabelGenerator.y
		self.trackObs = track_obstacles
		self.variables = ""
		self.rewards = ""
		self.transitions = ""
		self.initValues()
		pass
	# Returns the tracking variables needed for the given map 
	# as well as the reward function
	def initValues(self):
		w = self.map.width
		h = self.map.height
		variables = "checkLoc : [0..1] init 1;\n"
		reward = "rewards \"coverage\"\n"
		transitions = ""
		# Need to 1 index
		# XxY
		for i in range(1,w+1):
			for j in range(1,h+1):
				if(not self.trackObs and (self.map.map[i][j]==1)):
					continue
				var_name = "r"+str(i)+"x"+str(j)
				variables += var_name+" : bool init false;\n"
				if(not (i == 1 and j == 1)):
					reward+=" | "
				checkGridxy = str(self.xVar)+"="+str(i)+" & "+str(self.yVar)+"="+str(j)
				reward += "(!"+var_name+" & "+checkGridxy+")"
				transitions+= "[coverage] (checkLoc=1 & "+checkGridxy+") -> 1 : (checkLoc'=0) & ("+var_name+"'=true);\n"
		reward+=": 1;\nendrewards\n\n"
		# Count number of coverage queries
		reward += "rewards \"coverageQuery\"\n"
		reward += "[coverage] true: 1;\n"
		reward += "endrewards\n"
		
		self.variables = variables
		self.rewards = reward
		self.transitions = transitions

from random_model_generator import RandomModelGenerator

if __name__ == "__main__":
	map = Map(10, 10)
	#map.add_obstacle(9, 1)
	#map.add_obstacle(8, 4)
		
	model = RandomModelGenerator(map, num_angles=10, move_speed=8)
	tracker = CoverageTracker(map)
	print(model)
	print(tracker)
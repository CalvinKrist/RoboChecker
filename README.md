# File Summary

### random_model_generator

This file has the main method. It also has the class `RandomModelGenerator`, which can output a mdp model of the `random` robot. Running this file will output one such model. Within the main method are variables allowing one to set:

* Map width
* Map height
* Number of possible angles
* Movement speed
	
### grid_movement_approx

This file contains the `GridMovementApproximation` class. This is used to help approximate movement at arbitrary angles along a Cartesian grid. It can be used to determine the rounded movement at a certain angle, the path to get there, and to generate functions on if that movement is possible. This file also has a main method that can be used to help debug this class.

### label_generator

This file contains the `LabelGenerator` class, which can be used to generate labels detailing if a specific path is possible. It also stores global variables for how the following 4 variables are named:

* `x`: the name of the state list for the robot's x position
* `y`: the name of the state list for the robot's y position
* `w`: the name of the variable with map width

* `h`: the name of the variable with map height
It also has a main method that can be used to debug label generation.
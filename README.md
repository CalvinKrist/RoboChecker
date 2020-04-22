# File Summary

### random_model_generator

This file has the main method. It also has the class `RandomModelGenerator`, which can output a mdp model of the `random` robot. Running this file will output one such model. Within the main method are variables allowing one to set:

* Map width
* Map height
* Number of possible angles
* Movement speed
* Coverage Tracker

### grid_movement_approx

This file contains the `GridMovementApproximation` class. This is used to help approximate movement at arbitrary angles along a Cartesian grid. It can be used to determine the rounded movement at a certain angle, the path to get there, and to generate functions on if that movement is possible. This file also has a main method that can be used to help debug this class.

### label_generator

This file contains the `LabelGenerator` class, which can be used to generate labels detailing if a specific path is possible. It also stores global variables for how the following 4 variables are named:

* `x`: the name of the state list for the robot's x position
* `y`: the name of the state list for the robot's y position
* `w`: the name of the variable with map width

* `h`: the name of the variable with map height
It also has a main method that can be used to debug label generation.

### snake_model_generator

This file contains the `SnakeModelGenerator` class which inherits from `GridMovementApproximation` class. Running this file will give an implementation of the snake algorithm we discussed with an arbitrary number of angles/obstacles. The subclass introduces a new variable:
* Goal Speed: the speed at which the robot approaches the goal before it turns to "snake"

### path_generator.bat

This script is used to generate paths using the PRISM command line with extended RAM. Within the script, make sure to set `PRISM_DIR` to the correct value. Additionally, for large models you may need to further expand the RAM PRISM is run with.

Usage: `path_generator.bat [map_number] [step_count] [output_file]`

### coverage_tracker

This is the helper that creates coverage tracking functionality for a given `map`.

Usage example: 
`tracker = CoverageTracker(map)`
`model = RandomModelGenerator(map, num_angles=25, move_speed=10, tracker=tracker)`
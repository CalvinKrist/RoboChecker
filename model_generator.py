from grid_movement_approx import GridMovementApproximation, get_angles

class ModelGenerator:
    def __init__(self, map, num_angles=4, move_speed=1, tracker=None):
        angles = get_angles(num_angles)
        self.speed = move_speed

        self.approximations = []
        for angle in angles:
            self.approximations.append(GridMovementApproximation(angle, move_speed, map))

        self.map = map
        self.tracker = tracker
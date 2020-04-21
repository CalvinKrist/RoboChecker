from obstacle import Obstacle

class Map:
	def __init__(self, width, height):
		row = [0] * (height + 1)
		map = []
		for i in range(width + 1):
			map.append(row)
			
		self.map = map
		self.width = width
		self.height = height
		
		self.obstacles = []

		self.spawn_x = 1
		self.spawn_y = 1
		
	def add_obstacle(self, x, y):
		self.map[x][y] = 1
		self.obstacles.append(Obstacle(x, y))


def add_rect(map, loc, dim):
	loc[0] = int(loc[0])
	loc[1] = int(loc[1])
	dim[0] = int(dim[0])
	dim[1] = int(dim[1])

	p1 = loc
	p4 = [loc[0] + dim[0], loc[1] + dim[1]]

	for x in range(p1[0], p4[0] + 1):
		for y in range(p1[1], p4[1] + 1):
			if x == p1[0] or x == p4[0] or y == p1[1] or y == p4[1]:
				map.add_obstacle(x, y)

# A rectangular space with a bathroom in one corner with only a door
# to enter. There is a dresser along one wall and a hamper along
# another, and bed posts in a third corner
def get_map_1():
	width = 450
	map = Map(width, int(width * .9))

	# Add bathroom walls
	x = int(map.width * .6)
	for y in range(1, int(map.height * .46 + 1)):
		map.add_obstacle(x, y)

	y = int(map.height * .46)
	door_width = int(map.width * .12)
	door_center = int(map.width * .8)
	for x in range(int(map.width * .6), map.width + 1):
		if not (x >= door_center - door_width / 2 and x <= door_center + door_width / 2):
			map.add_obstacle(x, y)

	# Add dresser
	add_rect(map, [map.width * .605, map.height * .46], [map.width * .13, map.height * .077])

	# Add hamper
	width = int(map.width * .08)
	height = width
	add_rect(map, [map.width / 2 - width / 2, map.height - height], [width, height])

	# Add bed posts
	w_bed = int(map.width * .18)
	h_bed = int(map.height * .377)
	w_post = int(map.width * .01)
	offset = int(map.width * .01)

	# Add lower left bed post
	add_rect(map, [offset, map.height - w_post - offset], [w_post, w_post])
	# Add lower right bed post
	add_rect(map, [offset + w_bed, map.height - w_post - offset], [w_post, w_post])
	# Add upper left bed post
	add_rect(map, [offset, map.height - w_post - offset - h_bed], [w_post, w_post])
	# Add upper right bed post
	add_rect(map, [offset + w_bed, map.height - w_post - offset - h_bed], [w_post, w_post])

	map.spawn_x = 100
	map.spawn_y = 100

	return map

# A hallway that leads to multiple connected rooms
# One of the rooms is a kitchen with a large central tabletop
def get_map_2():
	width = 450
	m = Map(width, int(width * 0.9))

	hallway_height = int(m.height * .111)
	half_w_door = int(m.width * 0.12 * 0.5)

	# Add hallway
	for x in range(1, m.width + 1):
		if x not in range(int(m.width / 4) - half_w_door, int(m.width / 4) + half_w_door) and x not in range(int(3 * m.width / 4) - half_w_door, int(3 * m.width / 4 + half_w_door)):
			m.add_obstacle(x, hallway_height)

	# Add dividing walls

	x = int(m.width / 2)
	for y in range(hallway_height + 1, m.height + 1):
		m.add_obstacle(x, y)

	offset = int(m.height * 0.0444)
	for nx in range(x, m.width + 1):
		m.add_obstacle(nx, int(m.height / 2) - offset)

	for nx in range(1, x):
		if nx not in range(int(m.width / 4 - half_w_door), int(m.width / 4) + half_w_door):
			m.add_obstacle(nx, int(m.height / 2) + offset)

	# Add kitchen table
	center = [int(x / 2), int(int((m.height / 2) + offset - hallway_height) / 2)  + hallway_height]
	width = int(m.width * .18)
	height = int(m.height * .1222)
	add_rect(m, [center[0] - width / 2, center[1] - height / 2], [width, height])

	# Add dinning room table leg posts
	room_height = m.height - (int(m.height / 2) + offset)
	center = [int(x / 2), int(m.height - room_height / 2)]
	w_table = int(m.width * .28)
	h_table = int(m.height * .2)
	w_leg = int(m.width * .01)
	add_rect(m, [center[0] - w_table / 2, center[1] - h_table / 2], [w_leg, w_leg])
	add_rect(m, [center[0] + w_table / 2 - w_leg, center[1] - h_table / 2], [w_leg, w_leg])
	add_rect(m, [center[0] + w_table / 2 - w_leg, center[1] + h_table / 2 - w_leg], [w_leg, w_leg])
	add_rect(m, [center[0] - w_table / 2, center[1] + h_table / 2 - w_leg], [w_leg, w_leg])

	# Add chair legs
	w_chair = int(m.width * .02)
	w_chair_leg = int(m.width * .005)
	off_1 = int(m.width * .004)
	off_2 = int(m.width * .018)
	chair1 = [center[0] - w_table / 2 + w_chair * 4, center[1] - h_table / 2 - off_1]
	chair2 = [center[0] + w_table / 2 - w_chair * 4 - w_chair, center[1] - h_table / 2 - off_1]
	chair3 = [center[0] - w_table / 2 + w_chair * 4, center[1] - off_2 + h_table / 2]
	chair4 = [center[0] + w_table / 2 - w_chair * 4 - w_chair, center[1] - off_2 + h_table / 2]
	chairs = [chair1, chair2, chair3, chair4]

	for chair in chairs:
		add_rect(m, [chair[0], chair[1]], [w_chair_leg, w_chair_leg])
		add_rect(m, [chair[0] + w_chair, chair[1]], [w_chair_leg, w_chair_leg])
		add_rect(m, [chair[0], chair[1] + w_chair], [w_chair_leg, w_chair_leg])
		add_rect(m, [chair[0] + w_chair, chair[1] + w_chair], [w_chair_leg, w_chair_leg])

	m.spawn_x = 15
	m.spawn_y = 20

	return m

# A non-rectangular room with angled walls
def get_map_3():
	width = 450
	m = Map(width, int(width * .8))

	# Add lines around the corners
	x = 0
	y = int(2 * m.height / 3)
	while y < m.height + 1:
		m.add_obstacle(x, y)
		m.add_obstacle(x + 1, y)
		x += 1
		y += 1

	x = m.width
	y = int(2 * m.height / 3)
	while y < m.height + 1:
		m.add_obstacle(x, y)
		m.add_obstacle(x - 1, y)
		x -= 1
		y += 1

	# Add lines in the upper-center
	delta = int(m.height * .25)
	x = int(m.width / 5)
	y = 0
	while y < delta:
		m.add_obstacle(x, y)
		m.add_obstacle(x + 1, y)
		x += 1
		y += 1

	# Add lines in the upper-center
	x = int(4 * m.width / 5)
	y = 0
	while y < delta:
		m.add_obstacle(x, y)
		m.add_obstacle(x - 1, y)
		x -= 1
		y += 1

	y = delta
	for x in range(int(m.width / 5) + delta, int(4 * m.width / 5) + 1 - delta):
		m.add_obstacle(x, y)

	m.spawn_x = 225
	m.spawn_y = 200

	return m
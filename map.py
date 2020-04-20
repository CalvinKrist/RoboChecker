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
	map = Map(5000, 4500)

	# Add bathroom walls
	x = 3000
	for y in range(0, 2100 + 1):
		map.add_obstacle(x, y)

	y = 2100
	door_width = 600
	door_center = 4000
	for x in range(3000, map.width + 1):
		if not (x >= door_center - door_width / 2 and x <= door_center + door_width / 2):
			map.add_obstacle(x, y)

	# Add dresser
	add_rect(map, [3025, 2100], [650, 350])

	# Add hamper
	width = 400
	height = 400
	add_rect(map, [map.width / 2 - width / 2, map.height - height], [width, height])

	# Add bed posts
	w_bed = 900
	h_bed = 1700
	w_post = 50
	offset = 50

	# Add lower left bed post
	add_rect(map, [offset, map.height - w_post - offset], [w_post, w_post])
	# Add lower right bed post
	add_rect(map, [offset + w_bed, map.height - w_post - offset], [w_post, w_post])
	# Add upper left bed post
	add_rect(map, [offset, map.height - w_post - offset - h_bed], [w_post, w_post])
	# Add upper right bed post
	add_rect(map, [offset + w_bed, map.height - w_post - offset - h_bed], [w_post, w_post])

	return map

# A hallway that leads to multiple connected rooms
# One of the rooms is a kitchen with a large central tabletop
def get_map_2():
	m = Map(5000, 4500)

	# Add hallway
	for x in range(0, m.width + 1):
		if x not in range(int(m.width / 4) - 300, int(m.width / 4) + 300) and x not in range(int(3 * m.width / 4) - 300, int(3 * m.width / 4 + 300)):
			m.add_obstacle(x, 500)

	# Add dividing walls
	x = int(m.width / 2)
	for y in range(500, m.height + 1):
		m.add_obstacle(x, y)

	for nx in range(x, m.width + 1):
		m.add_obstacle(nx, int(m.height / 2) - 200)

	for nx in range(0, x):
		if nx not in range(int(m.width / 4 - 300), int(m.width / 4) + 300):
			m.add_obstacle(nx, int(m.height / 2) + 200)

	# Add kitchen table
	center = [int(x / 2), int(int((m.height / 2) + 200 - 500) / 2)  + 500]
	width = 900
	height = 550
	add_rect(m, [center[0] - width / 2, center[1] - height / 2], [width, height])

	# Add dinning room table leg posts
	room_height = m.height - (int(m.height / 2) + 200)
	center = [int(x / 2), int(m.height - room_height / 2)]
	w_table = 1400
	h_table = 900
	w_leg = 50
	add_rect(m, [center[0] - w_table / 2, center[1] - h_table / 2], [w_leg, w_leg])
	add_rect(m, [center[0] + w_table / 2 - w_leg, center[1] - h_table / 2], [w_leg, w_leg])
	add_rect(m, [center[0] + w_table / 2 - w_leg, center[1] + h_table / 2 - w_leg], [w_leg, w_leg])
	add_rect(m, [center[0] - w_table / 2, center[1] + h_table / 2 - w_leg], [w_leg, w_leg])

	# Add chair legs
	w_chair = 100
	w_chair_leg = 25
	chair1 = [center[0] - w_table / 2 + 100, center[1] - h_table / 2 - 20]
	chair2 = [center[0] + w_table / 2 - 100 - w_chair, center[1] - h_table / 2 - 20]
	chair3 = [center[0] - w_table / 2 + 100, center[1] - 90 + h_table / 2]
	chair4 = [center[0] + w_table / 2 - 100 - w_chair, center[1] - 90 + h_table / 2]
	chairs = [chair1, chair2, chair3, chair4]

	for chair in chairs:
		add_rect(m, [chair[0], chair[1]], [w_chair_leg, w_chair_leg])
		add_rect(m, [chair[0] + w_chair, chair[1]], [w_chair_leg, w_chair_leg])
		add_rect(m, [chair[0], chair[1] + w_chair], [w_chair_leg, w_chair_leg])
		add_rect(m, [chair[0] + w_chair, chair[1] + w_chair], [w_chair_leg, w_chair_leg])

	return m

# A non-rectangular room with angled walls
def get_map_3():
	m = Map(5000, 4000)

	# Add lines around the corners
	x = 0
	y = int(2 * m.height / 3)
	while y < m.height + 1:
		m.add_obstacle(x, y)
		x += 1
		y += 1

	x = m.width
	y = int(2 * m.height / 3)
	while y < m.height + 1:
		m.add_obstacle(x, y)
		x -= 1
		y += 1

	# Add lines in the upper-center
	x = int(m.width / 5)
	y = 0
	while y < 800:
		m.add_obstacle(x, y)
		x += 1
		y += 1

	# Add lines in the upper-center
	x = int(4 * m.width / 5)
	y = 0
	while y < 800:
		m.add_obstacle(x, y)
		x -= 1
		y += 1

	y = 800
	for x in range(int(m.width / 5) + 800, int(4 * m.width / 5) + 1 - 800):
		m.add_obstacle(x, y)

	return m
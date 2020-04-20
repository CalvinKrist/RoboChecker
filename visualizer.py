from PIL import Image
from map import *

def to_image(m, name):

    img = Image.new('RGB', (m.width, m.height))

    data = [(255, 255, 255)] * (m.width * m.height)

    for obstacle in m.obstacles:
        data[obstacle.xVal - 1 + (obstacle.yVal - 1) * m.width] = (0, 0, 0)

    img.putdata(data)
    img.save(name)

if __name__ == "__main__":
    to_image(get_map_1(), "maps/map_1.png")
    to_image(get_map_2(), "maps/map_2.png")
    to_image(get_map_3(), "maps/map_3.png")
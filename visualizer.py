from PIL import Image
from map import *
from label_generator import LabelGenerator
import os

def to_image(m, name):

    img = Image.new('RGB', (m.width, m.height))

    data = [(255, 255, 255)] * (m.width * m.height)

    for obstacle in m.obstacles:
        data[obstacle.xVal - 1 + (obstacle.yVal - 1) * m.width] = (0, 0, 0)

    img.putdata(data)
    img.save(name)

def path_to_points(path, kernel):
    points = []

    lines = []
    with open(path) as f:
        lines = f.read().split("\n")

    labels = lines[0].split(" ")
    x_index = 0
    y_index = 0

    for i in range(len(labels)):
        if labels[i] == LabelGenerator.x:
            x_index = i
        elif labels[i] == LabelGenerator.y:
            y_index = i

    del lines[0]

    for line in lines:
        if len(line) > 5:
            tokens = line.split(" ")
            x = int(tokens[x_index])
            y = int(tokens[y_index])
            k = int(kernel / 2)
            offset = 0 if kernel % 2 == 0 else 1
            for kx in range(x - k, x + k + offset):
                for ky in range(y - k, y + k + offset):
                    points.append((kx, ky))

    return points

def dir_to_points(dir, kernel):
    points = []
    for filename in os.listdir(dir):
        points.extend(path_to_points(os.path.join(dir, filename), kernel))
    return points

def to_heatmap(m, points, name):
    histogram = {}
    for point in points:
        if point[0] > 0 and point[0] <= m.width and point[1] > 0 and point[1] <= m.height:
            if point in histogram.keys():
                histogram[point] += 1
            else:
                histogram[point] = 1

    max = 0
    for key, count in histogram.items():
        if count > max:
            max = count

    img = Image.new('RGB', (m.width, m.height))

    data = [(255, 255, 255)] * (m.width * m.height)

    # Add heatmap data
    for point, count in histogram.items():
        prop = count / max
        data[point[0] - 1 + m.width * (point[1] - 1)] = (int(150 * prop + 105), int(100 - 100 * prop), int(150 - 150 * prop))

    # Add obstacle data
    for obstacle in m.obstacles:
        data[obstacle.xVal - 1 + (obstacle.yVal - 1) * m.width] = (0, 0, 0)

    img.putdata(data)
    img.save(name)

if __name__ == "__main__":
    to_image(get_map_1(), "images/map_1.png")
    to_image(get_map_2(), "images/map_2.png")
    to_image(get_map_3(), "images/map_3.png")

    to_heatmap(get_map_1(), dir_to_points("m1_paths", 5), "images/m1.png")
    to_heatmap(get_map_2(), dir_to_points("m2_paths", 5), "images/m2.png")
    to_heatmap(get_map_3(), dir_to_points("m3_paths", 5), "images/m3.png")
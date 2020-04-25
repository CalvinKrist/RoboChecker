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
        data[point[0] - 1 + m.width * (point[1] - 1)] = (int(225 * prop + 30), int(20 - 20 * prop), int(120 - 120 * prop))

    # Add obstacle data
    for obstacle in m.obstacles:
        data[obstacle.xVal - 1 + (obstacle.yVal - 1) * m.width] = (0, 0, 0)

    # Mark spawn point
    data[points[0][0] - 1 + (points[0][1] - 1) * m.width] = (0, 255, 0)

    img.putdata(data)
    img.save(name)

if __name__ == "__main__":
    to_image(get_map_1(), "maps/map_1.png")
    to_image(get_map_2(), "maps/map_2.png")
    to_image(get_map_3(), "maps/map_3.png")

    # Draw map 1 heatmaps
    '''to_heatmap(get_map_1(), path_to_points("spiral/m1paths/spawn1.txt", 1), "spiral/m1s1.png")
    to_heatmap(get_map_1(), path_to_points("random/m1paths/spawn1.txt", 1), "random/m1s1.png")
    to_heatmap(get_map_1(), path_to_points("snake/m1paths/spawn1.txt", 1), "snake/m1s1.png")
    to_heatmap(get_map_1(), path_to_points("spiral/m1paths/spawn2.txt", 1), "spiral/m1s2.png")
    to_heatmap(get_map_1(), path_to_points("random/m1paths/spawn2.txt", 1), "random/m1s2.png")
    to_heatmap(get_map_1(), path_to_points("snake/m1paths/spawn2.txt", 1), "snake/m1s2.png")'''

    # Draw map 2 heatmaps
    '''to_heatmap(get_map_2(), path_to_points("spiral/m2paths/spawn1.txt", 1), "spiral/m2s1.png")
    to_heatmap(get_map_2(), path_to_points("random/m2paths/spawn1.txt", 1), "random/m2s1.png")
    to_heatmap(get_map_2(), path_to_points("snake/m2paths/spawn1.txt", 1), "snake/m2s1.png")
    to_heatmap(get_map_2(), path_to_points("spiral/m2paths/spawn2.txt", 1), "spiral/m2s2.png")
    to_heatmap(get_map_2(), path_to_points("random/m2paths/spawn2.txt", 1), "random/m2s2.png")
    to_heatmap(get_map_2(), path_to_points("snake/m2paths/spawn2.txt", 1), "snake/m2s2.png")
    to_heatmap(get_map_2(), path_to_points("spiral/m2paths/spawn3.txt", 1), "spiral/m2s3.png")
    to_heatmap(get_map_2(), path_to_points("random/m2paths/spawn3.txt", 1), "random/m2s3.png")
    to_heatmap(get_map_2(), path_to_points("snake/m2paths/spawn3.txt", 1), "snake/m2s3.png")'''
    to_heatmap(get_map_2(), path_to_points("spiral/m2paths/spawn4.txt", 1), "spiral/m2s4.png")
    to_heatmap(get_map_2(), path_to_points("random/m2paths/spawn4.txt", 1), "random/m2s4.png")
    to_heatmap(get_map_2(), path_to_points("snake/m2paths/spawn4.txt", 1), "snake/m2s4.png")

    # Draw map 3 heatmaps
    to_heatmap(get_map_3(), path_to_points("spiral/m3paths/spawn1.txt", 1), "spiral/m3s1.png")
    to_heatmap(get_map_3(), path_to_points("random/m3paths/spawn1.txt", 1), "random/m3s1.png")
    to_heatmap(get_map_3(), path_to_points("snake/m3paths/spawn1.txt", 1), "snake/m3s1.png")
    to_heatmap(get_map_3(), path_to_points("spiral/m3paths/spawn2.txt", 1), "spiral/m3s2.png")
    to_heatmap(get_map_3(), path_to_points("random/m3paths/spawn2.txt", 1), "random/m3s2.png")
    to_heatmap(get_map_3(), path_to_points("snake/m3paths/spawn2.txt", 1), "snake/m3s2.png")
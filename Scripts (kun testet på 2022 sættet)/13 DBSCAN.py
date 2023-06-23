from sklearn.cluster import DBSCAN
import numpy as np

## Used for 13/20 in 2022 exam

data = [
    ("A", 4, 1),
    ("B", 2, 2),
    ("C", 5, 2),
    ("D", 7, 2),
    ("E", 1, 5),
    ("F", 5, 6),
    ("G", 2, 4),
    ("H", 5, 4),
    ("I", 7, 4),
    ("J", 4, 5),
    ("K", 6, 8),
    ("L", 8, 5),
    ("M", 2, 6),
    ("N", 3, 6),
    ("O", 7, 6),
    ("P", 2, 7),
    ("Q", 5, 7),
    ("R", 8, 7),
    ("S", 8, 8)
]

def manhattan_distance(p1, p2):
    return abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def is_core_point(point, epsilon, min_pts):
    neighbors = [p for p in data if manhattan_distance(point, p) <= epsilon]
    return len(neighbors) >= min_pts

statements = [
    ("M", 1, 2),
    ("L", 2, 5),
    ("B", 2, 3),
    ("C", 2, 5),
    ("O", 3, 5),
    ("A", 2, 3),
    ("S", 3, 4),
    ("Q", 1, 4)
]

for point_label, epsilon, min_pts in statements:
    point = [p for p in data if p[0] == point_label][0]
    result = is_core_point(point, epsilon, min_pts)
    print(f"{point_label} is a core point for ε = {epsilon} and MinPts = {min_pts}: {result}")

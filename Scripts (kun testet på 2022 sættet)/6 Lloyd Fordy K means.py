import numpy as np

## used for solution04 exercise 4.3 and page 6/20 in the 2022 exam

def custom_distance(x, y, mu):
    diff = np.array([x[0] - y[0], x[1] - y[1]])
    matrix = np.array([[3, 1], [0, 2]])
    result = np.sqrt(diff.dot(matrix).dot(diff.T))
    return result

# Given centroids and points
mu1 = (0, 2)
mu2 = (4, 7)
points = [(2, 5), (4, 0), (3, 4), (3, 3), (4, 4)]

# Calculate distances and assign points to clusters
assignments = []
for point in points:
    dist_to_mu1 = custom_distance(point, mu1, mu1)
    dist_to_mu2 = custom_distance(point, mu2, mu2)
    
    if dist_to_mu1 < dist_to_mu2:
        cluster = 1
    else:
        cluster = 2

    assignments.append(cluster)

# Print results
for idx, point in enumerate(points):
    print(f"Point {point} will be assigned to Cluster {assignments[idx]}")

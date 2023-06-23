import numpy as np

def distance_measure(point, mu):
    matrix = np.array([[2, 0], [0, 4]])
    diff = point - mu
    result = np.sqrt(np.dot(np.dot(diff, matrix), diff.T))
    return result

def assign_clusters(points, clusters):
    assignments = []
    results = []
    for point in points:
        distances = [distance_measure(point, mu) for mu in clusters]
        cluster_index = np.argmin(distances)
        assignments.append(cluster_index + 1)  # Cluster numbering starts from 1
        results.append(distances[cluster_index])
    return assignments, results

# Define the points and cluster means
points = np.array([(0, 2), (4, 0), (np.sqrt(8), 0), (8, 0), (np.sqrt(2), np.sqrt(3)), (1,0), (0,-2)])
clusters = np.array([(0, 0)])

# Assign points to clusters and get the distance results
assignments, results = assign_clusters(points, clusters)

# Print the assignments and distance results
for i, point in enumerate(points):
    print(f"Point {point} is assigned to Cluster {assignments[i]}")
    print(f"Distance: {results[i]}")
    print("-------------")


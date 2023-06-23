import numpy as np

def euclidean_distance(x, y):
    return abs(x - y)

def update_centroids(points, assignments, k):
    new_centroids = []
    for i in range(k):
        cluster_points = [points[j] for j in range(len(points)) if assignments[j] == i]
        if cluster_points:
            new_centroids.append(np.mean(cluster_points))
        else:
            new_centroids.append(None)
    return new_centroids

# Given points, initial means, and k value
points = [2, 3, 4, 10, 11, 12, 20, 25, 30]
k = 3
initial_means = [2, 4, 6]

# Initialize centroids and assignments
centroids = initial_means
assignments = [None] * len(points)

iteration = 0
while True:
    # Assign points to the closest centroid
    new_assignments = []
    for point in points:
        distances = [euclidean_distance(point, centroid) for centroid in centroids if centroid is not None]
        closest_centroid_idx = np.argmin(distances)
        new_assignments.append(closest_centroid_idx)
    
    # Update centroids based on new assignments
    new_centroids = update_centroids(points, new_assignments, k)
    
    # Check if the assignments have changed or not
    if new_assignments == assignments:
        break
    else:
        assignments = new_assignments
        centroids = new_centroids
        iteration += 1

    # Print results for each iteration
    print(f"Iteration {iteration}:")
    for i in range(k):
        cluster_points = [points[j] for j in range(len(points)) if assignments[j] == i]
        print(f"C{i + 1} = {cluster_points}")
    print(f"New centroids: {centroids}")

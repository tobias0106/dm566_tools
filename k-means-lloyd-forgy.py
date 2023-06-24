import numpy as np

def compute_distance(point, mean):
    return np.linalg.norm(point - mean)

def update_clusters(points, means):
    clusters = [[] for _ in range(len(means))]

    for point in points:
        distances = [compute_distance(point, mean) for mean in means]
        closest_mean_index = np.argmin(distances)
        clusters[closest_mean_index].append(point)

    return clusters

def update_means(clusters):
    means = []
    for cluster in clusters:
        mean = np.mean(cluster, axis=0)
        means.append(mean)

    return means

def k_means(points, initial_means):
    means = initial_means.copy()
    clusters = None

    while True:
        new_clusters = update_clusters(points, means)
        new_means = update_means(new_clusters)

        if np.array_equal(means, new_means):
            clusters = new_clusters
            break

        means = new_means

    return clusters

# Input data
points = np.array([[2, 0], [3, 0], [4, 0], [10, 0], [11, 0], [12, 0], [20, 0], [25, 0], [30, 0]])
initial_means = np.array([[2, 0], [4, 0], [6, 0]])

# Run k-means algorithm
clusters = k_means(points, initial_means)

means = update_means(clusters)

# Print clusters after each iteration
iteration = 1
for cluster in clusters:
    print(f"cluster {iteration}: {cluster}")
    iteration += 1

print("\nfinal means:", means)

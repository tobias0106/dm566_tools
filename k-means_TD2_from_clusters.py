import numpy as np

def T2individual(p1, p2):
    return np.sum((p1 - p2) ** 2)

def calculate_td2_score(clusters):
    means = [np.mean(cluster, axis=0) for cluster in clusters]
    td2_score = 0
    for i, cluster in enumerate(points):
        for point in cluster:
            td2_score += T2individual(point, means[i])

    return td2_score

# Example inputs
points = [np.array([(1, 0), (3,0), (5,0)]), np.array([(7,0), (10,0), (11,0), (12,0)])]

# Calculate TD2 score
td2_score = calculate_td2_score(points)

print("TD2 Score:", td2_score)

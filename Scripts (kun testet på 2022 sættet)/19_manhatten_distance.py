## Used for page 19/20 in the exam 2022

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def knn_classifier(circle_coords, square_coords, test_point, k):
    distances = []

    for coord in circle_coords:
        distances.append((manhattan_distance(coord, test_point), 'circle'))
    
    for coord in square_coords:
        distances.append((manhattan_distance(coord, test_point), 'square'))

    distances.sort()
    nearest_neighbors = distances[:k]

    circle_count = sum(1 for _, label in nearest_neighbors if label == 'circle')
    square_count = sum(1 for _, label in nearest_neighbors if label == 'square')

    return 'circle' if circle_count > square_count else 'square'


circle_coords = [(1,8),(2,2),(2,9),(4,9),(5,6),(6,7), (9,9)]
square_coords = [(3,3),(6,1),(6,2),(7,3),(7,4),(8,3), (8,4)]
test_point = (6, 6)

for k in [7, 6, 5, 3, 2]:
    prediction = knn_classifier(circle_coords, square_coords, test_point, k)
    print(f"For k={k}, the classifier will predict the label for the query point at {test_point} as {prediction}")

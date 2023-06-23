## Used for page 19/20 in the exam 2022

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def euclidean_distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5


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

# Coords and test points used for 2022 exam, give the correct answer
circle_coords = [(1,8),(2,2),(2,9),(4,9),(5,6),(6,7), (9,9)]
square_coords = [(3,3),(6,1),(6,2),(7,3),(7,4),(8,3), (8,4)]
test_point = (6, 6)

# Coords and test point used for 2021 exam, gives the correct answer
circle_coords2 = [(5,2),(6,1),(6,3),(6,4),(7,2),(8,2), (8,8),(9,3)]
square_coords2 = [(2,8),(3,4),(4,4),(4,6),(4,8),(5,7), (6,6), (7,3),(7,5),(8,9)]
test_point2 = (7, 4)


for k in [7 , 6, 5, 3, 2]:
    prediction = knn_classifier(circle_coords, square_coords, test_point, k)
    print(f"For k={k}, the classifier will predict the label for the query point at {test_point} as {prediction}")


'''
for k in [3 , 6, 10, 13, 15, 17, 18]:
    prediction = knn_classifier(circle_coords2, square_coords2, test_point2, k)
    print(f"For k={k}, the classifier will predict the label for the query point at {test_point2} as {prediction}")
'''
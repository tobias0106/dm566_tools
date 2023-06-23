import numpy as np
from sklearn.svm import SVC

# Used for 18/20 in exam 2022

circle_coordinates = [(2,8),(3,9),(4,6),(5,7),(6,6),(6,8)]
square_coordinates = [(3,3),(4,4),(5,3),(6,1),(6,2),(6,4), (8,2)]


positive_points = np.array(circle_coordinates)
negative_points = np.array(square_coordinates)

X = np.vstack((positive_points, negative_points))
y = np.hstack((np.ones(len(circle_coordinates)), -np.ones(len(square_coordinates))))

model = SVC(kernel='linear', C=1E10)
model.fit(X, y)

output = model.predict([(1, 4)])[0]
if output == 1:
    print("True")
else:
    print("False")



output = model.predict([(4, 1)])[0]
if output == 1:
    print("True")
else:
    print("False")


decision_value = model.decision_function([(1, 5)])[0]
if np.isclose(decision_value, 0, atol=1e-5):
    print("True")
else:
    print("False")


print((2, 8) in model.support_vectors_) # Output: True or False


print((6, 6) in model.support_vectors_) # Output: True or False


print((3, 3) in model.support_vectors_) # Output: True or False


print((4, 4) in model.support_vectors_) # Output: True or False

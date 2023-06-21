import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

# Square points
square_points = np.array([[3, 3], [4, 4], [5, 3], [6, 1], [6, 2], [6, 4], [8, 2]])
# Circle points
circle_points = np.array([[4, 6], [6, 6], [5, 7], [2, 8], [3, 9], [6, 8]])
# Labels (0 for square, 1 for circle)
labels = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Concatenate square and circle points
points = np.concatenate((square_points, circle_points))

# Create an SVM classifier
classifier = svm.SVC(kernel='linear')

# Fit the classifier to the points
classifier.fit(points, labels)

# Get support vectors and coefficients
support_vectors = classifier.support_vectors_
coefficients = classifier.coef_[0]

# Create a meshgrid to plot the decision boundary
x_min, x_max = points[:, 0].min() - 1, points[:, 0].max() + 1
y_min, y_max = points[:, 1].min() - 1, points[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the points
plt.scatter(square_points[:, 0], square_points[:, 1], color='red', label='Square')
plt.scatter(circle_points[:, 0], circle_points[:, 1], color='blue', label='Circle')

# Plot the support vectors
plt.scatter(support_vectors[:, 0], support_vectors[:, 1], color='black', marker='x', label='Support Vectors')

# Plot the decision boundary
plt.contour(xx, yy, Z, colors='black', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# Set plot labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.show()


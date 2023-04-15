import numpy as np

# probabilities of classifiers given the training data
p_h = np.array([0.6, 0.3, 0.1])

# class probabilities for each test instance and classifier
o_h = np.array([
    [[0.4, 0.6], [0.7, 0.3], [0.5, 0.5]],
    [[0.1, 0.9], [0.5, 0.5], [0.8, 0.2]],
    [[0.0, 1.0], [0.4, 0.6], [0.6, 0.4]],
    [[0.2, 0.8], [0.7, 0.3], [0.5, 0.5]],
    [[0.5, 0.5], [0.1, 0.9], [0.2, 0.8]]
])

# combine the classifiers using Bayes optimal classifier
p_o = np.zeros((5, 2))
for i in range(5):
    for j in range(3):
        p_o[i] += p_h[j] * o_h[i][j]
        
# print the results
for i in range(5):
    print(f"Class probabilities for test instance O{i+1}:")
    print("+:", p_o[i][0])
    print("-:", p_o[i][1])

import numpy as np

# Define the training data
X_train = np.array([['C', 'F'], ['A', 'E'], ['A', 'G'], ['B', 'G'], ['C', 'F'], ['B', 'D'], ['B', 'E'], ['C', 'E']])
y_train = np.array([1, -1, 1, -1, -1, 1, 1, -1])

def naive_bayes_predict(x1, x2):
    probabilities = []
    
    for y in [1, -1]:
        # Compute P(Y=y)
        p_y = np.mean(y_train == y)

        # Compute P(X1=x1 | Y=y)
        p_x1_given_y = np.mean(X_train[y_train == y, 0] == x1)

        # Compute P(X2=x2 | Y=y)
        p_x2_given_y = np.mean(X_train[y_train == y, 1] == x2)

        # Compute P(X1=x1, X2=x2 | Y=y) using naive Bayes assumption
        p_x1_x2_given_y = p_x1_given_y * p_x2_given_y

        probabilities.append(p_x1_x2_given_y * p_y)

    # Normalize the probabilities
    total_prob = sum(probabilities)
    if total_prob == 0:
        return [0, 0]
    else:
        return [p / total_prob for p in probabilities]

queries = [['C', 'D',], ['A', 'D',], ['B', 'F',], ['A', 'F',], ['C', 'G',]]

# Compute the probabilities for each query
for query in queries:
    x1, x2 = query
    p_plus_1, p_minus_1 = naive_bayes_predict(x1, x2)
    print(f"P(Y=+1 | X1={x1}, X2={x2}) = {p_plus_1:.3f}, P(Y=-1 | X1={x1}, X2={x2}) = {p_minus_1:.3f}")

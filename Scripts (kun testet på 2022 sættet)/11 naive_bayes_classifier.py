import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

## Used for page 11/20 in the 2022 exam

data = np.array([
    [1, 'A', 'D', 1],
    [2, 'B', 'D', -1],
    [3, 'A', 'E', 1],
    [4, 'C', 'D', -1],
    [5, 'B', 'E', -1],
    [6, 'A', 'E', 1],
    [7, 'B', 'D', 1],
    [8, 'C', 'D', -1],
    [9, 'A', 'D', -1]
], dtype=object)


le_X1 = LabelEncoder()
le_X2 = LabelEncoder()

X = data[:, 1:3]
X[:, 0] = le_X1.fit_transform(X[:, 0])
X[:, 1] = le_X2.fit_transform(X[:, 1])
Y = data[:, 3].astype(int)


gnb = GaussianNB()
gnb.fit(X, Y)


def evaluate_query(query):
    query_encoded = [le_X1.transform([query[0]])[0], le_X2.transform([query[1]])[0]]
    prediction = gnb.predict([query_encoded])[0]
    probabilities = gnb.predict_proba([query_encoded])[0]
    print(f"For test query {query}, it predicts class {prediction} with probabilities {probabilities}")


evaluate_query(('B', 'E'))
evaluate_query(('C', 'E'))
evaluate_query(('A', 'D'))
evaluate_query(('B', 'D'))

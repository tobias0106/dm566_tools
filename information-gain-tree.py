import pandas as pd
import numpy as np

data = {'X1': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
        'X2': ['C', 'C', 'D', 'D', 'C', 'C', 'D', 'C', 'D', 'C'],
        'X3': ['E', 'F', 'E', 'F', 'F', 'E', 'E', 'E', 'F', 'F'],
        'Y':  [-1, 1, -1, 1, -1, -1, 1, 1, 1, -1]}

df = pd.DataFrame(data)

def entropy(y):
    p = y.value_counts(normalize=True)
    return -np.sum(p * np.log2(p))

def info_gain(df, root, attribute):
    root_entropy = entropy(df[root])
    branch_entropies = df.groupby(attribute).apply(lambda group: entropy(group[root]))
    branch_weights = df[attribute].value_counts(normalize=True)
    
    weighted_entropy = np.sum(branch_weights * branch_entropies)
    return root_entropy - weighted_entropy

def choose_attribute(df, root, attributes):
    gains = {attr: info_gain(df, root, attr) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    return best_attr, gains[best_attr]


# Choose the best attribute for each branch of X1
root = 'Y'
attributes = ['X2', 'X3']

for branch_value in df['X1'].unique():
    branch_df = df[df['X1'] == branch_value]

    best_attr, gain = choose_attribute(branch_df, root, attributes)

    print(f"Branch X1 = {branch_value}:")
    print(f"Best attribute: {best_attr} with information gain: {gain:.5f}")
    print()


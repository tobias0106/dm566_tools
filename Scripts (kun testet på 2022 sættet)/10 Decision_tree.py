import pandas as pd
from typing import List


## Used for 10/20 in the 2022 exam
## Adjust data as needed
# Load the data
data = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'X1': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
        'X2': ['C', 'C', 'D', 'D', 'C', 'C', 'D', 'C', 'D', 'C'],
        'X3': ['E', 'F', 'E', 'F', 'F', 'E', 'E', 'E', 'F', 'F'],
        'Y': [-1, 1, -1, 1, -1, -1, 1, 1, 1, -1]}
df = pd.DataFrame(data)

def gini_index(df: pd.DataFrame, attribute: str, value: str) -> float:
    total_count = len(df)
    value_count = len(df[df[attribute] == value])
    other_count = total_count - value_count

    if value_count == 0 or other_count == 0:
        return 0

    pos_value = len(df[(df[attribute] == value) & (df['Y'] == 1)])
    neg_value = value_count - pos_value

    pos_other = len(df[(df[attribute] != value) & (df['Y'] == 1)])
    neg_other = other_count - pos_other

    gini_value = 1 - (pos_value / value_count) ** 2 - (neg_value / value_count) ** 2
    gini_other = 1 - (pos_other / other_count) ** 2 - (neg_other / other_count) ** 2

    return (value_count / total_count) * gini_value + (other_count / total_count) * gini_other

def min_gini_attribute(df: pd.DataFrame, branch_value: str, attributes: List[str]) -> str:
    min_gini = float('inf')
    best_attribute = None

    for attribute in attributes:
        for value in df[attribute].unique():
            gini = gini_index(df[df['X1'] == branch_value], attribute, value)
            if gini < min_gini:
                min_gini = gini
                best_attribute = attribute

    return best_attribute

# Calculate the minimum Gini index attribute for each branch
attributes = ['X2', 'X3']
branch_A = min_gini_attribute(df, 'A', attributes)
branch_B = min_gini_attribute(df, 'B', attributes)

# Evaluate the statements
print(f"For the branch of X1 = B, it will select {branch_B}.")
print(f"For the branch of X1 = A, it will select {branch_A}.")

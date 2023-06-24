import pandas as pd
import numpy as np

def calculate_gini_index(data, branch, attribute):
    filtered_data = data[data['X1'] == branch]
    filtered_data_attribute = filtered_data['Y'].groupby(filtered_data[attribute]).value_counts().unstack().fillna(0)
    total_samples_attribute = filtered_data_attribute.sum(axis=1)
    class_probabilities_attribute = filtered_data_attribute.div(total_samples_attribute, axis=0)
    gini_index_attribute = 1.0 - np.sum(class_probabilities_attribute ** 2, axis=1)
    weighted_gini_index_attribute = np.sum(gini_index_attribute * (total_samples_attribute / total_samples_attribute.sum()))
    return weighted_gini_index_attribute

# Create the dataset
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X1': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'X2': ['C', 'C', 'D', 'D', 'C', 'C', 'D', 'C', 'D', 'C'],
    'X3': ['E', 'F', 'E', 'F', 'F', 'E', 'E', 'E', 'F', 'F'],
    'Y': [-1, 1, -1, 1, -1, -1, 1, 1, 1, -1]
}

df = pd.DataFrame(data)

# Calculate Gini index for Branch X1 = A and attribute X2
gini_index_x2_A = calculate_gini_index(df, 'A', 'X2')

# Calculate Gini index for Branch X1 = A and attribute X3
gini_index_x3_A = calculate_gini_index(df, 'A', 'X3')

# Calculate Gini index for Branch X1 = B and attribute X2
gini_index_x2_B = calculate_gini_index(df, 'B', 'X2')

# Calculate Gini index for Branch X1 = B and attribute X3
gini_index_x3_B = calculate_gini_index(df, 'B', 'X3')

# Determine the suggested attribute to select for each branch
suggested_attribute_A = 'X2' if gini_index_x2_A < gini_index_x3_A else 'X3'
suggested_attribute_B = 'X2' if gini_index_x2_B < gini_index_x3_B else 'X3'

print("Gini Index (Branch X1 = A, Splitting on X2):", gini_index_x2_A)
print("Gini Index (Branch X1 = A, Splitting on X3):", gini_index_x3_A)
print("Gini Index (Branch X1 = B, Splitting on X2):", gini_index_x2_B)
print("Gini Index (Branch X1 = B, Splitting on X3):", gini_index_x3_B)

print("For the branch of X1 = A, it will select", suggested_attribute_A)
print("For the branch of X1 = B, it will select", suggested_attribute_B)


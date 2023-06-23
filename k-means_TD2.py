import pandas as pd
import numpy as np

#WARNING THIS SCRIPT IS ONLY TESED FOR MADS 2020 MCQ
# Define the dataset
data = {
    'ID': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Value': [1, 3, 5, 7, 10, 11, 12]
}

df = pd.DataFrame(data)

# Define the clustering solutions
solutions = [
    [['A', 'B', 'C'], ['D', 'E', 'F', 'G']],
    [['A', 'B'], ['C', 'D'], ['E', 'F', 'G']],
    [['A', 'B', 'C', 'D'], ['E', 'F', 'G']]
]

# Calculate the TD^2 for each solution
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    total_td2 = 0
    
    for cluster in solution:
        centroid = np.mean(df[df['ID'].isin(cluster)]['Value'])
        td2 = sum((df[df['ID'].isin(cluster)]['Value'] - centroid) ** 2)
        print(f"Cluster {cluster}: Centroid = {centroid:.2f}, TD^2 = {td2:.2f}")
        total_td2 += td2
        
    print(f"Total TD^2 = {total_td2:.2f}\n")

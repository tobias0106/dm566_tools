import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.tree import export_graphviz
import six
import sys
sys.modules['sklearn.externals.six'] = six

# Sample data
data = {
    'RID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'forecast': ['sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'rainy', 'rainy', 'rainy'],
    'humidity': ['high', 'high', 'high', 'normal', 'normal', 'high', 'normal', 'normal', 'normal', 'high'],
    'wind': ['weak', 'strong', 'weak', 'weak', 'strong', 'weak', 'weak', 'weak', 'strong', 'strong'],
    'play tennis?': ['no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'no']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the features and their corresponding mapping
features_mapping = {
    'forecast': {'sunny': 0, 'rainy': 1},
    'humidity': {'high': 0, 'normal': 1},
    'wind': {'weak': 0, 'strong': 1}
}

# Convert categorical variables into numerical values based on the mapping
for feature, mapping in features_mapping.items():
    df[feature] = df[feature].map(mapping)

# Separate features and target variable
features = ['forecast', 'humidity', 'wind']
X = df[features]
y = df['play tennis?']

best_gini = float('inf')
best_feature = None

# Iterate over features and select the one with the lowest Gini index
for feature in features:
    X_feature = X[feature].values.reshape(-1, 1)
    dt_classifier = DecisionTreeClassifier()
    dt_classifier.fit(X_feature, y)
    gini = dt_classifier.tree_.impurity[0]

    if gini < best_gini:
        best_gini = gini
        best_feature = feature

# Output the selected feature and its Gini index
print(f"The root feature is '{best_feature}' with a Gini index of {best_gini}")

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
    'Past Trend': ['Positive', 'Negative', 'Positive', 'Positive', 'Negative', 'Positive', 'Negative', 'Negative', 'Positive', 'Positive'],
    'Open Interest': ['Low', 'High', 'Low', 'High', 'Low', 'Low', 'High', 'Low', 'Low', 'High'],
    'Trading Volume': ['High', 'Low', 'High', 'High', 'High', 'Low', 'High', 'High', 'Low', 'High'],
    'Return': ['Up', 'Down', 'Up', 'Up', 'Down', 'Down', 'Down', 'Down', 'Down', 'Up']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the features and their corresponding mapping
features_mapping = {
    'Past Trend': {'Positive': 0, 'Negative': 1},
    'Open Interest': {'Low': 0, 'High': 1},
    'Trading Volume': {'Low': 0, 'High': 1}
}

# Convert categorical variables into numerical values based on the mapping
for feature, mapping in features_mapping.items():
    df[feature] = df[feature].map(mapping)

# Separate features and target variable
features = ['Past Trend', 'Open Interest', 'Trading Volume']
X = df[features]
y = df['Return']

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

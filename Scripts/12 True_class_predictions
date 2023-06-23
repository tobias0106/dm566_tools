from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

## Used for page 12/20 in the 2022 exam


## change the values below as needed
true_labels = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C']
predictions = ['B', 'A', 'C', 'A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'A', 'B', 'B', 'C']

# Calculate metrics
precision = precision_score(true_labels, predictions, average=None, labels=['A', 'B', 'C'])
recall = recall_score(true_labels, predictions, average=None, labels=['A', 'B', 'C'])

statements = [
    ("precision for class B is larger than precision for class C", precision[1] > precision[2]),
    ("recall for class B is larger than precision for class B", recall[1] > precision[1]),
    ("recall for class A is larger than recall for class B", recall[0] > recall[1]),
    ("precision for class C is larger than recall for class C", precision[2] > recall[2]),
    ("precision for class A is larger than precision for class C", precision[0] > precision[2]),
    ("precision for class A is larger than recall for class A", precision[0] > recall[0]),
    ("recall for class B is larger than recall for class C", recall[1] > recall[2]),
]

for statement, result in statements:
    print(f"{statement}: {'True' if result else 'False'}")

from sklearn.metrics import confusion_matrix, classification_report

# true class of the test objects   
y_true = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C']

# predicted class by the classifier
y_pred = ['B', 'A', 'C', 'A', 'B', 'A', 'C', 'B', 'A', 'A', 'C', 'A', 'B', 'B', 'C']

# calculate the confusion matrix
cm = confusion_matrix(y_true, y_pred)

# print the confusion matrix
print("Confusion matrix:")
print(cm)

# calculate the classification report which includes precision, recall, f1-score and support
cr = classification_report(y_true, y_pred)

# print the classification report
print("Classification report:")
print(cr)

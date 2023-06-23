# Models will be need to change depending on the table in the exam
# This script can be used for the problem on page 9/20 in the 2022 exam
models = [
    {"name": "Model 1", "train_error": 0.27, "test_error": 0.27, "parameters": 1},
    {"name": "Model 2", "train_error": 0.12, "test_error": 0.15, "parameters": 2},
    {"name": "Model 3", "train_error": 0.05, "test_error": 0.07, "parameters": 3},
    {"name": "Model 4", "train_error": 0.05, "test_error": 0.07, "parameters": 4},
    {"name": "Model 5", "train_error": 0.03, "test_error": 0.30, "parameters": 5},
]

def has_overfitted_most(model):
    return model["train_error"] < model["test_error"]

def has_underfitted_compared_to(model1, model2):
    return model1["train_error"] > model2["train_error"]

def has_highest_test_accuracy_per_unit_cost(model):
    accuracy_per_unit_cost = [1 - m["test_error"] / m["parameters"] for m in models]
    max_accuracy_per_unit_cost = max(accuracy_per_unit_cost)
    return (1 - model["test_error"] / model["parameters"]) == max_accuracy_per_unit_cost

"""
statements = [
    ("Model 4 has over-fitted most", has_overfitted_most(models[3])),
    ("Model 5 has under-fitted compared to Model 1", has_underfitted_compared_to(models[4], models[0])),
    ("Model 3 gives the highest test accuracy per unit prediction-time computational cost", has_highest_test_accuracy_per_unit_cost(models[2])),
    ("Model 5 has over-fitted most", has_overfitted_most(models[4])),
    ("Model 1 has under-fitted compared to Model 2", has_underfitted_compared_to(models[0], models[1])),
    ("Model 1 has over-fitted most", has_overfitted_most(models[0])),
    ("Model 4 gives the highest test accuracy per unit prediction-time computational cost", has_highest_test_accuracy_per_unit_cost(models[3])),
]

for statement, result in statements:
    print(f"{statement}: {'True' if result else 'False'}")
"""


# Name : "Model 1" = models[0]
print(has_overfitted_most(models[3]))
#### Used for page 8/20 in the 2022 exam


# Classifiers probabilities given training data
h1_prob = 0.4
h2_prob = 0.2
h3_prob = 0.4

# Test instances class probabilities given classifiers
o1_probs = [
    {"+": 0.5, "-": 0.5},
    {"+": 0.6, "-": 0.4},
    {"+": 0.3, "-": 0.7},
]
o2_probs = [
    {"+": 0.2, "-": 0.8},
    {"+": 0.9, "-": 0.1},
    {"+": 0.7, "-": 0.3},
]
o3_probs = [
    {"+": 0.3, "-": 0.7},
    {"+": 0.0, "-": 1.0},
    {"+": 0.4, "-": 0.6},
]

def bayes_optimal_probabilities(instance_probs, h_probs):
    pos_numerator = sum([instance_probs[i]["+"] * h_probs[i] for i in range(len(h_probs))])
    neg_numerator = sum([instance_probs[i]["-"] * h_probs[i] for i in range(len(h_probs))])
    denominator = sum(h_probs)

    pos_bayes_optimal = pos_numerator / denominator
    neg_bayes_optimal = neg_numerator / denominator

    return {"+": pos_bayes_optimal, "-": neg_bayes_optimal}

h_probs = [h1_prob, h2_prob, h3_prob]
o1_bayes_optimal = bayes_optimal_probabilities(o1_probs, h_probs)
o2_bayes_optimal = bayes_optimal_probabilities(o2_probs, h_probs)
o3_bayes_optimal = bayes_optimal_probabilities(o3_probs, h_probs)

print("o1 Bayes Optimal:", o1_bayes_optimal)
print("o2 Bayes Optimal:", o2_bayes_optimal)
print("o3 Bayes Optimal:", o3_bayes_optimal)

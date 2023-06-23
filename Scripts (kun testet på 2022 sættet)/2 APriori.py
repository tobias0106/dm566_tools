import pandas as pd
from mlxtend.frequent_patterns import apriori

## Used for page 2/20 in 2022 exam
## Will only find frequent subsets, not closed freaquent.

data = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1]
]

columns = ['A', 'B', 'C', 'D', 'E']
transactions = pd.DataFrame(data, columns=columns)

def find_closed_frequent_itemsets(transactions, support_threshold):
    frequent_itemsets = apriori(transactions, min_support=support_threshold, use_colnames=True)
    closed_frequent_itemsets = frequent_itemsets.copy()
    
    for idx, row in frequent_itemsets.iterrows():
        itemset_superset = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: x.issuperset(row['itemsets']))]
        if any(itemset_superset['support'] > row['support']):
            closed_frequent_itemsets = closed_frequent_itemsets.drop(idx)
    
    return closed_frequent_itemsets


support_threshold = 4 / len(transactions)
closed_frequent_itemsets = find_closed_frequent_itemsets(transactions, support_threshold)
print(closed_frequent_itemsets)


def is_closed_frequent(itemset, closed_frequent_itemsets):
    itemset = frozenset(itemset)
    return any(closed_frequent_itemsets['itemsets'].apply(lambda x: x == itemset))


itemset_ab = {'A', 'B'}
result = is_closed_frequent(itemset_ab, closed_frequent_itemsets)
print(f"Itemset {itemset_ab} is closed frequent: {result}")

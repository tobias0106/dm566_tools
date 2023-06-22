import numpy as np

table = np.array([['A', 'D', "+1"],
         ['B', 'D', "-1"],
         ['A', 'E', "+1"],
         ['C', 'D', "-1"],
         ['B', 'E', "-1"],
         ['A', 'E', "+1"],
         ['B', 'D', "+1"],
         ['C', 'D', "-1"],
         ['A', 'D', "-1"]
])

mappedValues = {
    'A': [0, 0],
    'B': [0, 0],
    'C': [0, 0],
    'D': [0, 0],
    'E': [0, 0]
}

numOfPos = 0
numOfNeg = 0

for row in table:
    if row[2] == "-1":
        numOfNeg += 1
        mappedValues[row[0]][1] += 1
        mappedValues[row[1]][1] += 1
    else:
        numOfPos += 1
        mappedValues[row[0]][0] += 1
        mappedValues[row[1]][0] += 1

queries = np.array([['B', 'E'], ['C', 'E'], ['A', 'D'], ['B', 'D']])

totalElems = numOfPos + numOfNeg
for query in queries:
    totalElemsOfFirst = mappedValues[query[0]][0] + mappedValues[query[0]][1]
    totalElemsOfSecond = mappedValues[query[1]][0] + mappedValues[query[1]][1]

    prFirstPlus = mappedValues[query[0]][0] / totalElemsOfFirst
    prFirstMinus = mappedValues[query[0]][1] / totalElemsOfFirst

    prSecondPlus = mappedValues[query[1]][0] / totalElemsOfSecond
    prSecondMinus = mappedValues[query[1]][1] / totalElemsOfSecond

    prPlus = numOfPos / totalElems
    prMinus = numOfNeg / totalElems

    
    calcPlus = prFirstPlus * prSecondPlus * prPlus
    calcMinus = prFirstMinus * prSecondMinus * prMinus

    classified = calcPlus/(calcPlus + calcMinus)

    print("for +1 pr of query: ", query, "is: ", classified)

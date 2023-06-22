# Modify these
props = [0.4, 0.2, 0.4]

# Modify these
o1 = [0.5, 0.6, 0.3]
o2 = [0.2, 0.9, 0.7]
o3 = [0.3, 0.0, 0.4]

# adjust to how many o's
sum1 = 0
sum2 = 0
sum3 = 0

# Modify this if more than 3 o's
for i in range(len(props)):
    sum1 += props[i] * o1[i]
    sum2 += props[i] * o2[i]
    sum3 += props[i] * o3[i]

print("for first class")
print("o1: ",sum1)
print("o2: ",sum2)
print("o3: ",sum3)
print()
print("for second class")
print("o1: ", 1-sum1)
print("o2: ", 1-sum2)
print("o3: ", 1-sum3)

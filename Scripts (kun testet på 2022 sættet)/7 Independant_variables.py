import numpy as np
import fractions

##### Used for page 7/20 in the 2022 exam

# Taking user input for dice and sides
dice1 = int(input("Enter the number of dice for the first set: "))
sides1 = int(input("Enter the number of sides for the first set of dice: "))
dice2 = int(input("Enter the number of dice for the second set: "))
sides2 = int(input("Enter the number of sides for the second set of dice: "))

# Taking user input for value and operator
value = int(input("Enter value to compare with: "))
operator = input("Enter the comparison operator (>, <, or =): ")

# Generating xvalues and yvalues based on user input
xvalues = np.arange(1, sides1 + 1)
yvalues = np.arange(1, sides2 + 1)

# Calculating the probability for each combination of xvalues and yvalues
probability_count = 0
total_combinations = len(xvalues) * len(yvalues)

for x in xvalues:
    for y in yvalues:
        if operator == ">":
            if x + y > value:
                probability_count += 1
        elif operator == "<":
            if x + y < value:
                probability_count += 1
        elif operator == "=":
            if x + y == value:
                probability_count += 1
        else:
            print("Invalid comparison operator.")
            exit()

# Calculate the probability based on the count of valid combinations
probability = probability_count / total_combinations

# Convert the probability to a Fraction object
fraction_probability = fractions.Fraction(probability).limit_denominator()

# Convert the Fraction object to a decimal value
decimal_probability = float(fraction_probability)

print(f"Pr[Z{operator}{value}]={fraction_probability} (fraction), {decimal_probability} (decimal)")

from fractions import Fraction

numerator = 0
bigger_than_five = 0
equal_seven = 0
equal_four = 0
less_than_seven = 0

denominator = 0

for x in range(1, 7):
    for y in range(1, 9):
        z = x + y
        if z > 5:
            bigger_than_five += 1
        if z == 7:
            equal_seven += 1
        if z == 4:
            equal_four += 1
        if z < 7:
            less_than_seven += 1
        denominator += 1

# Make all result a fraction_result
result_bigger_than_five = Fraction(bigger_than_five, denominator)
result_equal_seven = Fraction(equal_seven, denominator)
result_equal_four = Fraction(equal_four, denominator)
result_less_than_seven = Fraction(less_than_seven, denominator)

# print all result
print("Pr[Z > 5]: bigger_than_five: ", result_bigger_than_five)
print("Pr[Z = 7]: equal_seven: ", result_equal_seven)
print("Pr[Z = 4]: equal_four: ", result_equal_four)
print("Pr[Z < 7]: less_than_seven: ", result_less_than_seven)

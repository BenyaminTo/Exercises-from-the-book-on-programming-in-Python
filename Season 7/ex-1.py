from fractions import Fraction

class Rational(object):
    def __init__(self, numerator1, denominator1, numerator2, denominator2):
        self.frac1 = Fraction(numerator1, denominator1)
        self.frac2 = Fraction(numerator2, denominator2)

    def sum_fraction(self):
        return self.frac1 + self.frac2

    def sub_fraction(self):
        return self.frac1 - self.frac2

    def mul_fraction(self):
        return self.frac1 * self.frac2

    def div_fraction(self):
        return self.frac1 / self.frac2

# User input for fractions
numerator1 = int(input("Enter the numerator of the first fraction: "))
denominator1 = int(input("Enter the denominator of the first fraction: "))
numerator2 = int(input("Enter the numerator of the second fraction: "))
denominator2 = int(input("Enter the denominator of the second fraction: "))

# Create an instance of the Rational class
rational_instance = Rational(numerator1, denominator1, numerator2, denominator2)

# Print the results
print(f"Sum of the two fractions: {rational_instance.sum_fraction()}")
print(f"Subtraction of the two fractions: {rational_instance.sub_fraction()}")
print(f"Multiplication of the two fractions: {rational_instance.mul_fraction()}")
print(f"Division of the two fractions: {rational_instance.div_fraction()}")



        
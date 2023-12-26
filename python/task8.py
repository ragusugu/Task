from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map to square each element
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)

# Using filter to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Using reduce to calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)

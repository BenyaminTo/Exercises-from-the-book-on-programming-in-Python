import random

def generate_random_numbers(num_of_numbers, range_start, range_end):
    random_numbers = [random.randint(range_start, range_end) for _ in range(num_of_numbers)]
    return random_numbers
###############################################################################
num_of_numbers = 10
range_start = -100
range_end = 100
numbers = list()
numbers = generate_random_numbers(num_of_numbers, range_start, range_end)
print("Random numbers:", numbers)
negative_numbers = list()

negative_numbers = [num for num in numbers if num < 0]

numbers = [num for num in numbers if num >= 0]
        
print("Negative numbers:", negative_numbers)
print("Positive numbers:", numbers)

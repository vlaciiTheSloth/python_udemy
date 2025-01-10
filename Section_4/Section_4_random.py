# importing the 'random' module
# you can create your own modules, and import them the same way as this instance
import random

# randint: random integer number -> parameters: minimum and maximum-> providing the range
random_integer = random.randint(1,10)
print(random_integer)

# random: random float number between 0.0 <= x < 1.0
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

#uniform: random float number between a <= x <= b
random_float = random.uniform(1,10)
print(random_float)

# Heads or tails?
if random.randint(0,1) == 0:
    print("Heads")
else:
    print("Tails")
 


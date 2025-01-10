#TASK: Choose one person from a group of friends who pays the bill for everyone!

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randnum = random.randint(0,4)
print(friends[randnum])

#another solution:
print(random.choice(friends)) #random.choice is a function that chooses a random element from a list
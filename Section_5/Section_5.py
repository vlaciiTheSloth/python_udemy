# Section 5 - Loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

# the sum() function basically iterates over every element of a list and adds them together. If we would manually create it though, it would look like this:
sum = 0
for score in student_scores:
    sum += score
print(sum)

print(max(student_scores))
#the max() function picks out the largest number out of a list. Recreating this with a loop:
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)

# range() function -> defining a minimum and maximum value to iterate over (upper value is not exclusive!) (by defininf a 3rd value, you can define the steps)
for number in range(1, 11, 3):
    print(number)

# Gauss challange: adding the number up from 1 to 100
gauss_total = 0
for number in range (1, 101):
    gauss_total += number
print(gauss_total)
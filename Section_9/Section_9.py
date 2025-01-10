# Dictionaries

programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over.",
    }

print(programming_dictionary["Function"])

# adding data to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Wiping a dictionary
# programming_dictionary = {}

# Edit an item in a dictionary -> same way as adding a new entry
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# ---------------------------------------
# Coding exercise from Udemy

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Outstanding"

print(student_grades)
# -----------------------------------
# Nesting

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}

# print "Lille" from travel_log
print(travel_log["France"][1])

nested_list = ["A", "B" , ["C", "D"]]

#print D from nested_list
print(nested_list[2][1])

# making it more complex

travel_log2 = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg" , "Suttgart"],
        "total_visits" : 5
    },
}

print(travel_log2["Germany"]["cities_visited"][2])
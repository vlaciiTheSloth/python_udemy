def greet():
    print("Hello!")
    print("I hope you're doing well today!")
    print("Have a nice rest of the week!")

greet()

#functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Angela")

def life_in_weeks(age):
    remaining_weeks = (90*52) - (age * 52)
    print(f"You have {remaining_weeks} weeks left.")

life_in_weeks(23)

#functions that allows more than 1 parameter

def greet_with_name_location(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with_name_location("Laci", "Debrecen") # positional arguments

greet_with_name_location(location = "Debrecen", name = "Laci")
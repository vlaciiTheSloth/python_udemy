# Functions - now with outputs

def format_name(f_name, l_name):
    # docstring usage: you can define custom documentation to your own custom functions by declaring it in the first line of the function itself, between three quotation marks.
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"
    
print(format_name(input("What is your first name? "), input("What is your last name? ")))

# ----------------------------------

def function_1(text):
    return text + text

def function_2 (text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

# Udemy exercise ------------
def is_leap_year(year):
    """Returns a boolean value whether the given year is a leap year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2024))
# ---------------------------
        
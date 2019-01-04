number = 5

if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")

#Notice that the if and else statements must end in a colon

number = 5
if number:
    print("Number is defined and truthy")

text = "python"
if text:
    print("Text is defined and is truthy")

#Some variables are truthy, and evaluate to true when evaluated in an if statement, assuming the variable exists.
#This is often used to check if variable exists

python_course = True
if python_course:
    print("This will execute")

aliens_found = None
if aliens_found:
    print("This will NOT execute")

#Not ifs are the same as in other languages
if number != 5:
    print("This will not execute")

# and or, not && ||

if number == 5 and python_course:
    print("This will execute")

#Ternary if statements
a = 1
b = 2
print("bigger" if a > b else "smaller")


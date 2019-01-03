'Hello World' == "Hello World" == """Hello World""" #Triple quotes are usually used for function or class documents.

"""Test
multi
line
string
"""
#The above string essentially serves as a comment. It is not assigned to a variable, 
#and IDEs will even recognize such strings as comments

"hello".capitalize() == "Hello"
"hello".replace("e", "a") == "hallo"
"hello".isalpha() == True
"123".isdigit() == True #Useful when converting to int

"some,csv,values".split(",") == ["some", "csv", "values"] #split string into list using specified argument

name = "AndrewRay"
machine = "Glados"

"Nice to meet you {0}. I am {1}".format(name, machine) #string.format. you've used it before Andrew

f"Nice to meet you {name}. I am {Machine}" #interpolation!

r"Raw String!"
u"Unicode String!"

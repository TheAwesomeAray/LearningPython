student_names = ["Andrew", "ARay", "AKRay"]

for name in student_names:
	print(f"Student name is {name}") #really more of a foreach loop

x = 0;
for index in range(10):
	x += 10
	print(f"The value of x is {x}") #Range creates a list - [0, 1, 2, 3, ..., 9]

range(5, 10) == [5, 6, 7, 8, 9, 10] #can choose a start point

range(5, 10, 2) #third argument represents the increment amount

x = 0;
for index in range(10):
	x += 10
	print(f"The value of x is {x}") #Range creates a list - [0, 1, 2, 3, ..., 9]
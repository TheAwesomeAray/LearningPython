student_names = [] #Empty python list

student_names = ["Andrew", "ARay", "AKRay"] #We've been here before

student_names[0] == "Andrew"
student_names[2] == "AKRay" #and here...

student_names[-1] == "AKRay" #But definitely not here! Negative index starts with -1

student_names[0] = "Imposter" #Standard assignment
student_names == ["Imposter", "ARay", "AKRay"]

student_names.append("Andrew") ##add item to list. Differ from an array here
"Andrew" in student_names == True #Check for value
len(student_names) == 4 #len can be used for many types, such as strings

del student_names[0] #Delete the imposter. Elements shift to the left

student_names[1:] == ["AKRay", "Andrew"] # list slicing. Does not modify the list, only reports a specific portion
#Lists can include many types




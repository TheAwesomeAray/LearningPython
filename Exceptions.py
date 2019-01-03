
student = {
    "name": "Andrew",
    "student_id": 1,
    "grade": "A"
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Error! Could not find last name.")


student["last_name"] = "Ray"

try:
    last_name = student["last_name"]
    print(last_name)
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error! Could not find last name.")
#except TypeError:
    #print("Error! Cannot add these types.")
except Exception:
    print("Unknown Error!")

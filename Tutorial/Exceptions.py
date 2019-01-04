
student = {
    "name": "Andrew",
    "student_id": 1,
    "grade": "A"
}

try:
    last_name = student["last_name"]
except KeyError as error:
    print("Error! Could not find last name. {0}".format(error))


student["last_name"] = "Ray"

try:
    last_name = student["last_name"]
    print(last_name)
    numbered_last_name = 3 + last_name
except KeyError as error:
    print("Error! Could not find last name.")
except TypeError as error:
    print("Error! Cannot add these types.")
    print(error)
except Exception:
    print("Unknown Error!")

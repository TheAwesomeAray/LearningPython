studentDictionary = {
    "name": "Andrew",
    "student_id": 1,
    "grade": "A"
}

ListOfStudentDictionaries = [
    { "name": "Andrew", "student_id": 1, "grade": "A" },
    { "name": "Bob", "student_id": 2, "grade": "B" },
    { "name": "Kendall", "student_id": 3, "grade": "A+" }
]



for item in ListOfStudentDictionaries:
    print(f"{item['name']} has grade {item['grade']}")


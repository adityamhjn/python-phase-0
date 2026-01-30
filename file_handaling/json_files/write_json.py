import json

student = {
    "name": "Aditya",
    "cgpa": 9.66,
    "branch": "CSE"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")

import json
import os

file_path = os.path.join(os.path.dirname(__file__), "student.json")

with open(file_path, "r") as file:
    data = json.load(file)

print(data)

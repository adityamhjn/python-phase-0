data = [
    {"name": "Aman", "marks": 85},
    {"name": "Riya", "marks": 92},
    {"name": "Karan", "marks": 78}
]

total = 0
for student in data:
    total += student["marks"]

average = total / len(data)
print("Average marks:", average)

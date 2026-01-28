students = [
    ("Aman", "CSE"),
    ("Riya", "ECE"),
    ("Karan", "CSE"),
    ("Neha", "ECE")
]

groups = {}

for name, branch in students:
    if branch not in groups:
        groups[branch] = []
    groups[branch].append(name)

print(groups)

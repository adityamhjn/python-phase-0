students = {
    "Aman": {"marks": 85, "branch": "CSE"},
    "Riya": {"marks": 92, "branch": "ECE"},
    "Karan": {"marks": 78, "branch": "CSE"}
}

# Print students scoring above 80
for name, info in students.items():
    if info["marks"] > 80:
        print(name, info)

scores = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78
}

# Update
scores["Aman"] = 88

# Iterate
for name, marks in scores.items():
    print(name, marks)
# Add
scores["Neha"] = 95
# Delete
del scores["Karan"]
# Print final dictionary
print(scores)
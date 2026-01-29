import csv

data = [
    ["Name", "Marks"],
    ["Aman", 85],
    ["Riya", 92],
    ["Karan", 78]
]

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV written successfully.")
# This code writes a CSV file named "results.csv" with student names and their marks.
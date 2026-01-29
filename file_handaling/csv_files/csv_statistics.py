import csv

total = 0
count = 0
highest = 0
topper = ""

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            marks = int(row["Marks"])
        except (ValueError, KeyError):
            # Skip rows with missing or invalid marks
            continue
        total += marks
        count += 1

        if marks > highest:
            highest = marks
            topper = row["Name"]

if count > 0:
    average = total / count
    print("Average marks:", average)
    print("Topper:", topper, highest)
else:
    print("No student records found in 'students.csv'. Cannot compute statistics.")
# This code reads a CSV file named "students.csv", calculates the average marks, and identifies the student with the highest marks.
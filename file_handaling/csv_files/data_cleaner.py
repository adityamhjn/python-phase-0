import csv

cleaned_rows = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row.get("grade") != "":
            cleaned_rows.append(row)

with open("cleaned_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=cleaned_rows[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_rows)

print("Data cleaned and saved.")

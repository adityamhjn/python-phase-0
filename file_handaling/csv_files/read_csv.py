import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# This code reads a CSV file named "students.csv" and prints each row to the console.
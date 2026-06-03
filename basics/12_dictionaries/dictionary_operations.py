"""
12. DATA STRUCTURE - DICTIONARY
Learning: How to use Dictionary, add, delete, search in Dictionary
"""

# 12.1 Declare Dictionary
print("=== 12.1 Declare Dictionary ===")
CGPA = {1: 8.9, 2: 5.6, 4: 6.7, 7: 9.1, 8: 5.3}
print("Dictionary      --> ", CGPA)
print("Num of elements --> ", len(CGPA))
print("CGPA of 1       --> ", CGPA[1])
print("CGPA of 4       --> ", CGPA[4])
print("CGPA of 7       --> ", CGPA[7])

# 12.2 Traverse dictionary
print("\n=== 12.2 Traverse Dictionary ===")
CGPA = {1: 8.9, 2: 5.6, 4: 6.7, 7: 9.1, 8: 5.3}
for k in CGPA:
    print("CGPA of ", k, " --> ", CGPA[k])

# 12.3 Getting Keys and Values
print("\n=== 12.3 Getting Keys and Values ===")
CGPA = {1: 8.9, 2: 5.6, 4: 6.7, 7: 9.1, 8: 5.3}
print("Dictionary --> ", CGPA)
print("Keys       --> ", list(CGPA.keys()))
print("Values     --> ", list(CGPA.values()))

# 12.4 Updating, Adding and Deleting
print("\n=== 12.4 Update, Add, Delete from Dictionary ===")
CGPA = {1: 8.9, 2: 5.6, 4: 6.7, 7: 9.1, 8: 5.3}
print("Original Dictionary --> ", CGPA)
CGPA[4] = 9.2
print("After Updating (4)  --> ", CGPA)
CGPA[3] = 8.6
print("After Adding (3)    --> ", CGPA)
del CGPA[1]
print("After Deleting (1)  --> ", CGPA)
CGPA.clear()
print("After Clear         --> ", CGPA)

# 12.5 Checking for Key
print("\n=== 12.5 Checking for Key ===")
CGPA = {1: 8.9, 2: 5.6, 4: 6.7, 7: 9.1, 8: 5.3}
print("Original Dictionary --> ", CGPA)
print("Is Key 2 Present    --> ", 2 in CGPA)
print("Is Key 9 Present    --> ", 9 in CGPA)

# 12.6 More example 1
print("\n=== 12.6 Example - HomeTown ===")
HomeTown = {"Prashant": "Delhi", "Govind": "Gwalior", "Anil": "Morena", "Pankaj": "Agra"}
print("Original Dictionary --> ", HomeTown)
print("Home Town of Prashant is --> ", HomeTown["Prashant"])
print("Home Town of Govind is   --> ", HomeTown["Govind"])
print("Home Town of Anil is     --> ", HomeTown["Anil"])
print("Home Town of Pankaj is   --> ", HomeTown["Pankaj"])

# 12.7 More example 2 - Iterate
print("\n=== 12.7 Iterate Over Dictionary ===")
HomeTown = {"Prashant": "Delhi", "Govind": "Gwalior", "Anil": "Morena", "Pankaj": "Agra"}
print("Original Dictionary --> ", HomeTown)
for d in HomeTown:
    print("Home Town of ", d, " is  --> ", HomeTown[d])

"""
11. DATA STRUCTURE - LIST
Learning: How to use list, add, delete and search in the list
"""

# 11.1 List Declaration
print("=== 11.1 List Declaration ===")
L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List: ", L)
print("Number of elements in list: ", len(L))

# 11.2 List Iteration - While loop
print("\n=== 11.2 List Iteration - While Loop ===")
L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List: ", L)
i = 0
while i < len(L):
    print(L[i])
    i += 1

# 11.3 List Iteration - For loop with range
print("\n=== 11.3 List Iteration - For Loop with Range ===")
L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List: ", L)
for i in range(0, len(L)):
    print(L[i])

# 11.4 List Iteration - Direct for loop
print("\n=== 11.4 List Iteration - Direct For Loop ===")
L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List --> ", L)
for s in L:
    print(s)

# 11.5 Adding and deleting from list
print("\n=== 11.5 Add and Delete from List ===")
L = ["Pratham", 'Sharma', 3.14, 3]
print("Original List       --> ", L)
L.append("Rahul")
print("List After Adding   --> ", L)
del L[1]
print("List After Deleting --> ", L)

# 11.6 Sum/Average of List
print("\n=== 11.6 Sum and Average of List ===")
L = [3, 6, 9, 12, 5, 3, 2]
print("Original List --> ", L)
print("Sum     --> ", sum(L))
print("Average --> ", sum(L) / len(L))
print("Average --> ", sum(L) // len(L))
print("L * 3   --> ", L * 3)
print("L + L   --> ", L + L)

# 11.7 Min/Max/Sort the list
print("\n=== 11.7 Min/Max/Sort ===")
L = [3, 6, 9, 12, 5, 3, 2]
print("Original List --> ", L)
print("max --> ", max(L))
print("min --> ", min(L))
print("\nBefore Sort            --> ", L)
L.sort()
print("After Sort (Ascending)  --> ", L)
L.sort(reverse=True)
print("After Sort (Descending) --> ", L)

# 11.8 Merge lists and select elements
print("\n=== 11.8 Merge and Select Elements ===")
L1 = [3, 6, 9]
L2 = [12, 5, 3, 2]
L3 = L1 + L2
print("L1 --> ", L1)
print("L2 --> ", L2)
print("L3 --> ", L3)
print("\nL3[2:]  --> ", L3[2:])
print("L3[2:5] --> ", L3[2:5])
print("L3[:-1] --> ", L3[:-1])
print("L3[::2] --> ", L3[::2])

# 11.9 Multiply all elements by constant
print("\n=== 11.9 Multiply All Elements by Constant ===")
L = [12, 5, 3, 2, 7]
print("Original List --> ", L)
newL = [i * 5 for i in L]
print("After Multiply with constant --> ", newL)

# 11.10 Searching in the list
print("\n=== 11.10 Searching in List ===")
L = [3, 6, 9, 12, 5, 3, 2]
print("6 in L -->", 6 in L)
print("10 in L -->", 10 in L)
print("12 in L -->", 12 in L)

if (6 in L) == True:
    print("Present")
else:
    print("Not Present")

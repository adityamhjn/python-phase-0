"""
13. DATA STRUCTURE - TUPLE
Learning: How to use Tuple, add, delete, search in Tuple
Note: Tuples are immutable (unchangeable)
"""

# 13.1 Declare Tuple - Method 1
print("=== 13.1 Declare Tuple - Method 1 ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T               -->", T)
print("Num of elements -->", len(T))
print("Type of Object  -->", type(T))

# 13.1 Declare Tuple - Method 2
print("\n=== 13.1 Declare Tuple - Method 2 (from List) ===")
T = tuple(["Pratham", 'Sharma', 3.14, 3])
print("T               -->", T)
print("Num of elements -->", len(T))
print("Type of Object  -->", type(T))

# 13.2 Tuple Iteration - While loop
print("\n=== 13.2 Tuple Iteration - While Loop ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T -->", T)
i = 0
while i < len(T):
    print(T[i])
    i += 1

# 13.3 Tuple iteration - For loop with range
print("\n=== 13.3 Tuple Iteration - For Loop with Range ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T -->", T)
for i in range(0, len(T)):
    print(T[i])

# 13.4 Tuple iteration - Direct for loop
print("\n=== 13.4 Tuple Iteration - Direct For Loop ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T -->", T)
for s in T:
    print(s)

# 13.5 Accessing/Selecting in Tuple - Example 1
print("\n=== 13.5.1 Accessing Elements ===")
T = (3, 6, 9, 12, 5, 3, 2)
print("T     -->", T)
print("T[1]  -->", T[1])
print("T[2]  -->", T[2])
print("T[-1] -->", T[-1])
print("T[-2] -->", T[-2])

# 13.5 Accessing/Selecting in Tuple - Example 2
print("\n=== 13.5.2 Slicing Tuples ===")
T = (3, 6, 9, 12, 5, 3, 2)
print("T        -->", T)
print("T[1:3]   -->", T[1:3])
print("T[2:]    -->", T[2:])
print("T[2:5]   -->", T[2:5])
print("T[:2]    -->", T[:2])
print("T[:-1]   -->", T[:-1])
print("T[-4:-1] -->", T[-4:-1])

# 13.6 Sum/Average of Tuple
print("\n=== 13.6 Sum and Average ===")
T = (3, 6, 9, 12, 5, 3, 2)
print("T       -->", T)
print("Sum     -->", sum(T))
print("Average -->", sum(T) / len(T))
print("Average -->", sum(T) // len(T))

# 13.7 Min/Max in Tuple - Example 1
print("\n=== 13.7.1 Min/Max - Numbers ===")
T = (3, 6, 9, 12, 5, 3, 2)
print("T   -->", T)
print("Max -->", max(T))
print("Min -->", min(T))

# 13.7 Min/Max in Tuple - Example 2
print("\n=== 13.7.2 Min/Max - Strings ===")
T = ("Ram", "Shyam", "Human", "Ant")
print("T   -->", T)
print("Max -->", max(T))
print("Min -->", min(T))

# 13.8 Merging Tuples
print("\n=== 13.8 Merging Tuples ===")
T1 = (3, 6, 9)
T2 = (12, 5, 3, 2)
print("T1 -->", T1)
print("T2 -->", T2)
T3 = T1 + T2
print("T3 -->", T3)
T4 = T1 + T2 + T1 + T2
print("T4 -->", T4)

# 13.9 Merging part of Tuples
print("\n=== 13.9 Merging Part of Tuples ===")
T1 = (3, 6, 9)
T2 = (12, 5, 3, 2)
print("T1 -->", T1)
print("T2 -->", T2)
T3 = T1[1:2] + T2[1:3]
print("T3 -->", T3)
T4 = T1[:-2] + T2[:-3]
print("T4 -->", T4)

# 13.10 Searching in the tuple
print("\n=== 13.10 Searching in Tuple ===")
T = (3, 6, 9, 12, 5, 3, 2)
print("T       -->", T)
print("6  in T -->", 6 in T)
print("10 in T -->", 10 in T)
print("12 in T -->", 12 in T)

# 13.12 Adding element to Tuple (Workaround)
print("\n=== 13.12 Add Element to Tuple (Convert to List) ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T         -->", T)
T1 = list(T)
T1.append(9.8)
T = tuple(T1)
print("After Add -->", T)

# 13.13 Inserting element in Tuple (Workaround)
print("\n=== 13.13 Insert Element in Tuple ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T            -->", T)
T1 = list(T)
T1.insert(2, "Rahul")
T = tuple(T1)
print("After Insert -->", T)

# 13.15 Deleting from Tuple (Workaround)
print("\n=== 13.15 Delete from Tuple ===")
T = ("Pratham", 'Sharma', 3.14, 3)
print("T            -->", T)
T1 = list(T)
del T1[1]
T = tuple(T1)
print("After Delete -->", T)

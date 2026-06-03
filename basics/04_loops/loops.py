"""
4. LOOPS
Learning: Learn various loops (While, For, Range)
"""

# 4.1 While Loop - Print 1 to 10
print("=== 4.1 While Loop ===")
i = 1
while i <= 10:
    print(i)
    i = i + 1

# 4.2 Range Function
print("\n=== 4.2 Range Function ===")
print("range(10)        --> ", list(range(10)))
print("range(10,20)     --> ", list(range(10, 20)))
print("range(0,20,2)    --> ", list(range(2, 20, 2)))
print("range(-10,-20,2) --> ", list(range(-10, -20, 2)))
print("range(-10,-20,-2)--> ", list(range(-10, -20, -2)))

# 4.3.1 For loop - Version 1
print("\n=== 4.3.1 For Loop - Version 1 (0 to 10) ===")
for i in range(0, 10):
    print(i)

# 4.3.2 For loop - Version 2 (with step)
print("\n=== 4.3.2 For Loop - Version 2 (with step=2) ===")
for i in range(0, 20, 2):
    print(i)

# 4.3.3 For loop - Version 3 (negative)
print("\n=== 4.3.3 For Loop - Version 3 (negative) ===")
for i in range(0, -10, -1):
    print(i)

# 4.4 Print table of 5
print("\n=== 4.4 Print Table of 5 ===")
for i in range(1, 11):
    print(5, " * ", i, " = ", i * 5)

# 4.5.1 Sum all numbers from 1 to 10 - Version 1
print("\n=== 4.5.1 Sum (1 to 10) - Version 1 ===")
s = 0
for i in range(1, 11):
    s = s + i
print("Sum is --> ", s)

# 4.5.2 Sum all numbers from 1 to 10 - Version 2
print("\n=== 4.5.2 Sum (1 to 10) - Version 2 ===")
print("Sum is --> ", sum(range(1, 11)))

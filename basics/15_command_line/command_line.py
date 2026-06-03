"""
15. COMMAND LINE ARGUMENT
Learning: How to Take input from command line and process it

Note: Run these programs from terminal/command line

Usage Examples:
    python 15.1_add_numbers.py 10 20
    python 15.2_concatenate_strings.py Hello World
    python 15.3_sum_all_numbers.py 10 20 30 40
"""

import sys

# 15.1 Add two numbers given at cmd line
print("=== 15.1 Add Two Numbers from Command Line ===")
print("All arguments:", sys.argv)
if len(sys.argv) >= 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a + b
    print(a, " + ", b, " --> ", c)
else:
    print("Usage: python script.py <num1> <num2>")

# 15.2 Concatenate two strings given at cmd line
print("\n=== 15.2 Concatenate Strings from Command Line ===")
if len(sys.argv) >= 3:
    s = sys.argv[1] + " " + sys.argv[2]
    print(sys.argv[1], " + ", sys.argv[2], " --> ", s)
else:
    print("Usage: python script.py <string1> <string2>")

# 15.3 Add all the numbers given at cmd line
print("\n=== 15.3 Sum All Numbers from Command Line ===")
if len(sys.argv) > 1:
    total = 0
    for s in sys.argv[1:]:
        try:
            total += int(s)
        except ValueError:
            print(f"Skipping non-numeric argument: {s}")
    print("Sum is --> ", total)
else:
    print("Usage: python script.py <num1> <num2> ...")

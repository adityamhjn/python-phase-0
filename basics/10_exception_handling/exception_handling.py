"""
10. EXCEPTION HANDLING
Learning: How to handle exceptions
"""

# 10.1 Division by zero handling
print("=== 10.1 Exception Handling - Division by Zero ===")
for i in range(-5, 6):
    try:
        print("100/", i, " --> ", 100 / i)
    except:
        print("error - cannot divide by zero")

# 10.2 Array out of index handling
print("\n=== 10.2 Exception Handling - Array Index Out of Range ===")
L = [1, 2, 3, 4, 5]
for i in range(8):
    try:
        print(i, " --> ", L[i])
    except:
        print("error - index out of range")

# 10.3 File not found handling
print("\n=== 10.3 Exception Handling - File Not Found ===")
fileName = input("Enter File Name: ")
try:
    fp = open(fileName)
    fp.close()
except:
    print('Error !! "%s" File Not Found' % (fileName))

print("Done")

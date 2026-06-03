"""
5. IF-ELSE CONDITIONS
Learning: if-else Conditional Checking
"""

# 5.1 Compare two numbers
print("=== 5.1 Compare Two Numbers ===")
a = int(input("Enter First No: "))
b = int(input("Enter Second No: "))
if a > b:
    print(a, " > ", b)
else:
    print(a, " < ", b)

# 5.2 Check if number is odd or even
print("\n=== 5.2 Check Odd or Even ===")
n = int(input("Enter a No: "))
if n % 2 == 0:
    print(n, " is even")
else:
    print(n, " is odd")

# 5.3 Check if number is prime
print("\n=== 5.3 Check Prime Number ===")
n = int(input("Enter a No: "))
f = 0
for i in range(2, n // 2 + 1):
    if n % i == 0:
        f = 1
        break

if f == 0:
    print("Prime")
else:
    print("Not Prime")

# 5.4 Compare strings with elif
print("\n=== 5.4 Compare Strings ===")
a = input("Enter First String : ")
b = input("Enter Second String: ")

if a == b:
    print("a == b")
elif a >= b:
    print("a > b")
else:
    print("a < b")

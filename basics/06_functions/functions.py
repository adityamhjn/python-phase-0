"""
6. FUNCTIONS
Learning: How to declare and call function
"""

# 6.1 Add two numbers function
print("=== 6.1 Add Two Numbers ===")
def Add(a, b):
    c = a + b
    return c

print("Add(10,20) -->", Add(10, 20))
print("Add(20,50) -->", Add(20, 50))
print("Add(80,200) -->", Add(80, 200))

# 6.2 Check if number is prime
print("\n=== 6.2 Check Prime Number ===")
def IsPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 0
    return 1

print("IsPrime(20)  --> ", IsPrime(20))
print("IsPrime(23)  --> ", IsPrime(23))
print("IsPrime(200) --> ", IsPrime(200))
print("IsPrime(37)  --> ", IsPrime(37))

# 6.3 Add 1 to n
print("\n=== 6.3 Sum from 1 to N ===")
def AddN(n):
    s = sum(range(n + 1))
    return s

print("AddN(10)  --> ", AddN(10))
print("AddN(20)  --> ", AddN(20))
print("AddN(50)  --> ", AddN(50))
print("AddN(200) --> ", AddN(200))

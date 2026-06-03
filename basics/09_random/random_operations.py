"""
9. RANDOM NUMBERS AND STRINGS
Learning: Generate Random Numbers/String
"""

import random as r
import string as s

# 9.1 Generate random number between 0 and 1
print("=== 9.1 Random Float (0 to 1) ===")
print(r.random())
print(r.random())
print(round(r.random(), 4))

# 9.2 Generate random integer
print("\n=== 9.2 Random Integer ===")
print(r.randint(1, 100))
print(r.randint(1, 100))
print(r.randint(-10, 10))
print(r.randint(-10, 10))

# 9.3 Generate random real number
print("\n=== 9.3 Random Real Number (Uniform) ===")
print(r.uniform(1, 100))
print(r.uniform(1, 100))
print(r.uniform(-10, 10))
print(r.uniform(-10, 10))
print(round(r.uniform(-10, 10), 2))

# 9.4 Select sample from list
print("\n=== 9.4 Sample from List ===")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(r.sample(A, 4))
print(r.sample(A, 2))
print(r.sample(range(0, 100), 2))
print(r.sample(range(-100, 100), 5))

# 9.5 Generate random string
print("\n=== 9.5 Generate Random String ===")
print("String        --> ", s.ascii_letters)
passwd = r.sample(s.ascii_letters, 6)
print("Selected Char --> ", passwd)
passwd1 = "".join(passwd)
print("passwd1       --> ", passwd1)
passwd2 = "+".join(passwd)
print("passwd2       --> ", passwd2)
passwd3 = "*".join(passwd)
print("passwd3       --> ", passwd3)

# 9.6 Generate random digits
print("\n=== 9.6 Generate Random Digits (OTP) ===")
print("Digits --> ", s.digits)
otp = r.sample(s.digits, 5)
print("Selected num1 --> ", otp)
otp = "".join(otp)
print("otp1          --> ", otp)

otp = r.sample(s.digits, 5)
print("Selected num2 --> ", otp)
otp = "".join(otp)
print("otp2          --> ", otp)

# 9.7 Generate random string + digits
print("\n=== 9.7 Random String + Digits + Special Chars ===")
print("String + Digits --> ", s.ascii_letters + s.digits)

mixPasswd = r.sample(s.ascii_letters + s.digits, 5)
print("\nSelected Str1 --> ", mixPasswd)
mixPasswd = "".join(mixPasswd)
print("mixPasswd1    --> ", mixPasswd)

splChar = "#@!~%^&*()_+=-[]{}|"
mixPasswd = r.sample(splChar + s.ascii_letters + s.digits, 8)
print("\nSelected Str3 --> ", mixPasswd)
mixPasswd = "".join(mixPasswd)
print("mixPasswd3    --> ", mixPasswd)

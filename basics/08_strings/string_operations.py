"""
8. STRING OPERATIONS
Learning: How to handle string operations
"""

# 8.1 String Indexing
print("=== 8.1 String Indexing ===")
var = 'Hello World!'
print("var      --> ", var)
print("var[0]   --> ", var[0])
print("var[1:5] --> ", var[1:5])
print("var[:-5] --> ", var[:-5])

# 8.2 String length, upper, lower
print("\n=== 8.2 String Length, Upper, Lower ===")
var = 'Hello World!'
print("String --> ", var)
print("Length --> : ", len(var))
print("Upper  --> : ", var.upper())
print("Lower  --> : ", var.lower())

# 8.3 String formatting
print("\n=== 8.3 String Formatting ===")
name = input("Enter your name: ")
age = int(input("Enter your age : "))
price = float(input("Enter the book price: "))
s = "\nYour name is %s, age is %d and book price is %f" % (name.upper(), age, price)
print(s)

# 8.4 Triple Quotes
print("\n=== 8.4 String in Triple Quotes ===")
para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)

# 8.5 String strip
print("\n=== 8.5 String Strip ===")
var = " Indian   Army    "
print("String    --> ", var)
print("Length    --> ", len(var))
print("var strip --> ", var.strip())
print("Length of var after strip --> ", len(var.strip()))

# 8.6 String split
print("\n=== 8.6 String Split ===")
var = " Indian,   Army    "
print("String    --> ", var)
print("Length    --> ", len(var))
print("var split --> ", var.split())
print("var split --> ", var.split(' '))
print("var split --> ", var.split(','))
print("var split --> ", var.strip().split(','))

# 8.7 Count in string
print("\n=== 8.7 Count in String ===")
var = " Indian Army    "
print("String       --> ", var)
print("Count of ' ' --> ", var.count(' '))
print("Count of 'a' --> ", var.count('a'))
print("Count of 'n' --> ", var.count('an'))

# 8.8 Reverse a String
print("\n=== 8.8 Reverse a String ===")
var = "Indian Army"
print("String    --> ", var)
print("var[::1]  --> ", var[::1])
print("var[::2]  --> ", var[::2])
print("var[::-1] --> ", var[::-1])
print("var[::-2] --> ", var[::-2])
var = var[::-1]
print("var after reverse --> ", var)

# 8.9 Palindrome
print("\n=== 8.9 Palindrome ===")
s1 = "Indian Army"
s2 = "malayalam"
s3 = "madam"
s4 = "teacher"
print("s1 --> ", s1 == s1[::-1])
print("s2 --> ", s2 == s2[::-1])
print("s3 --> ", s3 == s3[::-1])
print("s4 --> ", s4 == s4[::-1])

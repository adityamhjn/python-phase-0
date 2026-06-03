"""
16. FILE HANDLING
Learning: How to open the file, read the file and write in the file
"""

# 16.1 Writing 1 to 10 in file
print("=== 16.1 Writing Numbers to File ===")
fp = open('result.txt', 'w')
for i in range(1, 11):
    fp.write(str(i) + "\n")
fp.close()
print("Writing done !! \nOpen result.txt to view the content")

# 16.2 Read a file and print its content
print("\n=== 16.2 Reading File Content ===")
fp = open('result.txt')
for line in fp:
    print(line.strip())
fp.close()

# 16.3 Read from one file, convert to uppercase and write to another
print("\n=== 16.3 Read, Convert to Uppercase, Write to New File ===")
Readfp = open('result.txt')
Writefp = open('abc.txt', 'w')
for line in Readfp:
    Writefp.write(line.upper())

Writefp.close()
Readfp.close()
print("Writing done !! \nOpen abc.txt to view the content")

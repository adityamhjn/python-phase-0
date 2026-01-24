word = input("Enter word: ").lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

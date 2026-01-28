with open("output.txt", "r") as file:
    text = file.read().lower()

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Total words:", len(words))
print("Word frequency:", word_count)
# This code reads the content of "output.txt", analyzes the frequency of each word,
# and prints the total word count along with the frequency of each word.
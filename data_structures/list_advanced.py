numbers = [5, 3, 8, 3, 1, 9, 5]

# Remove duplicates while preserving order
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique:", unique)

# Second largest element
unique.sort(reverse=True)
print("Second largest:", unique[1])

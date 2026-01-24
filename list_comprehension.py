numbers = [1, 2, 3, 4, 5]

squares = [n * n for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

print(squares)
print(even_numbers)

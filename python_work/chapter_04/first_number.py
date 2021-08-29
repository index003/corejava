for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

numbers = list(range(6))
print(numbers)

# 列表求和
print(sum(numbers))

# 指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
min_digits = min(digits)
max_digits = max(digits)
sum_digits = sum(digits)
print(max_digits)
print(min_digits)
print(sum_digits)

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

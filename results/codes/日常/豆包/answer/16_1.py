def move_numbers_to_start(s):
    numbers = []
    non_numbers = []
    for char in s:
        if char.isdigit():
            numbers.append(char)
        else:
            non_numbers.append(char)
    return ''.join(numbers) + ''.join(non_numbers)


test_string = "abc123def456"
result = move_numbers_to_start(test_string)
print(result)
    
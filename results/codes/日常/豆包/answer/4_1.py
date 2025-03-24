def swap_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result


input_string = "Hello, World!"
output_string = swap_case(input_string)
print(output_string)
    
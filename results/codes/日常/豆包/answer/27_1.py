def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2


numbers = [12, 3, 5, 7, 4, 19]
median = calculate_median(numbers)
print(f"这组数字的中位数是: {median}")
    
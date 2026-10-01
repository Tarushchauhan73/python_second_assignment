def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


print(find_largest([10, 25, 7, 40, 15]))
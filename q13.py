def remove_duplicates(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique


print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))
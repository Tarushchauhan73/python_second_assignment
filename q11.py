def count_frequency(numbers):
    for i in range(len(numbers)):
        already_counted = False

        for j in range(i):
            if numbers[i] == numbers[j]:
                already_counted = True
                break

        if already_counted:
            continue

        count = 0

        for number in numbers:
            if number == numbers[i]:
                count += 1

        print(numbers[i], "appears", count, "times")


count_frequency([1, 2, 2, 3, 1, 2])
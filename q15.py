def analyze_numbers(numbers):
    positive = negative = zeros = even = odd = 0

    for n in numbers:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zeros += 1

        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return positive, negative, zeros, even, odd


result = analyze_numbers([10, -5, 0, 7, -2, 4])

print("Positive:", result[0])
print("Negative:", result[1])
print("Zeros:", result[2])
print("Even:", result[3])
print("Odd:", result[4])
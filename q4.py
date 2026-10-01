def print_primes(start, end):
    for number in range(start, end + 1):
        if number < 2:
            continue

        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)


print_primes(10, 30)
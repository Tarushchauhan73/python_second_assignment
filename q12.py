def multiplication_tables(start, end):
    for number in range(start, end + 1):
        print("Table of", number)

        for i in range(1, 11):
            print(number, "x", i, "=", number * i)

        print()


multiplication_tables(2, 4)
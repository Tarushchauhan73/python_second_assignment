def is_palindrome(value):
    value = str(value)
    reverse = ""

    for char in value:
        reverse = char + reverse

    return value == reverse


print(is_palindrome("madam"))
print(is_palindrome(121))
print(is_palindrome("hello"))
def is_palindrome(string):
    return string == string[::-1]

A = input()
print('1' if is_palindrome(A) else '0')
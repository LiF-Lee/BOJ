def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

for _ in range(int(input())):
    print('Yes' if is_palindrome(input()) else 'No')
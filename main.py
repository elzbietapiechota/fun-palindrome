def check_palindrome(word):

    return word.lower() == word.lower()[::-1]

print(check_palindrome("Potop"))
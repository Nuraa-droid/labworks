def palindrome(word):
    return word == word[::-1]
word = input()
if palindrome(word):
    print("word is palindrome")
else:
    print("word is not palindrome")
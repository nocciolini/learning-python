word = str(input("Input a word to validate if it is a palindrome: ")).lower()

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "isn't a palindrome")
from unicodedata import normalize
def normalizeStr(str):
   return normalizeStr('NFKD', str).encode('ASCII', 'ignore').decode('ASCII')

word = str(input("Input a word to validate if it is a palindrome: ")).lower()

if normalizeStr(word) == normalizeStr(word[::-1]):
    print(word, "is a palindrome")
else:
    print(word, "isn't a palindrome")
# Problem 59A - Word
"""
if numberof lowercase letter == numberof Uppercase letter:
    replace all the letters with lowercase
elif numberof lowercase letter < numberof UPPERCASE letter:
    replace all letters with UPPERCASE
elif numberof lowercase letter > numberof UPPERCASE LETTER:
    replace all the letters with lowercase
"""
word = input()
upper = 0
lower = 0

for i in word:
    if i.isupper():
        upper += 1
    else:
        lower += 1

if upper == lower:
    print(word.lower())
elif upper > lower:
    print(word.upper())
elif upper < lower:
    print(word.lower())
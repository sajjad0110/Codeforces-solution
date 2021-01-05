# Lucky Digits: 4, 7
# Nearly Lucky number: if the number of lucky digits in it is a lucky number
number = list(input())

if number.count("4") + number.count("7") == 7 or 4:
    print("YES")
else:
    print("NO")

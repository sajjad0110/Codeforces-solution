# Problem 977A - Wrong Substraction
"""
if number % 10 != 0:
    number = number - 1
else:
    number = number // 10
"""
n, k = map(int, input().split())
for i in range(k):
    if n % 10 != 0:
        n -= 1
    else:
        n //= 10

print(n)
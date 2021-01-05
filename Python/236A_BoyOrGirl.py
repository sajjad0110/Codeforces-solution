# Problem 236A - Boy or Girl
"""
distinct_character % 2 != 0 : male
distinct_character % 2 == 0 : female
"""

name = list(input())
name.sort()
dist_char = 0

for i in range(1, len(name)):
    if name[i - 1] != name[i]:
        dist_char += 1

print(dist_char)

if dist_char % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

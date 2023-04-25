import math


def lengthOfLastWord(str) -> int:
    arr = str.split(' ')
    last = 0
    for i in arr[::-1]:
        if len(i) != 0 and last == 0:
            last = len(i)
    return last


str = "hello my world asdas ada ds "
print(lengthOfLastWord(str))

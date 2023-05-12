

columnTitle = "FXSHRXW"

result = 0
for i in range(len(columnTitle)):
    value = ord(columnTitle[i]) - 64
    result += value * (26 ** (len(columnTitle) - i - 1))


print(result)


nums = [2, 1, -1]
res = -1
for i in range(len(nums)):
    larr = nums[:i]
    rarr = nums[i:-1]
    lsum = 0
    rsum = 0
    for x in larr:
        lsum += x
    for y in rarr:
        rsum += y
    print(lsum, rsum)
    if lsum == rsum:
        res = i
        break
print(res)

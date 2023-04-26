import math


# num1 = [0]
# num2 = [1]
# m = 0
# n = 1
num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
m = 3
n = 3


def merge(nums1, m, nums2, n):
    j = 0
    for i in range(len(nums1)):
        if i >= m and j < n:
            nums1[i] = nums2[j]
            j += 1
    nums1.sort()
    print(nums1)


merge(num1, m, num2, n)

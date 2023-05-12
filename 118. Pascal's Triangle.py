

def main(numRows):
    n = numRows
    arr = []
    for i in range(n):
        rw = []
        for j in range(i+1):
            if (j == 0 or j == i):
                rw.append(1)
            else:
                rw.append(arr[i-1][j-1]+arr[i-1][j])
        arr.append(rw)
    return arr


if __name__ == "__main__":
    main(5)

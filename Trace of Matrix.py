def getlist():
    return list(map(int, input().split()))


def getinp():
    return map(int, input().split())


def solve(arr, n):
    max_trace = 0

    for i in range(n):
        for j in range(n):
            s = i
            r = j
            trace = 0
            while s < n and r < n:
                trace += arr[s][r]
                s += 1
                r += 1
                max_trace = max(max_trace, trace)

    return max_trace


def main():
    n = int(input())
    for _ in range(n):
        s = int(input())
        mr = []
        for t in range(s):
            mr.append(getlist())
        print(solve(mr, s))

    return 0


if __name__ == "__main__":
    main()

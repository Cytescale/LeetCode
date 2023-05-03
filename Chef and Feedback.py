

def getlist():
    return list(map(int, input().split()))


def getinp():
    return map(int, input().split())


def main():

    n = int(input())
    while n > 0:

        st = str(input())
        fl = 0
        for i in range(len(st)-2):
            ab = st[i:i+3]
            if ab == '101' or ab == '010':
                fl = 1
                break
        if fl == 1:
            print('Good');
        else:
            print('Bad')
        n -= 1

    return 0


if __name__ == "__main__":
    main()

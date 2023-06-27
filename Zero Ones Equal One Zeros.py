import math

def getlist():
    return list(map(int, input().split()))

def getinp():
    return map(int, input().split())

def gint():
    return int(input())


if(__name__ == '__main__'):
    t = int(input())
    while t>0:
        n=int(input());
        print('1'+((n-2)*'0')+'1');
        t-=1
        pass
    pass
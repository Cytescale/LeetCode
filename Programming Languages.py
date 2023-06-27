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
        A,B,A1,B1,A2,B2=getinp()
        if (A1==A or A1==B) and (B1==B or B1==A):
            print("1")
        elif (A2==A or A2==B) and (B2==B or B2==A):
            print("2")
        else:
            print("0")
        t-=1
        pass
    pass
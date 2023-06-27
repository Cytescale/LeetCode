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
        x1, y1, z1 = getinp()
        x2, y2, z2 = getinp()
        s1 = x1+y1+z1
        s2 = x2+y2+z2
        if s1>s2:
            print("Dragon")
        elif s2>s1:
            print("Sloth")
        elif (s1==s2 and x1>x2) or (s1==s2 and x1==x2 and y1>y2):
            print("Dragon")
        elif (s1==s2 and x2>x1) or (s1==s2 and x1==x2 and y2>y1):
            print("Sloth")
        else:
            print("Tie")
            
        t-=1
        pass
    pass
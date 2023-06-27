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
        x = gint();
        s = input();
        z = ['a','e','i','o','u']
        c  = 0
        for i in range(len(s)):
            if(s[i] not in z):c += 1;
            else:c=0;
            if c >= 4:break
        if c >= 4:
            print("NO");
            t-=1;
            continue;
        print("YES");
        t-=1
    pass
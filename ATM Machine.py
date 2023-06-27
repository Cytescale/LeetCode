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
        n,k =  getinp();
        arr = getlist();
        s = ""
        for i in arr:
            if i<=k:
                k-=i
                s += "1"
                continue;
            s+="0"
        t-=1;
        print(s);
        pass
    pass
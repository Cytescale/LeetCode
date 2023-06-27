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
        mt,mn,sn = getinp()
        tt = 1;
        cc = 0;
        
        nrem = sn;
        nn = mn;
        while(tt<=mt and nrem<=sn and nrem >= 0 ):
            if(nn > nrem):
                nn = nrem                
            nrem -= nn;
            cc += nn**2
            tt += 1
        print(cc)
        t-=1
        pass
    pass
    #include <bits/stdc++.h>

    using namespace std;

    #define push_back pb
    #define test  \
        int t;    \
        cin >> t; \
        while (t--)

    typedef long long ll;
    
    
    void solve(int x,int y ,int n,int r){

        int nor = 0;
        int pre = n;
        while((y*pre + x*nor) > r){
                pre--;
                nor++;   
                if(pre < 0 || nor < 0)break;
        }
        if(pre+nor != n || nor < 0 || pre < 0){
            cout<<"-1"<<endl;
            return;
        }
        cout<<nor<<" "<<pre<<endl;;
        
    }


    int main()
    {
        test
        {
            int x,y,n,r;
            cin>>x>>y>>n>>r;
            solve(x,y,n,r);
        }
        return 0;
    }

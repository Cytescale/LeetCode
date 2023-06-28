    #include <bits/stdc++.h>
    using namespace std;
    typedef long long ll;

    #define test  \
        int t;    \
        cin >> t; \
        while (t--)

    
    int solve(string s){

    	int c = 0;
    	int cr = 1;
    	for(int i = 0 ; i< s.length();i++){
    		if(s[i] == s[i+1]){
    			cr++;
    		}
    		else{
    			if(cr%2 ==0){
    				c += cr/2;
    			}
    			else{
    				c += (cr/2)+1;	
    			}
				cr = 1;
    		}
    	}

    	return c;
    }	


    int main()
    {
        test
        {
    			string s ;
    			cin >>s;
    			sort(s.begin(),s.end());
    			cout<< solve(s)<<endl;    			
        }
        return 0;
    }
    #include <bits/stdc++.h>
    using namespace std;

    #define test  \
        int t;    \
        cin >> t; \
        while (t--)

    string solve(string s)
    {
        for(int i = 0 ; i <s.length();i++){
            if(s[i]=='1' && s[i+1]=='0' &&s[i+2]=='1' )
                return "Good";
            if(s[i]=='0' && s[i+1]=='1' &&s[i+2]=='0' )
                return "Good";
        }
    
        return "Bad";
    }

    int main()
    {
        test
        {
            string c;
            cin >> c;
            cout << solve(c) << endl;
        }
        return 0;
    }

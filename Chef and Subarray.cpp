    #include <bits/stdc++.h>
    using namespace std;
    typedef long long ll;

    #define test  \
        int t;    \
        cin >> t; \
        while (t--)

    

     int solve(int n , int* arr){
     	int m = 0;
     	int c = 0;
     	for(int i = 0 ; i  < n ; i++){
     		m = max(m,c);
     		if(arr[i] ==0){;
     			c = 0;
     			continue;
     		}
     		c++;
     	}
     	m = max(m,c);
     	return m;
     }


    int main()
    {
    	cin.tie(nullptr);
    	ios::sync_with_stdio(false);
        int n ;
        cin >> n;
        int* arr = new int[n]{0};
        for(int i = 0 ; i < n ;i++){
        	int d ;
        	cin >> d;
        	arr[i] = d;
        }
        cout<<solve(n,arr)<<endl;
        return 0;
    }
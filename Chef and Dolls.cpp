#include <bits/stdc++.h>
using namespace std;

#define test  \
    int t;    \
    cin >> t; \
    while (t--)

int solve(int n, int *arr)
{
    sort(arr, arr + n);
    for (int i = 0; i < n; i += 2)
    {
        if (arr[i] != arr[i + 1] || i + 1 >= n)
            return arr[i];
    }
    return -100000;
}

int main()
{
    test
    {
        long long n;
        cin >> n;
        int *arr = new int[n];
        for (int i = 0; i < n; i++)
        {
            int d;
            cin >> d;
            arr[i] = d;
        }

        cout << solve(n, arr) << endl;
    }
    return 0;
}
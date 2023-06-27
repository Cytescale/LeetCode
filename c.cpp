#include <bits/stdc++.h>
using namespace std;

string solve(int n, const int *ad, const int *om)
{
    int a = 0, o = 0;
    for (int i = 0; i < n; i++, ++a, ++o)
    {
        if (ad[i] == 0)
            a = 0;
        if (om[i] == 0)
            o = 0;
    }
    return a != o ? a > o ? "Addy" : "Om" : "Draw";
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int *ad = new int[n];
        int *om = new int[n];
        for (int i = 0; i < n; i++)
        {
            int d;
            cin >> d;
            ad[i] = d;
        }
        for (int i = 0; i < n; i++)
        {
            int d;
            cin >> d;
            om[i] = d;
        }
        cout << solve(n, ad, om) << endl;
    }
    return 0;
}
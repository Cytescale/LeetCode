#include <bits/stdc++.h>
using namespace std;

string solve(int n, const int *ad, const int *om)
{
    int ma = 0, mo = 0, a = 0, b = 0;
    for (int i = 0; i < n; i++)
    {
        ma = max(ma, a++);
        mo = max(mo, b++);
        if (ad[i] == 0)
            a = 0;
        if (om[i] == 0)
            b = 0;
        // cout << a << " " << b << endl;
    }
    ma = max(ma, a);
    mo = max(mo, b);
    // cout << ma << " " << mo << endl;
    return ma != mo ? mo > ma ? "Addy" : "Om" : "Draw";
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
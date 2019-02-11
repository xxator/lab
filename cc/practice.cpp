#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,k;
    scanf("%d %d",&n,&k);
    string s;
    cin>>s;
    //cout<<s;

    vector <vector<int>> v(26);
    vector <int> vv(26);
    for(int i = 1;i<n;i++)
    {
        if(s[i]==s[i-1])
        {
            int c = 2;
            i++;
            while(s[i]==s[i-1] && i < n)
            {
                c++;
                i++;
            }
            v[s[i-1]-'a'].push_back(c);
        }
    }
    for(int i = 0;i<n;i++)
    {
        vv[s[i]-'a']++;
    }
    int max = 0;
    if(k == 1)
    {
        for(int i = 0;i<26;i++)
        {
            if(vv[i]>max)
            {
                max = vv[i];
            }
        }
        cout<<max;
        return 0;
    }
    for(int i = 0;i<26;i++)
    {
        int temp = 0;
        for(int j = 0;j<v[i].size();j++)
        {
            if(v[i][j]>=k)
            {
                temp += v[i][j]/k;
            }
        }
        if(temp > max)
        {
            max = temp;
        }
        //cout << endl;
    }
    cout << max;
    return 0;
}
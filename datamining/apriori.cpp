#include<bits/stdc++.h>
using namespace std;
#define se second 
#define fi first
#define pb push_back
#define mp make_pair
#define minsup 5000
#define minconf 10
vector <vector <int>> trans;
map <int,int> m;
vector < pair < vector <int>, int > > c;
vector < pair < vector <int>, int > > l[10000];
map <vector <int> ,int> hass;
int k;
int sig;
void nextc()
{
    if(k==0)
    {
        for(auto it=m.begin();it!=m.end();it++)
        {
            vector <int> arr;
            arr.pb(it->fi);
            c.pb(mp(arr,it->se));
        }
    }
    else
    {
        c.clear();
        for(int i=0;i<l[k].size();i++)
        {
            for(int j=i+1;j<l[k].size();j++)
            {
                int s1=l[k][i].fi.size();
                int s2=l[k][j].fi.size();
                vector <int> arr(s1+s2);
                auto it=set_union(l[k][i].fi.begin(),l[k][i].fi.end(),l[k][j].fi.begin(),l[k][j].fi.end(),arr.begin());
                arr.resize(it-arr.begin());
                if(arr.size()==k+1)
                {
                    if(hass.find(arr)==hass.end())
                    { 
                        int sup=0;
                        for(int ii=0;ii<trans.size();ii++)
                        {
                            if(includes(trans[ii].begin(),trans[ii].end(),arr.begin(),arr.end()))
                                sup++;
                        }
                        c.pb(mp(arr,sup));
                        hass[arr]=1;
                    }
                }
            }
        }
    }
    k++;
}
void nextl()
{
    for(int i=0;i<c.size();i++)
    {
        if(c[i].se>=minsup)
        {
            l[k].pb(c[i]);
        }
    }
    if(l[k].size()==0)
    {
        sig=1;
        return ;
    }
}
int main()
{
    freopen("mushroom.dat","r",stdin);
    string input;
    freopen("tmp.txt","w",stdout);
    while(getline(cin,input))
    {
        vector <int> inputs;
        istringstream in( input );
        copy(istream_iterator<int>( in ), istream_iterator<int>(),back_inserter( inputs ) );
        copy( inputs.begin(), inputs.end(),ostream_iterator<int>(cout," ") );
        trans.pb(inputs);
    }
   // tmp.close() ;  
    freopen("outputf.in","w",stdout);
    for(int i=0;i<trans.size();i++)
    {
        for(int j=0;j<trans[i].size();j++)
        {
           m[trans[i][j]]++;
        }
        sort(trans[i].begin(),trans[i].end());
    }
    k=0;
    sig=0;
    while(1)
    {
        nextc();        
        nextl();
          if(sig)
            break;
    }
    for(int i=1;i<=k;i++)
    {
        for(int j=0;j<l[i].size();j++)
        {
            for(int it=0;it<l[i][j].fi.size();it++)
            {
                cout<<l[i][j].fi[it]<<",";
            }
            cout<<"\n";
        }
    }
}
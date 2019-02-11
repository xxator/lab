#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    

    scanf("%d",&n);
    vector<int> in(n);
    for(int i = 0;i<n;i++)
    {
    	scanf("%d",&in[i]);
    }
    int min_sum = INT_MAX,ans = 0;
    int temp = 0;

    for(int i = 1;i<=100;i++)
    {
    	temp = 0;
    	for(int j = 0;j < n; j++)
    	{
    		temp = temp + min(min(abs(i-in[j]),abs(i-in[j]-1)),abs(i-in[j]+1));
    	}
    	if(temp< min_sum)
    	{
    		min_sum = temp;
    		ans = i;
    	}
    }
    printf("%d %d",ans,min_sum);
}
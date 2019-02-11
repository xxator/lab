#include <bits/stdc++.h>
using namespace std;
  
// Functions to calculate Follow 
void followfirst(char, int, int); 
void follow(char c); 
  
// Function to calculate First 
void findfirst(char, int, int); 
  
#define count 7
int n = 0; 
  
// Stores the final result  
// of the First Sets 
char calc_first[10][100]; 
  
// Stores the final result 
// of the Follow Sets 
char calc_follow[10][100]; 
int m = 0; 
  
// Stores the production rules 
//char production[10][10]; 

char production[10][10]; 
char f[10], first[10]; 
int k; 
char ck; 
int e; 

/*
void takeInput() 
{
    int n;
    cout<<"\nEnter number of non terminals: ";
    cin>>n;
    cout<<"\nEnter non terminals one by one: ";
    int i;
    vector<string> nonter(n);
    vector<int> leftrecr(n,0);
    for(i=0;i<n;++i) {
            cout<<"\nNon terminal "<<i+1<<" : ";
        cin>>nonter[i];
    }
    vector<vector<string> > prod;
    cout<<"\nEnter '^' for null";
    for(i=0;i<n;++i) {
        cout<<"\nNumber of "<<nonter[i]<<" productions: ";
        int k;
        cin>>k;
        int j;
        cout<<"\nOne by one enter all "<<nonter[i]<<" productions";
        vector<string> temp(k);
        for(j=0;j<k;++j) {
            cout<<"\nRHS of production "<<j+1<<": ";
            string abc;
            cin>>abc;
            temp[j]=abc;
            if(nonter[i].length()<=abc.length()&&nonter[i].compare(abc.substr(0,nonter[i].length()))==0)
                leftrecr[i]=1;
        }
        prod.push_back(temp);
    }
    for(i=0;i<n;++i) {
        cout<<leftrecr[i];
    }
    for(i=0;i<n;++i) {
        if(leftrecr[i]==0)
            continue;
        int j;
        nonter.push_back(nonter[i]+"'");
        vector<string> temp;
        for(j=0;j<prod[i].size();++j) {
            if(nonter[i].length()<=prod[i][j].length()&&nonter[i].compare(prod[i][j].substr(0,nonter[i].length()))==0) {
                string abc=prod[i][j].substr(nonter[i].length(),prod[i][j].length()-nonter[i].length())+nonter[i]+"'";
                temp.push_back(abc);
                prod[i].erase(prod[i].begin()+j);
                --j;
            }
            else {
                prod[i][j]+=nonter[i]+"'";
            }
        }
        temp.push_back("#");
        prod.push_back(temp);
    }
    cout<<"\n\n";
    cout<<"\nNew set of non-terminals: ";
    for(i=0;i<nonter.size();++i)
        cout<<nonter[i]<<" ";
    cout<<"\n\nNew set of productions: ";
    for(i=0;i<nonter.size();++i) {
        int j;
        for(j=0;j<prod[i].size();++j) {
            //cout<<"\n"<<nonter[i]<<"="<<prod[i][j];
            production.push_back(nonter[i]+"="+prod[i][j]);
        }
    }

}*/
  
int main(int argc, char **argv) 
{ 
    int jm = 0; 
    int km = 0; 
    int i, choice; 
    char c, ch; 
    //count = 8; 
      
    // The Input grammar
    int num;
    cout<<"Enter no. of poduction: ";
    cin>>num;
    for(int i=0;i<num;i++)
    {
        char str[10];
        cout<<"Enter production "<<i<<" : ";
        cin>>str;
        strcpy(production[i], str);
    }
    /*
    strcpy(production[0], "E=TR"); 
    strcpy(production[1], "R=+TR"); 
    strcpy(production[2], "R=#"); 
    strcpy(production[3], "T=FY"); 
    strcpy(production[4], "Y=*FY"); 
    strcpy(production[5], "Y=#"); 
    strcpy(production[6], "F=(E)"); 
    strcpy(production[7], "F=i"); 
    */

    /*
        E=TD          D==E'
        T=FS          S==T'
        F=(E)
        F=i
        D=+TD
        D=#
        S=*FS
    */
    int kay; 
    char done[count]; 
    int ptr = -1; 
      
    for(k = 0; k < count; k++) { 
        for(kay = 0; kay < 100; kay++) { 
            calc_first[k][kay] = '!'; 
        } 
    } 
    int point1 = 0, point2, xxx; 
      
    for(k = 0; k < count; k++) 
    { 
        c = production[k][0]; 
        point2 = 0; 
        xxx = 0; 
          
        for(kay = 0; kay <= ptr; kay++) 
            if(c == done[kay]) 
                xxx = 1; 
                  
        if (xxx == 1) 
            continue; 
          
        // Function call     
        findfirst(c, 0, 0); 
        ptr += 1; 
          
        // Adding c to the calculated list 
        done[ptr] = c; 
        printf("\n First(%c) = { ", c); 
        calc_first[point1][point2++] = c; 
          
        // Printing the First Sets of the grammar 
        for(i = 0 + jm; i < n; i++) { 
            int lark = 0, chk = 0; 
              
            for(lark = 0; lark < point2; lark++) { 
                  
                if (first[i] == calc_first[point1][lark]) 
                { 
                    chk = 1; 
                    break; 
                } 
            } 
            if(chk == 0) 
            { 
                printf("%c, ", first[i]); 
                calc_first[point1][point2++] = first[i]; 
            } 
        } 
        printf("}\n"); 
        jm = n; 
        point1++; 
    } 
    printf("\n"); 
    printf("-----------------------------------------------\n\n"); 
    char donee[count]; 
    ptr = -1; 
      
    // Initializing the calc_follow array 
    for(k = 0; k < count; k++) { 
        for(kay = 0; kay < 100; kay++) { 
            calc_follow[k][kay] = '!'; 
        } 
    } 
    point1 = 0; 
    int land = 0; 
    for(e = 0; e < count; e++) 
    { 
        ck = production[e][0]; 
        point2 = 0; 
        xxx = 0; 
          
        for(kay = 0; kay <= ptr; kay++) 
            if(ck == donee[kay]) 
                xxx = 1; 
                  
        if (xxx == 1) 
            continue; 
        land += 1; 
          
        // Function call 
        follow(ck); 
        ptr += 1; 
          
        donee[ptr] = ck; 
        printf(" Follow(%c) = { ", ck); 
        calc_follow[point1][point2++] = ck; 
          
        for(i = 0 + km; i < m; i++) { 
            int lark = 0, chk = 0; 
            for(lark = 0; lark < point2; lark++)  
            { 
                if (f[i] == calc_follow[point1][lark]) 
                { 
                    chk = 1; 
                    break; 
                } 
            } 
            if(chk == 0) 
            { 
                printf("%c, ", f[i]); 
                calc_follow[point1][point2++] = f[i]; 
            } 
        } 
        printf(" }\n\n"); 
        km = m; 
        point1++;  
    } 
} 
  
void follow(char c) 
{ 
    int i, j; 
      
    if(production[0][0] == c) { 
        f[m++] = '$'; 
    } 
    for(i = 0; i < 10; i++) 
    { 
        for(j = 2;j < 10; j++) 
        { 
            if(production[i][j] == c) 
            { 
                if(production[i][j+1] != '\0') 
                { 
                    followfirst(production[i][j+1], i, (j+2)); 
                } 
                  
                if(production[i][j+1]=='\0' && c!=production[i][0]) 
                { 
                    follow(production[i][0]); 
                } 
            }  
        } 
    } 
} 
  
void findfirst(char c, int q1, int q2) 
{ 
    int j; 
      
    if(!(isupper(c))) { 
        first[n++] = c; 
    } 
    for(j = 0; j < count; j++) 
    { 
        if(production[j][0] == c) 
        { 
            if(production[j][2] == '#') 
            { 
                if(production[q1][q2] == '\0') 
                    first[n++] = '#'; 
                else if(production[q1][q2] != '\0' 
                          && (q1 != 0 || q2 != 0)) 
                { 
                    findfirst(production[q1][q2], q1, (q2+1)); 
                } 
                else
                    first[n++] = '#'; 
            } 
            else if(!isupper(production[j][2])) 
            { 
                first[n++] = production[j][2]; 
            } 
            else 
            {
                findfirst(production[j][2], j, 3); 
            } 
        } 
    }  
} 
  
void followfirst(char c, int c1, int c2) 
{ 
    int k; 
      
    if(!(isupper(c))) 
        f[m++] = c; 
    else
    { 
        int i = 0, j = 1; 
        for(i = 0; i < count; i++) 
        { 
            if(calc_first[i][0] == c) 
                break; 
        } 
          
 
        while(calc_first[i][j] != '!') 
        { 
            if(calc_first[i][j] != '#')  
            { 
                f[m++] = calc_first[i][j]; 
            } 
            else
            { 
                if(production[c1][c2] == '\0') 
                { 
                    follow(production[c1][0]); 
                } 
                else
                {  
                    followfirst(production[c1][c2], c1, c2+1); 
                } 
            } 
            j++; 
        } 
    } 
} 


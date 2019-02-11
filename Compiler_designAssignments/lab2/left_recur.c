//#include<conio.h>
#include<stdio.h>
#include<string.h>
void main()
{
	char s[30],temp[20],LHS[30],fp[30],sp[30];
	int i,start,j,k=-1,flag1=0,flag2=0;
	clrscr();
	printf("enter production :");
	gets(s);
	start=2;
	LHS[0]=s[0];
	LHS[1]='\0';
	strcpy(fp,LHS);
	strcat(fp,"=");
	strcpy(sp,LHS);
	strcat(sp,"'=");
	r:
	j=0;
	for(i=start;s[i]!='|' && s[i]!='\0';i++)
		{
		temp[j]=s[i];
		j++;
		}
	temp[j]='\0';
	start=i+1;
	if(temp[0]==LHS[0])
		{
		 if(flag1==1)
			 {
				strcat(sp,"|");
			 }
		 strcat(sp,a+1);
		 strcat(sp,LHS);
		 strcat(sp,"'");
		 flag1=1;
		}
	else
		{
		 if(flag2==1)
			 {
			 	 strcat(fp,"|");
			 }
		 strcat(fp,a);
		 strcat(fp,LHS);
		 strcat(fp,"'");
		 flag2=1;
		}
	 if(start<strlen(s))
		 {
			goto r;
		 }
	 strcat(sp,"|null");
	 printf("\n%s",fp);
	 printf("\n%s",sp);
	 //getch();
}
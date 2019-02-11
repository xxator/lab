%{
#include<stdio.h>
%}
%%
"//"([a-z]|[0-9]|[A-Z]|" ")*    {};
"/*"([a-z]|[0-9]|[A-Z]|" "|"//"|\n|"\"\"")+"*/"    {};
[\t ' '] {};

%%
int main(int argc, char * argv[]){
    yyin=fopen(argv[1],"r");
yylex();
}
int yywrap()
{
return 1;
}
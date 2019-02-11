%{
#include <stdio.h>
%}


letter [a-zA-z]
digit [0-9]

%%
"//"([a-z]|[0-9]|[A-Z]|" ")*    {};
"/*"([a-z]|[0-9]|[A-Z]|" "|"//"|\n|"\"\"")+"*/"    {};
[\t ' '] {};
\n  {};
\n yylineno++;
"#include"+(" ")*+"<"+{letter}*+"."+"h>" printf("%d\t%s\tPREPROCESSOR\n",yylineno,yytext);
return|main|for|while|case|switch|if|else printf("%d\t%s\tKEYWORD\n",yylineno,yytext);
int|float|char|struct printf("%d\t%s\tDATATYPE\n",yylineno,yytext);
\( printf("%d\t%s\tBRACKET OPEN\n",yylineno,yytext);
\) printf("%d\t%s\tBRACKET CLOSE\n",yylineno,yytext);
{letter}({letter}|{digit})* printf("%d\t%s\tIDENTIFIER\n",yylineno,yytext);
{digit}+ printf("%d\t%s\tINTEGER\n",yylineno,yytext);
\{ printf("%d\t%s\tBRACE OPEN\n",yylineno,yytext);
\} printf("%d\t%s\tBRACE CLOSE\n",yylineno,yytext);
{digit}+"E"(\+|\-)?{digit}+ printf("%d\t%s\tREAL NUMBER\n",yylineno,yytext);
{digit}+\.{digit}+(E(\+|\-)?{digit}+)? printf("%d\t%s\tFLOATING NUMBER\n",yylineno,yytext);
= printf("%d\t%s\tASSIGNMENT\n",yylineno,yytext);
; printf("%d\t%s\tTERMINATOR\n",yylineno,yytext);
\t ;
" " ;
"\""+({letter}|{digit}|" ")+"\"" printf("%d\t%s\tSTRING CONSTANT\n",yylineno,yytext);




%%


int yywrap(){
    return 1;
}

int main(int argc, char * argv[]){
    yyin=fopen(argv[1],"r");
    printf("LINE\tLEXME\tTOKEN\n");
    yylex();
    fclose(yyin);
    return 0;
}
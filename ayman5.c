#include <stdio.h>
int main () {
char t;
float i;
float x;
int y;
int z ;
char c;
printf (" please:  writte the first number \n");
  y = scanf("%f", &i);
if(y != 1){
    printf("error : you have used a letter \n"); return (1);}
printf("writte the equation simple either this ( / ) for devision, ( * ) this multibly or (+ -) or adding :\n");
scanf(" %c", &t);
 switch (t)
  {case '=':break; 
   case '+':break; 
   case '/': break; 
   case '*':  break; 
 default:
  printf("you have chose a wrong simple\n"); break;}
 printf("writte the next number \n");

z = scanf("%f", &x);
if(z != 1){
    printf("error : you have used a letter \n ") ; return (1);
} 

 switch (t) {
 case '+':printf(" the result is :  %f\n",i+x ); break;
 case '-':printf(" the result is :  %f\n",i-x ); break;
 case '*': printf(" the result is :  %f\n",i*x ); break;
 case '/': printf(" the result is :  %f\n",i/x ); break;
 default: printf("you forgot to writte the equsion simple");}
return(0); }
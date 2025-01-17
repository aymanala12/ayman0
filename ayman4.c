#include <stdio.h>
int main () {


float i;
float x;
int y;
int z ;

printf (" please:  writte the first number \n");
 
 y = scanf("%f",&i);
if(y != 1){
    printf("error : you have used a letter \n"); return (1);
}
 printf ("writte the next number \n");

z = scanf("%f",&x);
if(z != 1){
    printf("error : you have used a letter \n ") ; return (1);
}
printf (" the result is :  %f\n",i+x);
 return(0);
}

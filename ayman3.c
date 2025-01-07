#include <stdio.h>
int x(char *c){


while (*c !='\0'){

    printf ("%c",*c) ;
    c++;
}  
 return (0) ;
}
 int main ()
{  
   char c[16] = "ayman ala aldein" ;

x(c);
return (0) ; } 
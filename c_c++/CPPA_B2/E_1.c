#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char *F,*Fn1,*Fn2,*res;
    int i ;
    F = "Moi" ;
    res = "" ;

    for (i=0 ; i<strlen(F) ; i++) {
       *res++ = F[i] ;
       printf("%s\n",res) ;
    }

    return 0;

}
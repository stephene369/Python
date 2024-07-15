#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fp ;

int main() {

    fp = fopen("moi.txt" , "w") ; 
    fclose(fp) ;
    fwrite("stephene") ;

    return 0 ;
}



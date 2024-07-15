#include <stdio.h>


int main() {
    
    int nombre ;
    int i ;
    printf("Nombre : ") ;
    scanf("%d" , &nombre) ;

    for (i=0 ;i<13 ;i++) {
        printf("\t") ;
        printf("\n%d x %d = %d" , nombre,i,(nombre*i)) ;
        
    }

    return 0 ;
}


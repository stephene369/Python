#include <stdio.h>


int main() {

    int nombre ;
    int i ;
    int factorielle=1;
    printf("Entrer un nombre : ") ;
    scanf ("%d",&nombre) ;

    for (i=nombre;i>=1;i--) {
        printf("%d",i) ;
        factorielle *= i ;
    }
    printf("Le facorielle de %d est %d",nombre,factorielle) ;

    return 0 ;

}



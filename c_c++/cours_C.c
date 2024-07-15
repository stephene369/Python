#include <stdio.h>
#include <stdlib.h>

// Déclarations de fonctions (facultatif)
int main() {

    char prenom[20] ;
    char nom[20] ;

    printf("Ton prenom : ");    scanf("%s" , &prenom) ;
    printf("Ton nom : ");       scanf("%d" , &nom) ;


    printf("on t'appel %s %s" , prenom , nom );
    return 0 ;

}

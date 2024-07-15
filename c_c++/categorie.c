#include <stdio.h>


char* main() {

    int age ;
    char ret ;

    printf("L'age de l'enfant : ") ;
    scanf("%d",&age) ;

    /*Methode 1 */
    printf("\n") ;

    if (age>=6 && age <7) {
        printf("Poussin ") ;
    }
    else if (age>=8 && age<9)
    {
        printf("Pupile ");
    }
    else if (age>=9 && age<11)
    {
        printf("Mimine") ;
    }
    else if (age>=12)
    {
        printf("Categorie : Cade") ;
    }
    else{
        printf("bebe") ;
    }
    
    return 0 ;

}
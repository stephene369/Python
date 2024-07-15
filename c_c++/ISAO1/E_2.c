#include <stdio.h>


int main() {

    int n, val, i ;
    printf("Les N valeurs du tableaux : ") ;
    scanf("%d",&n) ;
    
    int tab[n];

    for (i=0;i<n;i++) {
        if (i==0) {
        printf("\nElement[%d] : ",i);
        scanf("%d", &tab[i]) ;
        }
        else{
        printf("\nElement[%d] : ",i);
        scanf("%d", &tab[i]) ;
        while (tab[i-1]>=tab[i])
        {
            printf("\nEntrer a nouveau l'Element[%d] : ",i);
            scanf("%d", &tab[i]) ;
        }
        }
    }
    
    printf("Tableau dans l'ordre croissant : [ ") ;
    for (i=0;i<n;i++) {
        printf("%d , ", tab[i]) ;
    }
    printf("]") ;

    return 6;
}



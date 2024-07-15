#include <stdio.h>

int main(){

    int a,b,c,min ;
    a= 23 ;
    b =12 ;
    printf("Valeur de c : " ) ;
    scanf("%d" ,&c) ;
    min = a ;

    if (b<min) {
        min = b ;
    }
    if (c<min) {
        min=c ;
    }
    printf("La plus petite valeurs est %d , %d" , min , c) ;
    return 0 ;

}





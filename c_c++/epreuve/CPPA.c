#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void ordreCoissant() ;
void secondDegre() ;
void triCroissant() ;

int main() {
    int op ;
    printf("\nEXERCICE1 : Algorithme affichant dans l'ordre croissant tout antier naturel pair compris entre les entiers a et b ") ;
    printf("\nEXERCICE2 : Resolution d'equation d'une second degre") ;
    printf("\nEXERCICE3 : Tri par ordre croissant des elements d'un tableau") ;
    printf("\nEntrer le numero d'un exercice pour lancer le programme lui correspondant : \nExercice : ") ;
    scanf("%d" , &op) ;
    printf("\n\n") ;
    switch (op)
    {
    case 1:
        ordreCoissant(); 
        break;
    case 2 :
        secondDegre() ;
        break;
    case 3 :
        triCroissant() ;
        break;
    default:
        printf("Empty") ; 
        break;
    }
    return 0;
}

//EXERCICE 1
// Algorithme affichant dans l'ordre croissant tout entier naturel
//pair compris entre les entiers a et b 
void ordreCoissant() {
    int a,b,i ;
    printf("Entrer les nombre a et b telle que a<b\n") ;
    printf("\nEntrer le nombre a :\na = ") ; scanf("%d",&a) ;
    printf("\nEntrer le nombre b :\nb = ") ; scanf("%d",&b) ;

    while(a>=b){
        printf("a = ") ; scanf("%d",&a) ;
        printf("b = ") ; scanf("%d",&b) ;
    }
    printf("Nombre Paire entre a et b : [") ;
    for (i=a;i<=b;i++) {
        if ((i%2)==0){
            printf(" %d; ",i);
        }
    }    
    printf("]") ;
}


//EXERCICE 2 
//Resolution d'equation d'une second degre
void secondDegre() {
    int a,b,c;
    double disc ;
    printf("Equation de de type ax`2 + bx + c = 0") ;
    printf("\nEntrer le nombre a : \na = ") ; scanf("%d",&a) ;
    printf("\nEntrer le nombre b : \nb = ") ; scanf("%d",&b) ;
    printf("\nEntrer le nombre c : \nc = ") ; scanf("%d",&c) ;

    disc = (pow(b,2)) - (4*a*c) ;
    if ((a==0) & (b==0) & (c==0)){
        printf("\033[1;33m") ;
        printf("\nL'equation n'admet pas de solution") ;
    }
    else if (a==0){
        printf("\033[1;32m") ;
        printf("\nL'eqution admet une solution : x = %.2f",(float)-(c)/b );
    }
    else if (disc < 0) {
        printf("\033[1;31m") ;
        printf("\nLe discriminant est inférieur à 0.");
        printf("\nDonc l'équation n'adment pas de solution dans R") ;
    }
    else if (disc == 0 )
    {   printf("\033[1;34m") ;
        printf("\nLe disciminant est NULL alors l'equation admet une solution double");
        printf("\n X = %.2f", (float)((-b)/(2*a)) ) ;

    }
    else if (disc > 0) 
    {
        printf("\033[1;30m") ;
        printf("\nL'equation adment de deux solution : ") ;
        printf("\n X1 = %.2f", (float)( ((-b)-(sqrt(disc))) / (2*a)) );
        printf("\n X2 = %.2f", (float)( ((-b)+(sqrt(disc))) / (2*a)) );
    }
    
}



//EXERCICE 3 : 
//Tri par ordre croissant des elements d'un tableau
void triCroissant(){

    int N ;
    printf("Entrer le nombre d'element que dois contenir le tableau : N = ");
    scanf("%d",&N );
    int  i,j,a,tableau[N] ;

    for (i=0;i<N;i++){
        printf("\nTableau[%d] = ",i+1) ;
        scanf("%d",&tableau[i]) ;
    }

    for (i=0;i<N;i++) {
        for (j=i+1;j<N;j++){
            if (tableau[j] < tableau[i]){
                a = tableau[i] ;
                tableau[i] = tableau[j] ;
                tableau[j] = a ;
            }
        }
    }

    printf("\033[1;34m") ;
    printf("\nTableau dans l'ordre croissant : { ") ;
    for (i=0;i<N;i++){
        if (i==(N-1)){
            printf("%d",tableau[i]);
        }
        else {
            printf("%d , ",tableau[i]);
        }
    }
    printf(" }.") ;   
}



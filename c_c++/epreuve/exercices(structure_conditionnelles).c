#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void exercice1();
void exercice2();
void exercice3();
void exercice4();
void exercice5();
void exercice6();

int main() {

}
//Exercice 1 : Maximun entre 2 nombre 
void exercice1(){
    int a, b, c ;
    int d ; 
    printf("\nNombre a : ") ; scanf("%d",&a) ; 
    printf("\nNombre b : ") ; scanf("%d",&b) ; 
    printf("\nNombre c : ") ; scanf("%d",&c) ; 

    printf("\n") ;
    if ( (a>b) & (a>c)) {
        printf("Le maximun entre [ %d , %d , %d ] est : %d", a,b,c,a);
    }
    else if ( (b>a) & (b>c)) {
        printf("Le maximun entre [ %d , %d , %d ] est : %d", a,b,c,b);
    }
    else if ( (c>a) & (c>b)) {
        printf("Le maximun entre [ %d , %d , %d ] est : %d", a,b,c,c);
    }
    else {
        print("Pas de maximun") ;
    }
}

//Exercice 2 ; Signe du produit de a et b
void exercice2() {
    int a,b ;
    printf("\nNombre a : ") ; scanf("%d",&a) ; 
    printf("\nNombre b : ") ; scanf("%d",&b) ; 

    if ( ((a<0)&(b<0))||((a>0)&(b>0)) ) {
        print("\nLe produit est négatif") ;
    }
    else if ( (b==0)||(a==0) ) {
        print("\nLe produit est NULL") ;
    }
    else {
        printf("\nLe produit est négatif") ;
    }
}

//Exercice 3 ; Mention obtenu par un étudiant
void exercice3(){
    double moyenne ;

    if (moyenne<10){
        print("\nVous etes recalé") ;
    }
    else if ((moyenne>=10)&(moyenne<12)) {
        printf("\nMention Passable") ;
    }
    else if ((moyenne>=12)&(moyenne<14)) {
        printf("\nMention Assez bien") ;
    }
    else if ((moyenne>=14)&(moyenne<16)) {
        printf("\nMention bien") ;
    }
    else if ((moyenne>=16)) {
        printf("\nMention Très bien") ;
    }
}

//Exercice 4 ; Tester si un nombre entier est pair.
void exercice4(){
    int nombre ;
    printf("\nEntrer un nombre : ") ; scanf("%d",&nombre);

    if ((nombre%2)==0){
        printf("\nLe Chiffre %d est pair",nombre);
    }
    else{
        printf("\nLe Chiffre %d est impair",nombre);
    }
}

//Exercice 5 ; Année Bissextile 
void exercice5(){
    int annee ;
    print("\nAnnee : ") ; scanf("%d" , &annee) ;

    if ( ((annee%4)==0) || ((annee%100)==0) || ((annee%400)==0) ) {
        printf("\nL'annee %d est bissextile",annee) ;
    }
    else{
        printf("\nL'annee %d n''est pas bissextile",annee) ;
    }
}

//Exercice 6 ; Nombre en lettre 
void exercice6(){
    int nombre ;
    printf("\nEntrer un nombre : ") ; scanf("%d",&nombre);
    switch (nombre)
    {
    case 0:
        printf("Zero") ;
        break;
    case 5:
        printf("Cinq") ;
        break;
    case 9 :
        printf("Neuf") ;
        break;
    default:
        break;
    }
}




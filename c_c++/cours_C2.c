#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    char prenom[20] ;
    char nom[20] ;
    char nomCopie[20];
    char nom_prenom[20];
    char *suiteChaine = NULL ;
    char *suiteCaine2 = NULL ;
    char ecrire_dans[30];
    char texte[] = "Ceci est un texte contenant des mots";

    printf("\033[1;34m") ;
    printf("Ton nom : ");       scanf("%s" , &nom) ;
    printf("\033[1;35m") ;
    printf("Ton prenom : ");    scanf("%s" , &prenom) ;
    printf("\033[1;0m") ;

    // strlen pour calculer la longueur d'un chaon

    printf("\nLa longueur de ton nom est %d",strlen(nom)) ;
    printf("\nLa taille de ton prenom est %d", strlen(prenom)) ;

    // strcpy
    strcpy(nomCopie , nom) ;
    printf("\nLa copie du nom est %s",nomCopie) ;

    // strcat 
    strcat(strcat(nom ,"   ") , prenom );
    printf("\nPrenom dans nom donne : %s ",nom) ;

    //strcmp 
    if (strcmp("t","t")==0) {
        printf("\nLes chaines son identiques") ;
    }
    else {
        printf("\nLes chaines ne sont pas identique");
    }

    //strchr 
    suiteChaine = strchr(texte , 'u') ;
    if (suiteChaine !=NULL) {
        printf("\nLa suite de la chaine a partir du premier 'u' : %s" , suiteChaine) ;
    }

    //strpbrk
    suiteCaine2 = strpbrk(texte , "ces") ;
    if (suiteCaine2 != NULL){
        printf("\nLa suite de chaine a partie du premier [c,e,s] : %s" , suiteCaine2) ;
    }

    //strstr
    char *suiteCaine3 = NULL ;
    suiteCaine3 = strstr(texte , "texte") ;
    if (suiteCaine3 != NULL) {
        printf("\nLa suite de chaine de caractere apres 'texte' ",suiteCaine3) ;
    }

    //sprintf : stdio.h
    sprintf(ecrire_dans , "Bonjour %s " , nom );
    strcat(ecrire_dans , prenom) ;
    printf("\nChaine generer : %s" , ecrire_dans) ;
    
    sprintf(ecrire_dans , "Bonjour ");
    printf("\nChaine generer : %s" , ecrire_dans) ;


    return 0 ;

}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <dirent.h>

void date() ;
void pointeur() ; 
void manipulation() ;
void tab_tab() ; 
void tab2() ;
int addition(int a,int b) ;
void lire() ;
void ecrire();
void ranger();

int main() {

    //ecrire() ;
    //lire() ;
    ranger();
    //pointeur();
    return 0 ;

}                         

void ranger(){
    struct dirent *de ;
    DIR *dr = opendir(".") ;
    char tab[20][20] ,suffix[10][4] ;
    int i=0;
    char new[20] ;
    char suf[4] ;
    while ((de = readdir(dr)) != NULL)
    {
        printf("%s\n",de->d_name);
        //strcpy(tab[i],de->d_name) ;
        //printf("%s\n",tab[i]) ;
        //i++ ;
    }
    closedir(dr) ;    
}


void lire() {
    FILE* fichier = NULL ;
    fichier = fopen("file.txt" , "r") ;
    int caracter = 0;

// LIre une caractere
    if (fichier!=NULL){
        do {
            caracter=fgetc(fichier);
            printf("%c",caracter) ;
        }while(caracter!=EOF);
        printf("\n\n\n") ;

// Lire une chaine de caractere
    char chaine[100]="";
    fichier = fopen("file.txt" , "r") ;

    fgets(chaine,100,fichier) ;
    printf("%s",chaine) ;

// lire les chaine de caractere ligne par ligne
    printf("\n\n\n") ;
    fichier = fopen("file.txt" , "r") ;
    while (fgets(chaine,100,fichier)!=NULL) {
        printf("%s",chaine) ;
    }

// lire une chaine formatee
    printf("\n\n\nUNE CHAINE FORMATEE") ;
    int num[2] = {0} ;
    fichier = fopen("file.txt" , "r") ;
    fscanf(fichier,"%d",&num[0]) ;
    printf("Le premier nombre dans fichier est %d" , num[0]) ;
    
    //Positionner le curseur
    fseek(fichier , 2 , SEEK_SET) ;
    printf("\nPosition du curseur %d", ftell(fichier)) ;

    fseek(fichier , -2 , SEEK_CUR) ;
    printf("\nPosition du curseur %d", ftell(fichier)) ;

    fseek(fichier , 0 , SEEK_END) ;
    printf("\nPosition du curseur %d", ftell(fichier)) ;

    rewind(fichier) ;
    printf("\nPosition du curseur %d", ftell(fichier)) ;
    fclose(fichier) ;
//deplacer un fichier
    
    int value;
    char old[] = "file.txt" ;
    char new[] = "fichier.txt";

    value=rename(old,new) ;
    //remove("file.txt") ;
    printf("\nSuppression et renommage: %d",value) ;
    }
}

void ecrire() {
    //FILE* fopen(const char* file.txt , const shar* , "w");

    FILE* fichier = NULL ;
    fichier = fopen("file.txt" , "w") ;
// ecrire un char
    fputc('c',fichier) ;
//ecrire une chaine de char
    fputs("\nCeci est la deuxieme ligne" , fichier) ;
// une chaine formatee
    fprintf(fichier , "\nJe suis la %d ligne" ,3) ;
// close file
    fclose(fichier)    ;
}



void tab2() {
    int tab[2]={1,2};
}

int addition(int a , int b) {

    int add ;
    add = a+b ;
    return add ;

}


void tab_tab() {

    int tab[2][2] ;
    char *tabChar[2][2][12] ;

    int i,j ;
    for (i=0;i<2;i++)
    {
    for (j=0;j<2;j++) {
        printf("Nombre tab[%d][%d] = ",i,j) ;
        scanf("%d",&tab[i][j]) ;
    
        printf("\t\tChaine de caractere tabChar[%d][%d] = ",i,j) ;
        scanf("%s",&tabChar[i][j]) ;
         
    }
    }
    printf("\n") ;
    for (i=0;i<2;i++)
    {
    for (j=0;j<2;j++) {
        printf("\ntab[%d][%d] = %d",i,j,tab[i][j]) ;
        printf("\tChaine : tabChar[%d][%d] = %s",i,j,tabChar[i][j]) ;

    }

    }
}

void pointeur() {

    int* p ;
    int nb = 12 ;
    printf("Valeurs du pointeur %d ",nb) ;
    printf("\nLoc pointeur %d" ,p) ;
    printf("\nValeur %p" ,p) ;
    p = &nb ;
    printf("\nLoc pointeur %d" ,p) ; 
    printf("\nAdresse de nb %ld ",&nb) ;
    printf("\nValeur valeur pointeur %d" , *p) ;

    printf("\nAdresse momoire de nb %p",p);
    printf("\nAdresse momoire de nb %p",nb);
    printf("\nAdresse momoire de nb %p",&nb);

    printf("\n\ntaille de entier %d", sizeof(int));
    printf("\n\ntaille de char %d", sizeof(char));
    printf("\n\ntaille de chaine %d", sizeof(char*));

    int *prt = (int *)malloc(10 * sizeof(int)) ; 
    printf("\n\nAllocation dynamique") ; 
    //free(*p) ;
    //free(nb) ;


}

void date () {
    
    time_t seconds ;
    time_t seconds2 ;
    
    seconds = time(NULL) ;
    printf("Nombre de second depuis le 1 janvier 1970 %ld ",seconds) ;

    sleep(10) ;
    time(&seconds2)  ;
    printf("\n\nNombre de second depuis le 1 janvier 1970 %ld",seconds2) ;
}

void manipulation() {

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
}



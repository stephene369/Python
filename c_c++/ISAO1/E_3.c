#include <stdio.h>

int main() {

    int M,D,P,i;

    for (i=36;i>0;i--){ 
        M = i ; 
        D = 36-i ;
        
        if ( ((M*4)+(D*2)) !=100 ) {
            printf("Si M=%d alors D=%d donc p %dx4+%dx2=%d impossible\n",M,D,M,D,((M*4)+(D*2))) ;
        }
        else if (((M*4)+(D*2)) ==100 )
        {
           printf("\nSi M=%d alors D=%d donc p %dx4+%dx2=%d POSSIBLE\n",M,D,M,D,((M*4)+(D*2))) ;
           break;
        }
        
    }
    return 0 ;
}




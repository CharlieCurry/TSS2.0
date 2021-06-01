#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
#define Smax 2048
#define Smin 1024
#define SIZE 100
#define batch 8
#define min(x,y)    ((x)<(y)?(x):(y))
void print_Matrix(int **matrix,int PS,int M,int *array,FILE *fp,FILE *fp1){
    int n;
    for(int i=0;i<PS;++i){
        for(int k=0;k<512;){
            k=k+batch;
            printf("./process3.sh ");
            fprintf(fp,"./process3.sh ");

        for(int j=0;j<M;++j){
                printf("%d ",matrix[i][j]);
                fprintf(fp,"%d ",matrix[i][j]);

            }
            printf("%d %d %d\n",k,k,k);
            fprintf(fp,"%d %d %d\n",k,k,k);

    }

    }
}


void print_Array(int **matrix,int PS){
    for(int i=0;i<PS;++i){
	printf("%d\n",matrix[i]);
    }
}
int minPS(int a,int b,int c){
    return  c>(a>b?b:a)?(a>b?b:a):c;;
}
int main(){
FILE *fp = NULL;
FILE *fp1 =NULL;
fp = fopen("PS_rand_tiled.txt", "a+");
fp1= fopen("PS_rand_untile.txt", "a+");
    srand((unsigned)time(NULL));
    int** matrix=(int**)malloc(sizeof(int*)*SIZE);
    int* minps=(int*)malloc(sizeof(int)*SIZE);
    for(int i=0;i<SIZE;++i){
        matrix[i]=(int*)malloc(sizeof(int)*3);
    }
    for(int i=0;i<SIZE;++i){
        minps[i]=(int)malloc(sizeof(int)*3);
    }
    for(int i=0;i<SIZE;++i){
        matrix[i][0]=(int)1.0*rand()%(Smax-Smin+1)+Smin;
        matrix[i][1]=(int)1.0*rand()%(Smax-Smin+1)+Smin;
        matrix[i][2]=matrix[i][0];
        minps[i] = minPS(matrix[i][0],matrix[i][1],matrix[i][2]);
    }
    print_Matrix(matrix,SIZE,3,minps,fp,fp1);
     for(int i=0;i<SIZE;++i){
        fprintf(fp1,"./process3b.sh");
        for(int j=0;j<3;++j){
            fprintf(fp1," %d",matrix[i][j]);
        }
        fprintf(fp1,"\n");
    }

   fclose(fp);
   fclose(fp1);
return 0;
}


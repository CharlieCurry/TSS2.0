#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
#define Smax 1
#define Smin 0
#define alpha 0.6
#define beta 0.5
double **Init_Matrix_rand_PSxM(double **matrix,int PS,int M){
    matrix=(double**)malloc(sizeof(double*)*PS);
    for(int i=0;i<PS;++i){
        matrix[i]=(double*)malloc(sizeof(double)*M);
    }
    for(int i=0;i<PS;++i){
        for(int j=0;j<M;++j){
            //32767 (2^16-1)
            matrix[i][j]=(double)rand()/32767*(Smax-Smin)+Smin;
        }
    }
    return matrix;
}



double **Init_Matrix_zero_PSxM(double **matrix,int PS,int M){
    matrix=(double**)malloc(sizeof(double*)*PS);
    for(int i=0;i<PS;++i){
        matrix[i]=(double*)malloc(sizeof(double)*M);
    }
    for(int i=0;i<PS;++i){
        for(int j=0;j<M;++j){
            //32767 (2^16-1)
            matrix[i][j]=0;
        }
    }
    return matrix;
}

void free_Matrix(double **matrix,int PS){
     for(int i=0;i<PS;++i){
        free(matrix[i]);
    }
    free(matrix);
}

int main(int argc,char *argv[]){
    double **A,**C;
    FILE *fp = NULL;
 double Total_time = 0.0;
    srand((unsigned)time(NULL));
    int PS1 =atoi(argv[1]);
    int PS2 =atoi(argv[2]);
    int PS3 =atoi(argv[3]);
     int I = atoi(argv[4]);
    int J = atoi(argv[5]);
    int K = atoi(argv[6]);
   C = Init_Matrix_zero_PSxM(C,PS1,PS2);
    A = Init_Matrix_rand_PSxM(A,PS3,PS1);
  //  B = Init_Matrix_rand_PSxM(B,PS2,PS3);
    clock_t start1 = clock();
#pragma scop
for (int i=0;i<PS1;i++){
            for(int j=i;j<PS2;j++){
	for(int k=0;k<PS3;k++){
                C[i][j]+=A[k][i]*A[k][j];
            }
C[j][i]=C[i][j];
        }
    }
#pragma endscop
    clock_t finish1 = clock();
    double time1 =((double)(finish1 - start1)) / CLOCKS_PER_SEC;
    printf("%d %d %d %d %d %d %.10f\n",PS1,PS2,PS3,I,J,K,time1);
    fp = fopen("sourceCodeOut.txt", "a+");
    fprintf(fp," %d %d %d %d %d %d %.10f",PS1,PS2,PS3,I,J,K,time1);
    fclose(fp);
    free_Matrix(A,PS3);
   // free_Matrix(B,PS2);
   free_Matrix(C,PS1);	
return 0;
}


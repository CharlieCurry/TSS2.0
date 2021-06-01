#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
#define Smax 1
#define Smin 0
#include <omp.h>
#define alpha 0.6
double **Init_Matrix_rand_PSxM(double **matrix,int PS,int M){
    matrix=(double**)malloc(sizeof(double*)*PS);
    for(int i=0;i<PS;++i){
        matrix[i]=(double*)malloc(sizeof(double)*M);
    }
    for(int i=0;i<PS;++i){
        for(int j=0;j<M;++j){
            //32767 (2^16-1)
            matrix[i][j]=1;
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
void print_Matrix(double **matrix,int PS,int M){
     for(int i=0;i<PS;++i){
	for(int j=0;j<M;++j){
printf("%f ",matrix[i][j]);
}
printf("\n");
    }
}
int main(int argc,char *argv[]){
    double **A,**C;
    FILE *fp = NULL;
 double Total_time = 0.0;
    srand((unsigned)time(NULL));
    int PS1 =atoi(argv[1]);
    int PS2 =atoi(argv[2]);
    int PS3 =atoi(argv[3]);
    C = Init_Matrix_zero_PSxM(C,PS1,PS3);
    A = Init_Matrix_rand_PSxM(A,PS1,PS2);
double ompt1= omp_get_wtime();
#pragma scop
for (int i=0;i<PS1;i++){
        for(int j=0;j<PS3;j++){
            for(int k=j;k<PS2;k++){
                C[j][k] += A[i][j] * A[i][k];
            }
        }
    }
#pragma endscop
double ompt2 = omp_get_wtime();
double time2  = ompt2 - ompt1;
    printf("%d %d %d %.10f\n",PS1,PS2,PS3,time2);
    fp = fopen("sourceCodeOutb.txt", "a+");
    fprintf(fp," %d %d %d %.10f",PS1,PS2,PS3,time2);
//print_Matrix(C,PS1,PS3);
    fclose(fp);
    free_Matrix(A,PS1);
free_Matrix(C,PS1);
   // free_Matrix(B,PS2);
return 0;
}


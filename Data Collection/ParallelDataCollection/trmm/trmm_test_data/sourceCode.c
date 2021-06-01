#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
#define Smax 1
#include <omp.h>
#define Smin 0
#define alpha 0.6
double **Init_Matrix_rand_PSxM(double **matrix,int PS,int M){
    matrix=(double**)malloc(sizeof(double*)*PS);
    for(int i=0;i<PS;++i){
        matrix[i]=(double*)malloc(sizeof(double)*M);
    }
    for(int i=0;i<PS;++i){
        for(int j=0;j<M;++j){
            //32767 (2^16-1)
            matrix[i][j]=(double)rand()/32767*(Smax-Smin)+Smin;;
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
    double **A,**B;
    FILE *fp = NULL;
 double Total_time = 0.0;
    srand((unsigned)time(NULL));
    int PS1 =atoi(argv[1]);
    int PS2 =atoi(argv[2]);
    int PS3 =atoi(argv[3]);
     int I = atoi(argv[4]);
    int J = atoi(argv[5]);
    int K = atoi(argv[6]);
omp_set_num_threads(8); 
//PS1==PS2
// A is MxM = PS1*PS2
// B is MxN = PS2*PS3
   // C = Init_Matrix_zero_PSxM(C,PS1,PS3);
    A = Init_Matrix_rand_PSxM(A,PS1,PS2);
    B = Init_Matrix_rand_PSxM(B,PS2,PS3);
double ompt1= omp_get_wtime();
#pragma scop
for (int i=0;i<PS1;i++){
        for(int j=0;j<PS3;j++){
            for(int k=i+1;k<PS2;k++){
                B[i][j] += A[k][i] * B[k][j];
	B[i][j]=alpha*B[i][j];
            }
        }
    }
#pragma endscop
double ompt2 = omp_get_wtime();
double time2  = ompt2 - ompt1;
printf("omp time: %lf\n", time2);
    printf("%d %d %d %d %d %d %.10f\n",PS1,PS2,PS3,I,J,K,time2);
    fp = fopen("sourceCodeOut.txt", "a+");
    fprintf(fp," %d %d %d %d %d %d %.10f",PS1,PS2,PS3,I,J,K,time2);
    fclose(fp);
    free_Matrix(A,PS1);
    free_Matrix(B,PS2);
return 0;
}


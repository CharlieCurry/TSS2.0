#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
#define Smax 1
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
    double **A,**B;
    FILE *fp = NULL;
 double Total_time = 0.0;
    srand((unsigned)time(NULL));
//PS1==PS2
// A is MxM = PS1*PS2
// B is MxN = PS2*PS3
    int PS1 =atoi(argv[1]);
    int PS2 =atoi(argv[2]);
    int PS3 =atoi(argv[3]);
    //C = Init_Matrix_zero_PSxM(C,PS1,PS3);
    A = Init_Matrix_rand_PSxM(A,PS1,PS2);
    B = Init_Matrix_rand_PSxM(B,PS2,PS3);
    clock_t start1 = clock();
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
    clock_t finish1 = clock();
    double time1 =((double)(finish1 - start1)) / CLOCKS_PER_SEC;
    printf("%d %d %d %.10f\n",PS1,PS2,PS3,time1);
    fp = fopen("sourceCodeOutb.txt", "a+");
    fprintf(fp," %d %d %d %.10f",PS1,PS2,PS3,time1);
    fclose(fp);
    free_Matrix(A,PS1);
    free_Matrix(B,PS2);
return 0;
}


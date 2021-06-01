#include <omp.h>
#include <math.h>
#define ceild(n,d)  ceil(((double)(n))/((double)(d)))
#define floord(n,d) floor(((double)(n))/((double)(d)))
#define max(x,y)    ((x) > (y)? (x) : (y))
#define min(x,y)    ((x) < (y)? (x) : (y))

#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
#define Smax 1
#define Smin 0

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
void print_Matrix(double **matrix,int PS,int M){
     for(int i=0;i<PS;++i){
	for(int j=0;j<M;++j){
printf("%f ",matrix[i][j]);
}
printf("\n");
    }
}
int main(int argc,char *argv[]){
    double **A,**B,**C;
    FILE *fp = NULL;
 double Total_time = 0.0;
    srand((unsigned)time(NULL));
    int PS1 =atoi(argv[1]);
    int PS2 =atoi(argv[2]);
    int PS3 =atoi(argv[3]);
     int I = atoi(argv[4]);
    int J = atoi(argv[5]);
    int K = atoi(argv[6]);
    C = Init_Matrix_zero_PSxM(C,PS1,PS3);
    A = Init_Matrix_rand_PSxM(A,PS1,PS2);
    B = Init_Matrix_rand_PSxM(B,PS2,PS3);
omp_set_num_threads(8); 
int numProcs = omp_get_num_procs();
printf( "omp_get_num_procs() =%d ", numProcs);
double ompt1= omp_get_wtime();
/* Copyright (C) 1991-2018 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 10.0.0.  Version 10.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2017, fifth edition, plus
   the following additions from Amendment 1 to the fifth edition:
   - 56 emoji characters
   - 285 hentaigana
   - 3 additional Zanabazar Square characters */
/* We do not support C11 <threads.h>.  */
  int t1, t2, t3, t4, t5, t6;
 int lb, ub, lbp, ubp, lb2, ub2;
 register int lbv, ubv;
/* Start of CLooG code */
if ((PS1 >= 1) && (PS2 >= 1) && (PS3 >= 1)) {
  lbp=0;
  ubp=min(min(floord(PS1-1,512),floord(PS2-1,512)),floord(PS3-1,512));
#pragma omp parallel for private(lbv,ubv,t2,t3,t4,t5,t6)
  for (t1=lbp;t1<=ubp;t1++) {
    for (t2=t1;t2<=floord(PS3-1,512);t2++) {
      for (t3=t1;t3<=floord(PS2-1,512);t3++) {
        for (t4=512*t1;t4<=min(min(min(PS1-1,PS2-1),PS3-1),512*t1+511);t4++) {
          for (t5=max(512*t3,t4);t5<=min(PS2-1,512*t3+511);t5++) {
            lbv=max(512*t2,t4);
            ubv=min(PS3-1,512*t2+511);
#pragma ivdep
#pragma vector always
            for (t6=lbv;t6<=ubv;t6++) {
              C[t4][t6] += A[t4][t5] * B[t5][t6];;
            }
          }
        }
      }
    }
  }
}
/* End of CLooG code */
double ompt2 = omp_get_wtime();
//    clock_t finish1 = clock();
double time2  = ompt2 - ompt1;
//    double time1 =((double)(finish1 - start1)) / CLOCKS_PER_SEC;
printf("omp time: %lf\n", time2);
    printf("%d %d %d %d %d %d %.10f\n",PS1,PS2,PS3,I,J,K,time2);
    fp = fopen("sourceCodeOut.txt", "a+");
    fprintf(fp," %d %d %d %d %d %d %.10f",PS1,PS2,PS3,I,J,K,time2);
    fclose(fp);
//print_Matrix(C,PS1,PS3);
    free_Matrix(A,PS1);
    free_Matrix(B,PS2);
    free_Matrix(C,PS1);
return 0;
}


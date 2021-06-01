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
//PS1==PS2
// A is MxM = PS1*PS2
// B is MxN = PS2*PS3
    C = Init_Matrix_zero_PSxM(C,PS1,PS3);
    A = Init_Matrix_rand_PSxM(A,PS1,PS2);
   // B = Init_Matrix_rand_PSxM(B,PS2,PS3);
    clock_t start1 = clock();
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
 register int lbv, ubv;
/* Start of CLooG code */
if ((PS1 >= 1) && (PS2 >= 1) && (PS3 >= 1)) {
  for (t1=0;t1<=min(floord(PS2-1,512),floord(PS3-1,512));t1++) {
    for (t2=t1;t2<=floord(PS2-1,512);t2++) {
      for (t3=0;t3<=floord(PS1-1,512);t3++) {
        for (t4=512*t1;t4<=min(min(PS2-1,PS3-1),512*t1+511);t4++) {
          for (t5=512*t3;t5<=min(PS1-1,512*t3+511);t5++) {
            lbv=max(512*t2,t4);
            ubv=min(PS2-1,512*t2+511);
#pragma ivdep
#pragma vector always
            for (t6=lbv;t6<=ubv;t6++) {
              C[t4][t6] += A[t5][t4] * A[t5][t6];;
            }
          }
        }
      }
    }
  }
}
/* End of CLooG code */
    clock_t finish1 = clock();
    double time1 =((double)(finish1 - start1)) / CLOCKS_PER_SEC;
    printf("%d %d %d %d %d %d %.10f\n",PS1,PS2,PS3,I,J,K,time1);
    fp = fopen("sourceCodeOut.txt", "a+");
    fprintf(fp," %d %d %d %d %d %d %.10f",PS1,PS2,PS3,I,J,K,time1);
    fclose(fp);
    free_Matrix(A,PS1);
free_Matrix(C,PS2);
   // free_Matrix(B,PS2);
return 0;
}


#include <stdio.h>
#include "math.h"
#include <stdlib.h>
#include "time.h"
int main(int argc,char *argv[]){
    int PS1 = atoi(argv[1]);
    int PS2 = atoi(argv[2]);
    int PS3 = atoi(argv[3]);
    int I = atoi(argv[4]);
    int J = atoi(argv[5]);
    int K = atoi(argv[6]);
    FILE *fp = NULL;
    fp = fopen("tile.sizes", "r+");
    fprintf(fp,"%d %d %d\n",I,J,K);
printf("%d %d %d\n",I,J,K);
    fclose(fp);
    return 0;
}


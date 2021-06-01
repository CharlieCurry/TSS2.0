./setTileSize.out $1 $2 $3 $4 $5 $6
../polycc sourceCode.c --tile --parallel  workspace/sourceCode.pluto.c
g++ -O2 -fopenmp sourceCode.pluto.c -o sourceCode.pluto.out
time ./sourceCode.pluto.out $1 $2 $3 $4 $5 $6

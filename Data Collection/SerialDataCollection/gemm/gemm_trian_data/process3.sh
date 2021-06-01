./setTileSize.out $1 $2 $3 $4 $5 $6
../polycc sourceCode.c --tile workspace/sourceCode.pluto.c
g++ -O2 sourceCode.pluto.c -o sourceCode.pluto.out
./sourceCode.pluto.out $1 $2 $3 $4 $5 $6

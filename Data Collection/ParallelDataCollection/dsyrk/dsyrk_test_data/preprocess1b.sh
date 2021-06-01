../polycc sourceCodeb.c --parallel workspace/sourceCodeb.pluto.c
g++ -O2 -fopenmp sourceCodeb.pluto.c -o sourceCodeb.pluto.out
./process2b.sh


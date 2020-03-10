gcc -Wall -I/home/ritesh/gsl/include -c GSL_LU_Decomposition.c
gcc -L/home/ritesh/gsl/lib GSL_LU_Decomposition.o -lgsl -lgslcblas -lm

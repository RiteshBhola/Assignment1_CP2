#include<stdio.h>
#include<stdlib.h>
#include <gsl/gsl_vector.h>
#include<gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_blas.h>

  //function for printing matrices
void Print(gsl_matrix *A,int rows,int cols)  
{
for (int i = 0; i < rows; i += 1)
  {
     for (int j = 0; j < cols; j += 1)
       printf("%f ",gsl_matrix_get(A,i,j));
        printf("\n");
  }
}  

//Driver 
int main()
{
  int i,j,rows=3,cols=3,s;
  i=j=0;
  double a[3][3]={{1,0.67,0.33},{0.45,1,0.55},{0.67,0.33,1}};
  
  gsl_matrix *A,*L,*U,*C;
  A = gsl_matrix_calloc(rows,cols);
  C = gsl_matrix_calloc(rows,cols);
  L = gsl_matrix_calloc(rows,cols);
  gsl_matrix_set_identity(L);
  U = gsl_matrix_calloc(rows,cols);
  gsl_permutation * p = gsl_permutation_alloc (3);
  gsl_permutation_init (p);
  
  for (i = 0; i < rows; i += 1)
  for (j = 0; j < cols; j += 1)
   gsl_matrix_set(A,i,j,a[i][j]);
     	
  
  
  printf("Matrix A\n");
  Print(A,rows,cols);
  //LU decomposition
 gsl_linalg_LU_decomp(A, p,&s);

  for (i = 0; i < rows; i += 1)
  {
     for (j = 0; j < cols; j += 1)
     {
     	       if(i>j)
     	  gsl_matrix_set(L,i,j,gsl_matrix_get(A,i,j));
     	  
     	  
     	       if(i<=j)
     	  gsl_matrix_set(U,i,j,gsl_matrix_get(A,i,j));
     	  
     }  	
  }
  printf("Matrix L\n");
  Print(L,rows,cols);
  
  printf("Matrix U\n");
  Print(U,rows,cols);
  
  //matrix multiplication LU and stored in C
  gsl_blas_dgemm (CblasNoTrans, CblasNoTrans,
                  1.0,L,U,
                  0.0,C);
  
  printf("Matrix LU\n");
  Print(C,rows,cols);
  return 0;
}


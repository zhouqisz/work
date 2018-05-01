

#include "stdio.h"
#include "time.h"



static int fib(int n){
    if(n==0)
            return 0;
    if(n==1)
            return 1;
    return fib(n-1)+fib(n-2);
}
int main(){
    clock_t t=clock();
    printf("%d\n",fib(40));
    printf("%f sec\n",(clock()-t)/1000.0/1000.0);
}

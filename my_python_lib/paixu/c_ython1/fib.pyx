import time

cdef int fib(int n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
t=time.time()
print(fib(40))
print(time.time()-t)

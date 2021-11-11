# Fibonacci number is true or false
def isFibonacci(n):
    c,a,b=0,1,1
    if n==0 or n==1:
        return True
    else:
        while c<n:
            c=a+b
            a=b
            b=c
        if c==n:
            return True
        else:
            return False
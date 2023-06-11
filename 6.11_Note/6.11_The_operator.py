# The symbol : + - * / %
n = int(input("What is the input value n?"))
def odd_or_even(n):
    n = n % 2
    if n==1:
        print("This number is odd.")
    else:
        print("This number is even")

odd_or_even(n);

def fib(n):
    if  n==1 or n == 0:
        return 1
    if n > 1:
        return fib(n-1) + fib(n-2)

print(int(fib(n)))
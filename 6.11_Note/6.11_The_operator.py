# The symbol : + - * / %
# n = int(input("What is the input value n?"))
def odd_or_even(n):
    n = n % 2
    if n == 1:
        print("This number is odd.")
    else:
        print("This number is even")


def fib(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)

#A dynamic processing in find Fibonacci number on python
#6.12
def fib_dp(n):
    fib = [0 for a in range(n + 1)]
    fib[0] = 0
    fib[1] = 1

    x = range(2,n+1)
    for i in x:
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib[n])


def test():
    n = int(input("What is the input value n?"))
    if n <= 1:
        print(f"Fib{n} is {n}")
    else:
        print(f"Fib({n}) is ", end="")
        fib_dp(n)


test()

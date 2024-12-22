def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)


n=5
result = fact(n)
print(f'fact of {n} is {result}')
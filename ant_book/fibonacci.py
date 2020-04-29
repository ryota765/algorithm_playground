def fibonacci(num,a=0,b=1):
    num -= 1
    if num == 0:
        return a+b
    else:
        return fibonacci(num,b,a+b)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(10))
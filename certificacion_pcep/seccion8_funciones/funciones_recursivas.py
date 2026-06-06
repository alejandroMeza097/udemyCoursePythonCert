#Factorial
def factorial(num : int) -> int:
    factorial_total : int = 1
    for num in range(1,num + 1):
        factorial_total = factorial_total * num
    return factorial_total

#Factorial de forma recursiva
def factorial_rec(num : int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial_rec(4))

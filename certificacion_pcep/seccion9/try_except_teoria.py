x : int = 10
y : int = 0

try:
    print(x/y)
except ZeroDivisionError as zderr:
    print(zderr)
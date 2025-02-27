import math

def mltply(n):
    return math.prod(n)

n = input()
n = list(map(int, n.split()))
result = mltply(n)
print(result)
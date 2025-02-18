def func(n):
    cnt = n
    while cnt >= 0:
        yield cnt
        cnt -= 1
        
n = int(input())
for a in func(n):
    print(a, end=" ")
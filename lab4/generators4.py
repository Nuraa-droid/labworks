def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = int(input()), int(input())
for ans in squares(a, b):
    print(ans, end=" ")

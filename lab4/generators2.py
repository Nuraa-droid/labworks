def even_nums(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input())
print(",".join(even_nums(n)))
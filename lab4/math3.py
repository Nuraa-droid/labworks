import math

def area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

n = int(input("Input number of sides:"))
s = int(input("Input the length of a side:"))
ans = area(n, s)
ans = round(ans)
print(f"The area of the polygon is: {ans}")
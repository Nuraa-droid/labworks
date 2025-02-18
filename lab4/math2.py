def area(h, a, b):
    return (a + b) * h / 2

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
ans = area(h, a, b)
print(f"area = {ans}")
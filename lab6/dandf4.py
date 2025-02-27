filename = input()
with open(filename, "r") as file:
    lines = sum(1 for line in file)

print(lines)
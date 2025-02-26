import re

def splitt(s):
    result = re.split(r'(?=[A-Z])', s)
    return [a for a in result if a]

s = input()
print(splitt(s))
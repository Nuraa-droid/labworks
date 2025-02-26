import re

def insert(s):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    return result
s = input()
print(insert(s))
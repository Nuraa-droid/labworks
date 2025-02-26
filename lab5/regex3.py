import re

def find(s):
    pattern = r"\b[a-z]+_[a-z]+\b"
    matches = re.findall(pattern, s)
    return matches

s = input()
print(find(s))
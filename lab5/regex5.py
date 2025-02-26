import re

def check(s):
    pattern = r"^a.*b$"
    if re.fullmatch(pattern, s):
        return "match"
    else:
        return "no match"

s = input()
print(check(s))
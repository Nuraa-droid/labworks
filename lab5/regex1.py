import re

def match_string(s):
    pattern = r"^ab*$"
    if re.fullmatch(pattern, s):
        return "match"
    else:
        return "no match"
    
s = input()
print(match_string(s))
import re

def match_string(s):
    pattern = r"^ab{2,3}$"
    if re.fullmatch(pattern, s):
        return "match"
    else:
        return "no match"
    
s = input()
print(match_string(s))
import re

def match_string(s):
    pattern = r"\b[A-Z][a-z]+\b"
    matches = re.findall(pattern, s)
    return matches
    
s = input()
print(match_string(s))
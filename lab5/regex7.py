import re

def convert(snake):
    camel = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake)
    return camel

snake = input()
print(convert(snake))
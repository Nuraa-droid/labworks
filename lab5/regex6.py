import re

def replace(text):
    pattern = r"[ ,.]"
    result = re.sub(pattern, ":", text)
    return result

text = input()
print("new text:", replace(text))
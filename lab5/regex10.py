import re

def convert(camel):
    snake = re.sub(r'([A-Z])', r'_\1', camel).lower()
    return snake.lstrip('_')
camel = input()
print(convert(camel))
import string

def create_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        print(filename)

create_files()
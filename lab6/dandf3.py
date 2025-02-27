import os

def check(path):
    if os.path.exists(path):
        print("path exists")

        filename = os.path.basename(path)
        print(f"filename: {filename}")

        directory = os.path.dirname(path)
        print(f"directory: {directory}")

    else:
        print("path does not exists")

path = input()
check(path)
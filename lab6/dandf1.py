import os

def lst(path):
    if not os.path.exists(path):
        print("Path do not exists")
        return
    
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("\nDirectories:")
    for d in directories:
        print(d)

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("\nFiles")
    for f in files:
         print(f)

    print("\nAll files and directories:")
    for item in os.listdir(path):
        print(item)

path = input()
lst(path)
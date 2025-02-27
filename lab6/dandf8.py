import os

def delete_path(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
        else:
            print("path is not writable")
    else:
        print("path does not exists!")
path = input()
delete_path(path)
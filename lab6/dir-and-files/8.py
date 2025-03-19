import os

path = r"C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files\23.py"

exists=os.access(path, os.F_OK)

if exists:
    os.remove(path)
else:
    print("Path does not exist")
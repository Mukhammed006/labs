import os
import string

path=r"C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files"

exists=os.access(path, os.F_OK)

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("hello world")

if exists:
    generate_files()
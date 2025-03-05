import os
path = r'C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files\t.txt'

files = os.listdir(path)
with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}; {}'.format(os.path.base_name(path), len(lines)))
import os
path=r"C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files"
path_exists=os.access(path, os.F_OK)

if path_exists:
    print("Directions:", ', '.join([name for name in os.listdir(path) if os.path.isdir(path, name)]))
    print("Files:", ', '.join([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))
else:
    print("Path does not exist")
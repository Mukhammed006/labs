import os 

path = r'C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files'

print('Exists:', os.access(path, os.F_OK))
print('Access to read:', os.access(path, os.R_OK))
print('Access to write:', os.access(path, os.W_OK))
print('Can be executed:', os.access(path, os.X_OK))

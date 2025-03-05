with open(r'C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files\t.txt', 'r') as f1:
    with open('new_t.txt', 'w') as f2:
        f2.write(f1.read())
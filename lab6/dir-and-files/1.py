import os
path=r"C:\Users\Mukha\Desktop\PP2_vs code\lab6\dir-and-files"

with os.scandir(path) as entries:
    all_items = []
    folders = []
    files = []

    for entry in entries:
        all_items.append(entry.name)
        if entry.is_dir():
            folders.append(entry.name)
        if entry.is_file():
            files.append(entry.name)

print(f"All: {', '.join(all_items)}")
print(f"Folder: {', '.join(folders) if folders else ''}")
print(f"File: {', '.join(files) if files else ''}")

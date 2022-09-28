import os
path = os.getcwd() 
print("Current dir:", path)
path1 = os.startfile(path)
print(path1)


entries = os.scandir(path)
with os.scandir(path) as entries:
    for entry in entries:
        print(entry.name)

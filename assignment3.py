1.
import os
from pathlib import Path
path = os.getcwd()
print(f'Current path: {Path.cwd()}')
def count_directories(path):
    return f'antal kataloger: {len([entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))])}'
def count_files(path):
    return f'antal filer: {len([entry for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))])}'
print(count_directories(path))
print(count_files(path))
2.
import os
path = os.getcwd()
print(path)
text = '''1. List directories
2. Change directory
3. List files
4. Quit
'''
val = int(input(text))
while val != 4:
    if val == 1:
        def list_dir(path):
            return next(os.walk('.'))[1]
        print(list_dir(path))
    elif val == 3:
        def list_files(path):
            return next(os.walk('.'))[2]
        print(list_files(path))
    elif val == 2:
        x = input('katalog ')
        os.chdir(x)
        path = os.getcwd()
        print(path)
    val = int(input('s '))
11.
import random
lst = []
for i in range(100):
    f = random.randint(1,200)
    lst.append(f)
print(lst)
def different(x):
    y = set(x)
    y = sorted(y)
    return list(y)
print(different(lst))
5.
import os
path = os.getcwd()
filename = input("filename: ")
print("Enter the content and end with 'stop':")
buffer = []
while True:
    print("> ", end="")
    line = input()
    if line == "stop":
        break
    buffer.append(line)
content = "\n".join(buffer)
print("You entered...")
print()
print(content)
def writing(path, filename, content):
    with open(f'{path}\{filename}',"w") as file:
        return file.write(content)
print(writing(path, filename, content))
6.
import os
path = os.getcwd()
filename = input('skriv in valfritt filnamn: ')
def reading(path, filename):
    counter = 0
    with open(f'{path}\{filename}',"r") as reader:
        content = ''
        for line in reader.readlines():
            content = content + line
            counter += 1
        allt = f'''antal rader: {counter}\ncontent:\n{content}'''
        return allt
print(reading(path,filename))
8.
import os
import re
path = os.getcwd()
input_file = 'life_of_brian(1).txt'
number_of_words = 0
x = []
# Opening our text file in read only
# mode using the open() function
with open(input_file, 'r') as file:
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
    # Splitting the data into separate lines
    # using the split() function
    lines = data.split()
    print(lines)
    #x.append(lines)
    # Adding the length of the
    # lines in our number_of_words
    # variable
    number_of_words += len(lines)
#for i in x:
   # print(i,'\n')
#print(*x, sep="\n")
print(x)
# Printing total number of words
print(number_of_words)
#print(x[1])
#with open("testfile1.txt", "x") as f:
    #for row in x:
       # print(", ".join(row), file=f)
12.
import random
lst = []
for i in range(100):
    y = random.randint(1,10)
    lst.append(y)
dic = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,}
for i in dic:
    for y in lst:
        if y == i:
            dic[i] += 1
print(dic)

import random
lst = []
for i in range(100):
    y = random.randint(1,10)
    lst.append(y)
def count_occurences(lst):
    dic = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,}
    for i in dic:
        for y in lst:
            if y == i:
                dic[i] += 1
    return dic
print(count_occurences(lst))

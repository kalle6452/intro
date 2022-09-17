1.
summa = 0
for i in range(1,101):
    if i%2==0:
        summa += i
print(summa)
2.
count = 0
sum = 0

for i in range(0,100):
    sum = sum + count
    count = count + 1

print(sum)
3.
tal = int(input('skriv in ett tal '))
summa = 0
if tal < 0:
    print('Endast positiva heltal är tillåtna.')
for i in range(0,tal):
    if i%2==0:
        summa += i
        if summa > tal:
            print(i-2)
            break
4. Primtal ofärdig
primtal = int(input('skriv in antal primtal '))
counter = 0
for num in range(2, 99999999):
    if counter < primtal:
        if all(num % i != 0 for i in range(2, num)):
            if counter%9==0 and counter != 0:
                #print(counter)
                print(num)
            else:
                print(num,end=' ')
            counter += 1
5.
import random
x = 0
faces = {1:[],2:[],3:[],4:[],5:[],6:[]}
for i in range(0,5242880):
    x = random.randint(1,6)
    #print(x)
    faces[x] += [1]
print(faces)
print(faces.values())
print(faces.keys())
#print(faces[1].count(1))
#print(faces[2].count(1))
lista = []
for i in range(1,7):
    #print(faces[i].count(1))
    lista.append(faces[i].count(1))
print(max(lista))
svar = max(lista)
svar1 = min(lista)
svar3 = max(lista) - min(lista)
svar4 = svar3/max(lista)
print(svar4*100)
5.1
import random
x = 0
rolls = 2621440
faces = {1:[],2:[],3:[],4:[],5:[],6:[]}
for i in range(0,rolls):
    x = random.randint(1,6)
    faces[x] += [1]
lista = []
for i in range(1,7):
    lista.append(faces[i].count(1))
svar = (max(lista) - min(lista))/max(lista)
svar *= 100
print(f'om man kastar tärningen {rolls} är skillnaden {svar}%')
6.
import random
störst = 0
minst = 0
alla = 0
n = int(input('Skriv in hur många siffror som ska skrivas ut '))
if n < 0:
    print('Var vänlig skriv in ett positivt tal. ')
else:
    print('Genererade tal:',end=' ')
    for i in range(n):
        tal = random.randint(1,100)
        print(tal, end=' ')
        if i == 0:
            störst += tal
            alla += tal
            minst += tal
        else:
            alla += tal
            if tal > störst:
                störst = tal
            elif tal < minst:
                minst = tal
    print()
    print(f'störst, minst, genomsnitt: {störst}, {minst}, {alla/n}')
7.
even = 0
odd = 0
zero = 0
print(1%7)
n = int(input('skriv in ett tal '))
while n:
    #x = n // 10
    print(n)
    if n%2==0:
        if n%0.1 != 0:
            even += 1
        else:
            zero += 1
    elif n%2!=0:
        odd += 1
    n //= 10
print(f'jämna: {even}, udda: {odd}, noll: {zero}')
9.
import random
n = random.randint(0,3)
def pronoun(n):
    n = random.randint(0,3)
    dic = {0:'I', 1:'You', 2:'It', 3:'We', 4:'They'}
    z = dic.get(n)
    return z
def verb(n):
    dic = {0: 'see', 1: 'eat', 2: 'pull', 3: 'touch', 4: 'smell'}
    x = dic.get(n)
    return x
def noun(n):
    dic = {0: 'house', 1: 'car', 2: 'computer', 3: 'tree', 4: 'bike'}
    y = dic.get(n)
    return y
for i in range(0,10):
    n = random.randint(0, 3)
    print(f'{pronoun(n)} will {verb(n)} a {noun(n)}')

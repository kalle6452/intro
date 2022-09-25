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
8.
age = 0
candles = 24
box = 1
box_count = 0
candle_total = 0
while age <= 99:
    age += 1
    candles -= age
    candle_total += age
    while candles <= 0:
        candles += 24
        box += 1
        box_count += 1
        print(age, box_count)
    box_count = 0
print(age, candles, box, candle_total)
print(f'Total number of boxes: {box}, Remaining candles: {candles}')
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
10.
import random
n = random.randint(0,100)
t = random.randint(0,100)
print(n)
print(t)
def inc(n):
    return n+1
def inc_with(n,t):
    return n+t
def dec(n):
    return n-1
def dec_with(n,t):
    return n-t
def greatest(n,t):
    if n > t:
        return n
    else:
        return t
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
def power(n,t):
    return n**t
def fac(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac*i
    return fac
print(f'{n}+1 = {inc(n)}')
print(f'{n}-1 = {dec(n)}')
print(f'{n}+{t} = {inc_with(n,t)}')
print(f'{n}-{t} = {dec_with(n,t)}')
print(f'största värdet: {n} eller {t}? svar: {greatest(n,t)}')
print(f'är {n} jämnt? svar: {is_even(n)}')
print(f'{n} upphöjt till {t}: {power(n,t)}')
print(f'{3} factorial: {fac(3)}')
11.
x1 = int(input('xkoordinat ett '))
y1 = int(input('ykoordinat ett '))
x2 = int(input('xkoordinat två '))
y2 = int(input('ykoordinat två '))
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(f'avståndet mellan ({x1}.0,{y1}.0) till ({x2}.0,{y2}.0) är {round(distance,3)}')
12.
import string
s = 'I am 1 with the Force, not 2...'
def first_last(s):
    return f'första och sista i: "{s}": {s[:1]}, {s[-1:]}'
def char_types(s):
    antal = 0
    antal0 = 0
    antal1 = 0
    for i in s:
        antal += 1
    x = ['a','e','i','o','u','y','å','ä','ö','A', 'E', 'I', 'O', 'U', 'Y', 'Å', 'Ä', 'Ö']
    v = [i for i in s if i in x]
    for i in v:
        antal0 += 1
    z = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X']
    f = [i for i in s if i in z]
    for i in f:
        antal1 += 1
    return f'Det finns {antal0} vokaler och {antal1} konsonanter'
def symbol(s):
    antal = 0
    antal0 = 0
    antal1 = 0
    for i in s:
        antal += 1
    x = ['a','e','i','o','u','y','å','ä','ö','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','A', 'E', 'I', 'O', 'U', 'Y', 'Å', 'Ä', 'Ö','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X']
    z = ['0','1','2','3','4','5','6','7','8','9']
    v = [i for i in s if i in x]
    for i in v:
        antal0 += 1
    f = [i for i in s if i in z]
    for i in f:
        antal1 += 1
    return f'bokstäver: {antal0}, siffror: {antal1}, symboler: {antal-(antal0+antal1)}'
print(first_last(s))
print(char_types(s))
print(symbol(s))
13.
import random
a = str(random.randint(1,9))
b = str(random.randint(0,9))
c = str(random.randint(0,9))
d = str(random.randint(1,9))
abcd = a+b+c+d
dcba = d+c+b+a
abcd = int(abcd)
dcba = int(dcba)
print(abcd)
while 4*abcd != dcba:
    a = str(random.randint(1, 9))
    b = str(random.randint(0, 9))
    c = str(random.randint(0, 9))
    d = str(random.randint(1, 9))
    abcd = a + b + c + d
    dcba = d + c + b + a
    abcd = int(abcd)
    dcba = int(dcba)
    if 4*abcd == dcba:
        break
print(abcd)
print(dcba)
15.
import random

lista = ['ask again later', 'yes', 'concentrate','screw you']

inp = input('8-ball: ')
while inp != 'stop':
    i = random.randint(0,3)
    print(lista[i])
    inp = input('8-ball ')
16.
import random
lista = []
x = 0
for i in range(1,100):
    y = random.randint(1,10000)
    lista.append(y)
    x += y
lista.sort()
print(f'störst: {max(lista)}, minst: {min(lista)}, genomsnitt: {x/100}, näst störst: {lista[-2]}')
17.
import random
suits = ['spades', 'hearts', 'diamonds', 'clubs']
faces = ['ace']
faces += range(2, 11)
faces += ['jack', 'queen', 'king']
deck = ['%s of %s'%(f, s) for f in faces for s in suits]
print(deck)
for i in range(0,5):
    tal = random.randint(0, 51)
    print(deck[tal])
18.
s = 'Ni talar bra latin!'
def is_palindrome(s):
    import re
    regex = re.compile(r'\s+')
    s1 = s.lower()
    s2 = re.sub(regex, '', s1)
    list=['?','!','.']
    s2="".join(i for i in s2 if i not in list)
    s3 = s2[::-1]
    if s2 == s3:
        return True
print(is_palindrome(s))
19.
import random
n = 5
def random_num_list(n):
    lista = [random.randint(0,100) for i in range(n)]
    return lista
lista = random_num_list(n)
print(f'lista: {lista}')
def only_odd(lista):
    lista = [i for i in lista if i%2!=0]
    return lista
print(f'udda: {only_odd(lista)}')
def square(lista):
    lista = [i**2 for i in lista]
    return lista
print(f'kvadrerade: {square(lista)}')
def sublist(lista):
    lista1 = lista[1:-1]
    return lista1
print(f'de i mitten: {sublist(lista)}')
21.
tal = input('Löner: ')
lista = tal.split()
lista = list(map(int, lista))
x = 0
y = len(lista)
lista = sorted(lista)
for i in lista:
    x += i
print(f'Genomsnitt: {round(x/y)}')
index = (y - 1) // 2
if (y % 2):
    median = round(lista[index])
    print(f'median: {median}')
else:
    median = (lista[index] + lista[index + 1])/2.0
    median = round(median)
    print(f'Median: {median}')
genomsnitt = lista[-1] - lista[0]
genomsnitt = round(genomsnitt)
print(f'genomsnitt: {genomsnitt}')

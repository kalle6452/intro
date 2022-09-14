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

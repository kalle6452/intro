1. a
print('Knowledge is power!')
1. b
print('Knowledge\nis\npower!')
print('Knowledge')
x = 'is'
y = 'Power!'
x.center(3)
print(x.center(7))
print(y.center(10))
1. c
for i in range(26):
    print('=',end='')
print()
print('|                        |')
print('|  Knowledge is power!   |')
print('|                        |')
for i in range(26):
    print('=',end='')
2.
x = input('Write a line of text: ')
print('Quote: ' + f'"{x}"')
3.
F = float(input('Skriv in temperatur i fahrenheit '))
x = 9/5
C = (F - 32)/x
print(C)
4.
savings = 1000
interest = 1.09
years = 5
x = 0
for i in range(years):
    x = savings * interest
    savings = x
print(round(x))
5.
import math
r = int(input('Skriv in radien'))
r = r**3
x = 4/3
v = x*math.pi*r
print(round(v,1))
6.
time = int(input('Skriv in tiden '))
future = int(input('Skriv in när alarm går '))
summa = time + future
alarm = summa%24
print(f'larmet går {alarm}.00')
9.
tal = int(input('type a number '))
if tal < 0:
    print(f'{tal} is negative')
elif tal == 0:
    print(f'{tal} is zero')
else:
    print(f'{tal} is positive')
10.
a = 132
b = 153
c = 1723
if a > b and a > c:
  print(f'största talet är {a}')
elif b > a and b > c:
  print(f'största talet är {b}')
else:
  print(f'största talet är {c}')
11.
import random
talx = 0
tal = random.randint(-10, 10)
#print(tal)
talx = tal % 2
#print(talx)
if talx == 0 and tal < 0:
  print(f'{tal} är jämnt och negativt')
elif talx == 0 and tal > 0:
  print(f'{tal} är jämnt och positivt')
elif talx != 0 and tal > 0:
  print(f'{tal} är udda och positivt')
else:
  print(f'{tal} är udda och negativt')
12.
first = input('Write first name.')
second = input('Write second name.')
last = input('Write last name.')
print(f'{first[0]}. {second[0]}. {last[0:-1]}')
13.
dag = input('Skriv in en veckodag på svenska.')
if dag == 'söndag':
    print('Sunday')
elif dag == 'måndag':
    print('Monday')
elif dag == 'tisdag':
    print('Tuesday')
elif dag == 'onsdag':
    print('Wednesday')
elif dag == 'torsdag':
    print('Thursday')
elif dag == 'fredag':
    print('Friday')
elif dag == 'lördag':
    print('Saturday')
    
    
    Very good
7.
nummer = int(input('skriv in valfri siffra. '))
summa = 0
while nummer:
    summa += nummer % 10
    nummer //= 10
print(summa)
8.
lista = [1,2,5,10,20,50,100,200,500,1000]
lista.reverse()
pris = 372
pris = round(pris)
start = 1000
skuld = 0
plats = 0
antal = 0
while skuld < pris:
    for i in lista:
        skuld += lista[plats]
        antal += 1
        if skuld > pris:
            skuld -= lista[plats]
            plats += 1
            print(lista[plats])
        elif plats == 9:
            plats = 0
        elif skuld == pris:
            break
print(f'Change: {start-skuld} kr')
print(f'{antal} bills/coins required')
print(start-skuld)
14.
income = int(input('Skriv in värdet som ska skattas '))
if income < 38000:
    taxed = income*0.3
    print(f'skatt: {round(taxed)}')
elif 38000 <= income <= 50000:
    taxed = income*0.3
    income = income - 38000
    income = income * 0.05
    taxed += income
    #0.05
    print(f'skatt: {round(taxed)}')
elif income > 50000:
    taxed = income*0.3
    taxed += 12000 * 0.05
    income = income - 50000
    income = income * 0.1
    taxed += income
    print(f'skatt: {round(taxed)}')
    15.
import math
a = float(input('första talet '))
b = float(input('andra talet '))
c = float(input('sista talet '))
sol = (b**2) - (4*a*c)
try:
    sol1 = (-b-math.sqrt(sol))/(2*a)
    sol2 = (-b+math.sqrt(sol))/(2*a)
    if sol1 != sol2:
        print(f'Det finns två reella lösningar, {sol1},{sol2}')
    elif sol1 == sol2:
        print(f'Det finns en reell lösning, {sol1}')
except ValueError:
        print('Det finns inga reella lösningar.')
#print('The solution are {0} and {1}'.format(sol1,sol2))
#print(sol1,sol2)

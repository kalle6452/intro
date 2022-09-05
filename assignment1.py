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
7.
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
nummer = 12345
summa = 0
while nummer:
    # Lägger till den sista integern i summa.
    summa += nummer % 10
    print(summa)
    # Tar bort den sista integern från number.
    nummer //= 10
    print(nummer)
    #print(number / 10)
print(summa)

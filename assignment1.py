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
2.
x = input('Write a line of text: ')
print('Quote: ' + f'"{x}"')
3.
F = float(input('Skriv in temperatur i fahrenheit '))
x = 9/5
C = (F - 32)/x
print(C)
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
11.
first = input('Write first name.')
second = input('Write second name.')
last = input('Write last name.')
print(f'{first[0]}. {second[0]}. {last[0:-1]}')

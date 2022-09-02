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

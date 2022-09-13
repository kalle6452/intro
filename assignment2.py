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
4.

from random import choice

a = '0123456789'
x = choice(a[1:10])
s = 0
for n in range(3):
    z = ''.join(a.split(x[n]))
    x += choice(z)
print('Загаданное число - ', x)
while True:
    y = input('Введите 4-х значное число: ')
    b = 0
    c = 0
    s += 1
    for n in range(4):
        if x[n] == y[n]:
            b += 1
        elif y[n] in x:
            c += 1
    print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коров')
    if b == 4:  # Если число угадано
        print('Вы победили за '+ str(s) + ' ходов')  # Победа
        break

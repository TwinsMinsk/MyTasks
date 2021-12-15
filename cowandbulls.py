import string
from random import choice

num = '0123456789'
x = choice(num[1:10])#первый символ не включаю, чтобы он не начинался с нуля
step = 0
for n in range(3):
    num = ''.join(num.split(x[n]))
    x += choice(num)
print('Загаданное число - ', x)

while True:
    y = input('Введите 4-х значное число: ')
    if len(y) == 4 and y.isdigit():
        bulls = 0
        cows = 0
        step += 1
        for n in range(4):
            if x[n] == y[n]:
                bulls += 1
            elif y[n] in x:
                cows += 1
        print(f'{y} содержит {bulls} быка и {cows} коров')
        if bulls == 4:  # Если число угадано
            print(f'Вы победили за {step} ходов')  # Победа
            break
    else:
        print("Число введено неверно, попробуйте еще раз...")
        continue

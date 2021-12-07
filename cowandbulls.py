from random import choice

num = '0123456789'
x = choice(num[1:10]) # первый символ не включаю, чтобы он не начинался с нуля
step = 0
for n in range(3):
    num = ''.join(num.split(x[n]))
    x += choice(num)
print('Загаданное число - ', x)
while True:
    y = input('Введите 4-х значное число: ')
    bulls = 0
    cows = 0
    step += 1
    for n in range(4):
        if x[n] == y[n]:
            bulls += 1
        elif y[n] in x:
            cows += 1
    print(y + ' содержит ' + str(bulls) + ' быка и ' + str(cows) + ' коров')
    if bulls == 4:  # Если число угадано
        print('Вы победили за '+ str(step) + ' ходов')  # Победа
        break

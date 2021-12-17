message = input('Введите строку ')
result1 = []

for i in message:
    if i == '#':
        result1.pop(-1)
    else:
        result1.append(i)

print("".join(result1))

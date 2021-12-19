alpha_eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
step = int(input('Шаг шифровки: '))
message = input("Сообщение для шифровки: ").upper()
result = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        place = alpha_ru.find(i)
        new_place = place - step
        if i in alpha_ru:
            result += alpha_ru[new_place]
        else:
            result += i
else:
    for i in message:
        place = alpha_eu.find(i)
        new_place = place - step
        if i in alpha_eu:
            result += alpha_eu[new_place]
        else:
            result += i
print (result.title())




alpha_eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
step = int(input('Шаг шифровки: '))
message = input("Сообщение для ДЕшифровки: ").upper()
result = ''
lang = input('Выберите язык RU/EU: ')
if lang == 'RU':
    for i in message:
        place = alpha_ru.find(i)
        new_place = place + step
        if i in alpha_ru:
            result += alpha_ru[new_place]
        else:
            result += i
else:
    for i in message:
        place = alpha_eu.find(i)
        new_place = place + step
        if i in alpha_eu:
            result += alpha_eu[new_place]
        else:
            result += i
print (result.title())
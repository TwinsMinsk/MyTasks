
message = str(input())
count = 1
x = 1
result = message[x:x + 1]
for i in message:
    if i in result:
        count += 1
    elif count == 1:
        print(i,end='')
    else:
        print(i, end='')
        print(count, end='')
        count = 1
    x += 1
    result = message[x:x + 1]

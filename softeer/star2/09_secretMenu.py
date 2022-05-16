lenSecret, lenButton, maxNum = list(map(int, input().split()))

secretKey = list(map(int, input().split()))
buttons = list(map(int, input().split()))

status = 'normal'
for i in range(len(buttons)):
    if lenSecret > lenButton:
        status = 'normal'
        break

    key = buttons[i:i+lenSecret]
    if key == secretKey:
        status = 'secret'
        break


print(status)
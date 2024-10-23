def evenchecker():
    num = int(input('enter a num:'))
    if (num % 2 == 0):
        print(str(num) + ' is an even number')
    else:
        print((str(num))+ ' is not an even number')

evenchecker()
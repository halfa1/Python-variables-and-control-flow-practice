def simplecalculator():
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the second number:'))
    operation = input('Enter an operator, either(+,-,*,/):')

    if operation == '-':
        print(str(num1) + '-' + str(num2) + '=' + str(num1 - num2))
    elif operation == '+':
        print(str(num1) + '+' + str(num2) + '=' + str(num1 + num2))
    elif operation == '*':
        print(str(num1) + '*' + str(num2) + '=' + str(num1 * num2))
    elif operation == '/':
        print(str(num1) + '/' + str(num2) + '=' + str(num1 / num2))
    else:
        print('You entered an invalid operation')

simplecalculator()
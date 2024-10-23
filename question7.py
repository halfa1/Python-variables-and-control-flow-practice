#A program to check the type of a tringle after user enters the sides length
def triangletypechecker():
    side1=float(input('Enter the length of first side: '))
    side2=float(input('Enter the length of second side: '))
    side3=float(input('Enter the length of third side: '))

    if side1 == side2 == side3:
        print('The triangle is an equilateral triangle')
    elif side1 != side2 and side1 != side3 and side2 != side3:
        print('This is a scalene triangle')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('This is a isosceles triangle.')

triangletypechecker()
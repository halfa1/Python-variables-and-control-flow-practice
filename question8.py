def daynames():
    days = ['Monday', 'Tuesday', 'wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_number = int(input('Enter the day of the week in numbers from 1 to 7: '))
    if day_number > 7 or day_number < 1:
        print('Invalid Input')
    else:
        if day_number == 1:
            print(days[0])
        elif day_number == 2:
            print(days[1])
        elif day_number == 3:
            print(days[2])
        elif day_number == 4:
            print(days[3])
        elif day_number == 5:
            print(days[4])
        elif day_number == 6:
            print(days[5])
        else:
            print(days[6])
daynames()
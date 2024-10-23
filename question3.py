def grades():
    score = float(input('Enter the score in the range (1-100):'))
    if score>=90 and score<=100 :
        print('Your grade is A')
    elif score>=80 and score<=89 :
        print('Your grade is B')
    elif score>=70 and score<=79 :
        print('Your grade is C')
    elif score>=60 and score<=69 :
        print('Your grade is D')
    else :
        print('Your grade is F')

grades()
import random
a = random.randint(0,9)
b=None
while a!=b:
    b=int(input('Guess the number between 0 and 9 im thinking off '))
    if (a==b):
        print('You got it!')
    elif b>a:
        print ('Lower!')
    else: print ('Higher!')

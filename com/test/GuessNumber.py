import random

def guess_number():
    val = random.randint(1,20)
    times = 3
    print(val)
    while times>0:
       num = int(input('Guess  a Number between 1 and 20 : '))
       if num == val:
            print('You are correct')
            break
       elif num > 20:
            print('You guessed higher')
       else:
            print('You guess lesser')
       times -= 1

    print('The End')


guess_number()


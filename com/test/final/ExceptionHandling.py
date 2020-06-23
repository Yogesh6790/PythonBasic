

while True:
    try:
        numerator = int(input('Enter Numerator : '))
        denominator = int(input('Enter denominator : '))
        result = numerator/denominator
    except ZeroDivisionError:
        print('Input is wrong - denominator is 0')
    except ValueError:
        print('Input is wrong - denominator is not int')
    else:
        print(f'result is {result:.2f}')
        break
    finally:
        print("finally executed") # this is always executed

### Example of raise an exception and understanding the function call stack
def function1():
    function2()

def function2():
    raise Exception('Our Exception raised')

function1()
import math
import time
from functools import wraps

def decorator(fnPtr):
    @wraps(fnPtr)
    def timeLogWrapper(*args, **kwds):
        with open('logfile.txt', 'w') as log:
            log.write('Function execution begins\n')

        start_time = time.time()
        i = fnPtr(*args, *kwds)
        end_time = time.time()
        with open('logfile.txt', 'a') as log:
            log.write('Import of file ends\n')
            log.write(f'Time taken for file computing factorial: {end_time-start_time}\n')
            
        return i
    return timeLogWrapper

@decorator
def getFactorial(number):
    '''
     This function is used to get the factorial of a given number
     Parameters
     number - integer
     return type - number - factorial of a number.
     '''
    
    return math.factorial(number)

getFactorial(100000)

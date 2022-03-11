'''
Decorator is an special type of closure.
Is a function that receives as a paramater another function,it add somethings,
but returns a different function.
'''
from datetime import datetime

def execution_time(func): #Looking for the program efficiency
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Elapsed ' + str(time_elapsed.total_seconds()) + ' Seconds')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000000):
        pass

random_func()
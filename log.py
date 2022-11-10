import time

'''
Create a file named log.py and create decorator inside called timestamp
• The decorator should print the current time then afterwards print anything the is being decorated (see
examples below)
Hint: - Use time.ctime()
Examples: Input (in file called test.py):
'''
def timestamp(some_func):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        result = some_func(*args, **kwargs)   
        return result
    return wrapper


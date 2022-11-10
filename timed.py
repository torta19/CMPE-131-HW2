import time
'''Create a file named timed.py and add import time at the top of the file.
• Create a decorator called timeme
• The decorator should print Total time X where X is the amount of time it took to run in seconds.
• Do not keep any test code when you submit your code. We only want the decorator.
Hint:
• Use time.time() to get the current time in seconds.
• You can use the function time.sleep(2) to test your code.'''

def timeme(some_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = some_func(*args, **kwargs)
        final_time = time.time()
        print (f'Total time {final_time - start_time:.3f} seconds')
        return result
    return wrapper

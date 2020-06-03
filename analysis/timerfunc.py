# a wrapper function that measures time and memory usage will let us try a few different ways to load the data 
# and select the fastest way to lad the info

import time
from functools import wraps
from memory_profiler import memory_usage

def profile(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        #fn_kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        # if you want to print the function name and kwargs - print(f'\n{fn.__name__}({fn_kwargs_str})')

        # Measure time and memory
        # set time start
        t = time.perf_counter()
        
        # execute function and capture memory usage
        mem, retval = memory_usage((fn, args, kwargs), retval=True, interval=1e-7) #timeout=200
        elapsed = time.perf_counter() - t

        # print results of time and memory
        print(f'Time   {elapsed:0.4}')
        print(f'Memory {max(mem) - min(mem)}')

        # return function output
        return retval

    # return inner function
    return inner
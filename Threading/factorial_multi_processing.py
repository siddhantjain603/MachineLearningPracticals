import multiprocessing
import sys
import math
import time

sys.set_int_max_str_digits(1000000)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    return result

if __name__=="__main__":
    
    numbers = [30000,40000,50000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)
    
    for result in results:
        print(f"Result:{result}")
        print()
    
    exc_time = time.time() - start_time
    print(exc_time)

from concurrent.futures import ProcessPoolExecutor
import time

def print_square(number):
    time.sleep(3)
    return f"Sqaure : {number**2}"

numbers = [1,2,3,4,5,6,7,8,9,10,11]

if __name__=="__main__":

    t = time.time()
    with ProcessPoolExecutor(max_workers=9) as executor:
        results = executor.map(print_square,numbers)
    
    for result in results:
        print(result)
    
    exc_time = time.time()-t
    print(f"Execution time: {exc_time}")


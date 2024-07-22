import multiprocessing
import time


def print_square():

    for i in range(5):
        time.sleep(1)
        print(f"Square is : {i*i}")

def print_cube():

    for i in range(5):
        time.sleep(1.5)
        print(f"Cube is : {i*i*i}")

if __name__=="__main__":

    t = time.time()
    p1 = multiprocessing.Process(target=print_square)
    p2 = multiprocessing.Process(target=print_cube)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    exc_time = time.time() - t
    print(f"Execution time: {exc_time}")
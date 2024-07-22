import threading
import time


def print_numbers():

    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")


def print_letters():

    for i in "abcde":
        time.sleep(2)
        print(f"Letter : {i}")


# t = time.time()
# print_numbers()
# print_letters()

# finished_time = time.time() - t

# print(f"Total execution time: {finished_time}")


#Using threads
t = time.time()

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

#Start thw threaqds
t1.start()
t2.start()

#Waiting for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t

print(f"Total execution time: {finished_time}")
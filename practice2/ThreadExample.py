from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Hello")


class Hi(Thread):
    def run(self):
        for i in range(10):
            sleep(1)
            print("Hi")


T1 = Hello()
T2 = Hi()

T1.start()
sleep(0.2)
T2.start()


"""
Once the threads start, the current program (you can think of it like a main thread) also keeps on executing. 
In order to stop execution of current program until a thread is complete, we use join method.
As a result, the current program will first wait for the completion of t1 and then t2. Once, they are finished, 
the remaining statements of current program are executed.
"""

# wait until thread 1 is completely executed
T1.join()
# wait until thread 2 is completely executed
T2.join()

# both threads completely executed
print("Done!")

print("Thread name ", current_thread().name)    # It will Print Name of current Thread

"""
To create a new thread, we create an object of Thread class. It takes following arguments:
target: the function to be executed by thread
args: the arguments to be passed to the target function
In above example, we created 2 threads with different target functions:

t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))

"""


def print_cube(num):
    for i in range(num):
        sleep(1)
        print("print_cube Method")


def print_square(num):
    for i in range(num):
        sleep(1)
        print("print_square Method")


t1 = Thread(target=print_square, args=(10,), name="T1")
t2 = Thread(target=print_cube, args=(10,), name="T2")

# starting thread 1
t1.start()
sleep(0.2)
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()


print("Done!")


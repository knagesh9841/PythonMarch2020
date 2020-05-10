import threading
from time import sleep

"""
threading module provides a Lock class to deal with the race conditions

Lock class provides following methods:

acquire([blocking]) : To acquire a lock. A lock can be blocking or non-blocking.
When invoked with the blocking argument set to True (the default), thread execution is blocked until the lock is 
unlocked, then lock is set to locked and return True.
When invoked with the blocking argument set to False, thread execution is not blocked. 
If lock is unlocked, then set it to locked and return True else return False immediately.
release() : To release a lock.
When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.
If lock is already unlocked, a ThreadError is raised.

"""


class ThreadSync(threading.Thread):
    def __init__(self):
        super(ThreadSync, self).__init__()
        self.lock = threading.Lock()

    def run(self):
        for i in range(10):
            self.lock.acquire(blocking=True)
            print("Hello "+threading.current_thread().name, i)
            self.lock.release()


T1 = ThreadSync()
T2 = ThreadSync()

T1.setName("Hello")     # set thread name
T2.setName("Hi")

print(T1.getName())     # get Thread Name
print(T2.getName())

T1.start()
sleep(0.2)
T2.start()

T1.join()
T2.join()

print("Done")




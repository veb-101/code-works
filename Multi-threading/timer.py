#!usr/bin/python3

import threading
import time

tLock = threading.Lock()


def timer(name, delay, repeat):
    print("{} started.".format(name))
    tLock.acquire()
    print("{} has acquired the lock".format(name))
    while repeat > 0:
        time.sleep(delay)
        print("{0}: arrived at{1}".format((name), (time.ctime(time.time()))))
        repeat -= 1
    print("{} is releasing the lock".format(name))
    tLock.release()
    print("{} is complete.".format(name))


def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()
    print("Main completed.")


if __name__ == "__main__":
    Main()

#!usr/bin/python3


import threading
import time


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(2)
        print("Finished background File Write to " + self.out)


def Main():
    message = input("Enter a String to store:")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("The program can coninue while it writes another thread")
    print("100 + 400 = ", 100 + 400)
    background.join()
    print("Waited until thrad was complet")


if __name__ == "__main__":
    Main()

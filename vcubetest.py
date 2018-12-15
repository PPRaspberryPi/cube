import threading
import vCubeAPI as api
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        i = 0
        while True:
            time.sleep(2)
            api.led_on([i % 7, i % 7, i % 7])
            i += 1
            eingabe = input("Nummer[x,y,z]: ")
            api.led_on(eingabe)


# Create new threads
thread1 = MyThread()

# Start new Threads
thread1.start()
api.start()

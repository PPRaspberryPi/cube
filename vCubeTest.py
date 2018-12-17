import threading
import vCubeAPI as api
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        i = 0
        while True:
            time.sleep(0.5)
            api.led_on([i, i, i])
            i += 1


# Create new threads
thread1 = MyThread()

# Start new Threads
thread1.start()
api.start()

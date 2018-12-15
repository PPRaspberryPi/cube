#!/usr/bin/python

import threading
import vCubeAPI as api
import time


class myThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        i = 1
        while True:
            time.sleep(5)
            api.led_on([i, i, i])
            i += 1


# Create new threads
thread1 = myThread()

# Start new Threads
thread1.start()
api.start()

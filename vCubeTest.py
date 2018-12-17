import threading
import vCubeAPI as api
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        z = 0
        while z < 8:
            y = 0
            while y < 8:
                x = 0
                while x < 8:
                    time.sleep(0.014)
                    api.led_on([z, y, x])
                    x += 1
                time.sleep(0.014)
                api.led_on([z, y, x])
                y += 1
            time.sleep(0.014)
            api.led_on([z, y, x])
            z += 1


# Create new threads
thread1 = MyThread()

# Start new Threads
thread1.start()
api.start()

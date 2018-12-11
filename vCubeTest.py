import threading
import vCubeAPI as api


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        while True:
            eingabe = input("Nummer[x,y,z]: ")
            api.led_on(eingabe)


# Create new threads
thread1 = MyThread()

# Start new Threads
thread1.start()
api.start()

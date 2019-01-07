import sys
import Snake


if any("Snake" in arr for arr in sys.argv):
    Snake.thread1 = Snake.MyThread()

    Snake.thread1.start()
    Snake.api.start()

elif any("Pong" in arr for arr in sys.argv):
    print("test")

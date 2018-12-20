import threading
import Direction
import vCubeAPI as api
import time


class MyThread(threading.Thread):
    snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
    snake_length = 3

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            direction = Direction.direction
            latest_loc = self.snake_loc[self.snake_length - 1]
            for x in range(1, self.snake_length):
                self.snake_loc[self.snake_length - x] = self.snake_loc[self.snake_length - x - 1]
            if direction == Direction.Direction.UP:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] + 1, y[2]]
            elif direction == Direction.Direction.DOWN:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] - 1, y[2]]
            elif direction == Direction.Direction.RIGHT:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] + 1]
            elif direction == Direction.Direction.LEFT:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] - 1]
            elif direction == Direction.Direction.BACK:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] + 1, y[1], y[2]]
            elif direction == Direction.Direction.FORTH:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] - 1, y[1], y[2]]
            for s in self.snake_loc:
                api.led_on(s)

            api.led_off(latest_loc)
            time.sleep(0.2)


# Create new threads
thread1 = MyThread()

# Start new Threads
thread1.start()
api.start()

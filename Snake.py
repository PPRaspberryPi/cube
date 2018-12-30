import threading
import Direction
import vCubeAPI as api
import time
import random


class MyThread(threading.Thread):
    snake_loc = [[0, 2, 0], [0, 1, 0], [0, 0, 0]]
    direction = Direction.Direction.UP
    snake_length = 3
    pickup_loc = [0, 7, 1]
    failed = False

    def __init__(self):
        super().__init__()

    def run(self):
        while not self.failed:
            self.direction = Direction.direction
            if self.snake_length > len(self.snake_loc):
                self.snake_loc.append(self.snake_loc[len(self.snake_loc) - 1])
                self.snake_length = len(self.snake_loc)

            api.led_off(self.snake_loc[self.snake_length - 1])
            for x in range(1, self.snake_length):
                self.snake_loc[self.snake_length - x] = self.snake_loc[self.snake_length - x - 1]
            if self.direction == Direction.Direction.UP:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] + 1, y[2]]
            elif self.direction == Direction.Direction.DOWN:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1] - 1, y[2]]
            elif self.direction == Direction.Direction.RIGHT:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] + 1]
            elif self.direction == Direction.Direction.LEFT:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0], y[1], y[2] - 1]
            elif self.direction == Direction.Direction.BACK:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] + 1, y[1], y[2]]
            elif self.direction == Direction.Direction.FORTH:
                y = self.snake_loc[0]
                self.snake_loc[0] = [y[0] - 1, y[1], y[2]]
            for s in self.snake_loc:
                api.led_on(s)

            api.led_on(self.pickup_loc)

            if self.snake_loc[0] in self.snake_loc[1:]:
                self.failed = True

            if self.snake_loc[0][0] % 8 == self.pickup_loc[0] and self.snake_loc[0][1] % 8 == self.pickup_loc[1] and \
                    self.snake_loc[0][2] % 8 == self.pickup_loc[2]:
                self.snake_length += 1
                found_spawn = False
                while not found_spawn:
                    self.pickup_loc = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)]
                    if self.pickup_loc not in self.snake_loc:
                        found_spawn = True
            time.sleep(0.2)


if __name__ == "__main__":
    # Create new threads
    thread1 = MyThread()

    # Start new Threads
    thread1.start()
    api.start()

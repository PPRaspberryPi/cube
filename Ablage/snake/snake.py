from enum import Enum
from threading import Thread
import time
import keyboard


class Color(Enum):
    BLACK = 1
    WHITE = 2


class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Tile:
    pos_x = 0
    pos_y = 0
    color = Color.WHITE

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self):
        pass

    def change_color(self, color: Color):
        self.color = color
        self.draw()


class GameTicks(Thread):
    snake = None

    def __init__(self, tick_speed, snake):
        pass

        Thread.__init__(self)
        self.tick_speed = tick_speed
        self.snake = snake

    def run(self):
        while True:
            # draw etc.
            print(self.snake.current_direction)  # testing
            time.sleep(self.tick_speed)


class KeyCheck(Thread):
    snake = None

    def __init__(self, snake):
        pass

        Thread.__init__(self)
        self.snake = snake

    def run(self):
        while True:
            try:
                if keyboard.is_pressed('w'):
                    self.snake.change_direction(Direction.UP)
                elif keyboard.is_pressed('a'):
                    self.snake.change_direction(Direction.LEFT)
                elif keyboard.is_pressed('s'):
                    self.snake.change_direction(Direction.DOWN)
                elif keyboard.is_pressed('d'):
                    self.snake.change_direction(Direction.RIGHT)
            except:
                break


class Snake:
    current_direction = Direction.UP
    s_length: int = 1
    current_pos = (0, 0)

    def __init__(self, starting_pos_x, starting_pos_y, tiles):
        tiles[starting_pos_x * starting_pos_y].change_color(Color.BLACK)
        self.current_pos = (starting_pos_x, starting_pos_y)

    def change_direction(self, direction: Direction):
        self.current_direction = direction

    def move(self):
        if self.current_direction == Direction.UP:
            if self.current_pos[1] == 0:
                return False
            else:
                self.current_pos = (self.current_pos[0], self.current_pos[1] - 1)
                return True
        elif self.current_direction == Direction.LEFT:
            if self.current_pos[0] == 0:
                return False
            else:
                self.current_pos = (self.current_pos[0] - 1, self.current_pos[1])
                return True
        elif self.current_direction == Direction.DOWN:
            if self.current_pos[1] == sy - 1:
                return False
            else:
                self.current_pos = (self.current_pos[0], self.current_pos[1] + 1)
                return True
        elif self.current_direction == Direction.RIGHT:
            if self.current_pos[0] == sx - 1:
                return False
            else:
                self.current_pos = (self.current_pos[0] + 1, self.current_pos[1])
                return True


def main(tick_speed):
    tiles = [Tile(n, m) for n in range(0, sx) for m in range(0, sy)]
    snake = Snake(sx // 2, sy - 1, tiles)
    for tile in tiles:
        print(tile.pos_x, " ", tile.pos_y)  # just for testing purpose
        tile.draw()  # initial ...

    game_ticks = GameTicks(tick_speed, snake)
    game_ticks.start()

    key_check = KeyCheck(snake)
    key_check.start()


sx, sy = 5, 5
main(0.5)

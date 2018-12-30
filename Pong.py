import threading
import vCubeAPI as api
import time
import random


class MyThread(threading.Thread):
    player_loc = [[2, 0, 2], [3, 0, 2], [2, 0, 3], [3, 0, 3]]
    ball_loc = [3, 1, 2]
    ball_vel_x = 1
    ball_vel_y = 1
    ball_vel_z = 1

    failed = False

    def __init__(self):
        super().__init__()

    def move_player(self):
        pass

    def run(self):
        while not self.failed:
            # Turn off last position
            api.led_off(self.ball_loc)

            # Ball moving
            self.ball_loc[0] += self.ball_vel_x
            self.ball_loc[1] += self.ball_vel_y
            self.ball_loc[2] += self.ball_vel_z

            # Ball bouncing on walls
            if self.ball_loc[0] > 6 or self.ball_loc[0] < 1:
                self.ball_vel_x *= -1
            if self.ball_loc[1] > 6 or self.ball_loc[1] < 1:
                self.ball_vel_y *= -1
            if self.ball_loc[2] > 6 or self.ball_loc[2] < 1:
                self.ball_vel_z *= -1

            # If Ball hits the ground
            # TODO: NOT WORKING AS INTENDED
            if self.ball_loc[1] == 0 and \
                    (self.player_loc[0][0] != self.ball_loc[1] or self.player_loc[0][2] != self.ball_loc[1] or
                     self.player_loc[1][0] != self.ball_loc[1] or self.player_loc[1][2] != self.ball_loc[1] or
                     self.player_loc[2][0] != self.ball_loc[1] or self.player_loc[2][2] != self.ball_loc[1] or
                     self.player_loc[3][0] != self.ball_loc[1] or self.player_loc[3][2] != self.ball_loc[1]):
                self.failed = True

            print(self.ball_loc[1])

            # Turn on new position
            api.led_on(self.ball_loc)
            for s in self.player_loc:
                api.led_on(s)

            time.sleep(1)


if __name__ == "__main__":
    # Create new threads
    thread1 = MyThread()

    # Start new Threads
    thread1.start()
    api.start()

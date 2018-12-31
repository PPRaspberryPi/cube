import threading
import vCubeAPI as api
import time


class MyThread(threading.Thread):
    player_loc = [[2, 0, 1], [3, 0, 1], [2, 0, 2], [3, 0, 2]]
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
            if self.ball_loc[1] == 0 and not any(loc in [self.ball_loc] for loc in self.player_loc):
                self.failed = True

            # If Ball hits the paddle bounce off of it and do not go into the paddle
            if self.ball_loc[1] == 0 and any(loc in [self.ball_loc] for loc in self.player_loc):
                self.ball_loc[1] = 1

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

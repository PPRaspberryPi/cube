import threading
import vCubeAPI as api
import Direction
import time


class MyThread(threading.Thread):
    player1_loc = [[0, 2, 0], [1, 2, 0], [0, 3, 0], [1, 3, 0]]  # Left Side P1
    player2_loc = [[0, 2, 7], [1, 2, 7], [0, 3, 7], [1, 3, 7]]  # Right Side P2
    ball_loc = [3, 1, 2]
    ball_vel_x = 1
    ball_vel_y = 1
    ball_vel_z = 1
    failed = False
    player1_action = None
    player2_action = None

    player1_score = 0
    player2_score = 0

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

            # TODO: UGLY AF. WE SHOULD FIX THAT. IT ONLY UPDATES PLAYER EACH INTERVAL
            # Player moving
            self.player1_action = Direction.direction
            if self.player1_action is not None:
                if self.player1_action == Direction.Direction.UP:
                    for s in self.player1_loc:
                        api.led_off(s)
                    self.player1_loc[0][0] += 1
                    self.player1_loc[1][0] += 1
                    self.player1_loc[2][0] += 1
                    self.player1_loc[3][0] += 1
                    for s in self.player1_loc:
                        api.led_on(s)
                if self.player1_action == Direction.Direction.DOWN:
                    for s in self.player1_loc:
                        api.led_off(s)
                    self.player1_loc[0][0] -= 1
                    self.player1_loc[1][0] -= 1
                    self.player1_loc[2][0] -= 1
                    self.player1_loc[3][0] -= 1
                    for s in self.player1_loc:
                        api.led_on(s)
                if self.player1_action == Direction.Direction.RIGHT:
                    for s in self.player1_loc:
                        api.led_off(s)
                    self.player1_loc[0][2] += 1
                    self.player1_loc[1][2] += 1
                    self.player1_loc[2][2] += 1
                    self.player1_loc[3][2] += 1
                    for s in self.player1_loc:
                        api.led_on(s)
                if self.player1_action == Direction.Direction.LEFT:
                    for s in self.player1_loc:
                        api.led_off(s)
                    self.player1_loc[0][2] -= 1
                    self.player1_loc[1][2] -= 1
                    self.player1_loc[2][2] -= 1
                    self.player1_loc[3][2] -= 1
                    for s in self.player1_loc:
                        api.led_on(s)
                Direction.direction = None

            # Ball bouncing on walls
            if self.ball_loc[0] > 6 or self.ball_loc[0] < 1:
                self.ball_vel_x *= -1
            if self.ball_loc[1] > 6 or self.ball_loc[1] < 1:
                self.ball_vel_y *= -1
            if self.ball_loc[2] > 6 or self.ball_loc[2] < 1:
                self.ball_vel_z *= -1

            # If Ball hits player1 wall
            if self.ball_loc[0] == 0 and not any(loc in [self.ball_loc] for loc in self.player1_loc):
                self.player2_score += 1
                #self.failed = True

            # If Ball hits player1 wall
            if self.ball_loc[0] == 7 and not any(loc in [self.ball_loc] for loc in self.player2_loc):
                self.player1_score += 1
                #self.failed = True

            # If Ball hits the paddle bounce off of it and do not go into the paddle P1
            if self.ball_loc[0] == 0 and any(loc in [self.ball_loc] for loc in self.player1_loc):
                self.ball_loc[0] = 1

            # If Ball hits the paddle bounce off of it and do not go into the paddle P2
            if self.ball_loc[0] == 7 and any(loc in [self.ball_loc] for loc in self.player2_loc):
                self.ball_loc[0] = 6

            # Turn on new position
            api.led_on(self.ball_loc)
            for s in self.player1_loc:
                api.led_on(s)

            for s in self.player2_loc:
                api.led_on(s)

            time.sleep(0.22)


if __name__ == "__main__":
    # Create new threads
    thread1 = MyThread()

    # Start new Threads
    thread1.start()
    api.start()

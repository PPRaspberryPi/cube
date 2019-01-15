import threading
import time
import Direction
import vCubeAPI as api
import Animations
import Game


class Pong(Game.CubeGame, threading.Thread):
    _name = 'Pong'
    _version = 'v0.1'

    _menu_frame = [0, 0, 0, 1, 0, 0, 0, 0,
                   0, 0, 1, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0, 0, 0,
                   1, 0, 0, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 1, 0, 0,
                   0, 0, 1, 0, 1, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0, 0,
                   0, 0, 1, 1, 1, 0, 0, 0]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)
        self.player_loc = [[2, 0, 1], [3, 0, 1], [2, 0, 2], [3, 0, 2]]
        self.ball_loc = [3, 1, 2]
        self.ball_vel_x = 1
        self.ball_vel_y = 1
        self.ball_vel_z = 1
        self.failed = False
        self.player_action = None

        self.p_loc = [0.5, 0.5]

        self.mov_val = (1 / (self.cube_size - 1))

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        an = Animations.TickerAnimation("pong")
        an.start()
        an.join()

    def done(self):
        pass

    def run(self):
        while not self.failed:
            # Turn off last position
            api.led_off(self.ball_loc)

            # Ball moving
            """
            self.ball_loc[0] += self.ball_vel_x
            self.ball_loc[1] += self.ball_vel_y
            self.ball_loc[2] += self.ball_vel_z
            """

            # Player moving
            self.player_action = Direction.direction
            if self.player_action is not None:
                if self.player_action == Direction.Direction.UP:

                    api.pad_led_off(self.p_loc)

                    if self.p_loc[0] + self.mov_val <= 1:
                        self.p_loc[0] += self.mov_val
                    else:
                        self.p_loc[0] = 0.99

                    api.pad_led_on(self.p_loc)

                if self.player_action == Direction.Direction.DOWN:
                    api.pad_led_off(self.p_loc)

                    if self.p_loc[0] - self.mov_val >= 0:
                        self.p_loc[0] -= self.mov_val
                    else:
                        self.p_loc[0] = 0.01

                    api.pad_led_on(self.p_loc)
                if self.player_action == Direction.Direction.RIGHT:
                    api.pad_led_off(self.p_loc)

                    if self.p_loc[1] + self.mov_val <= 1:
                        self.p_loc[1] += self.mov_val
                    else:
                        self.p_loc[1] = 0.99

                    api.pad_led_on(self.p_loc)
                if self.player_action == Direction.Direction.LEFT:
                    api.pad_led_off(self.p_loc)

                    if self.p_loc[1] - self.mov_val >= 0:
                        self.p_loc[1] -= self.mov_val
                    else:
                        self.p_loc[1] = 0.01

                    api.pad_led_on(self.p_loc)
                Direction.direction = None

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

                # Timer for cooldown
                for x in range(0, 8):
                    api.led_on([0, x, 0], [7, x, 0], [0, x, 7], [7, x, 7])
                    api.display()
                    time.sleep(1)

            # If Ball hits the paddle bounce off of it and do not go into the paddle
            if self.ball_loc[1] == 0 and any(loc in [self.ball_loc] for loc in self.player_loc):
                self.ball_loc[1] = 1

            # Turn on new position
            api.led_on(self.ball_loc)
            api.pad_led_on(self.p_loc)

            api.display()

            time.sleep(0.22)

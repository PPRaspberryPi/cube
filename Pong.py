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

        self.an = None

        self.b_loc = [0.250, 0.5, 0.250]
        self.b_size = 1
        self.b_radius = (self.b_size / self.cube_size) / 2
        self.ball_vel_x = 0.125
        self.ball_vel_y = 0.125
        self.ball_vel_z = 0.125
        self.failed = False
        self.player_action = None

        self.p_loc = [0.5, 0, 0.5]
        self.p_size = 2
        self.p_radius = (self.p_size / self.cube_size) / 2

        self.mov_val = (1 / (self.cube_size - 1))

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        self.an = Animations.TickerAnimation("pong")
        self.an.start()

    def close_animation(self):
        self.an.stop()

    def stopped_animation(self):
        return self.an.stopped()

    def is_animation_alive(self):
        return self.an.is_alive()

    def done(self):
        for x in range(0, 8):
            api.led_on([0, x, 0], [7, x, 0], [0, x, 7], [7, x, 7])
            api.display()
            time.sleep(1)

    def run(self):
        counter = 0
        while not self.failed:
            # Turn off last position
            # api.led_off(self.ball_loc)

            # Ball moving
            """
            self.ball_loc[0] += self.ball_vel_x
            self.ball_loc[1] += self.ball_vel_y
            self.ball_loc[2] += self.ball_vel_z
            """

            api.ball_off(self.b_loc)

            if counter == 7:
                self.b_loc[0] += self.ball_vel_x
                self.b_loc[1] += self.ball_vel_y
                self.b_loc[2] += self.ball_vel_z

                if self.b_loc[0] - self.b_radius < 0 or self.b_loc[0] + self.b_radius > 1:
                    self.ball_vel_x *= -1

                if self.b_loc[1] - self.b_radius < 0 or self.b_loc[1] + self.b_radius > 1:
                    self.ball_vel_y *= -1

                if self.b_loc[2] - self.b_radius < 0 or self.b_loc[2] + self.b_radius > 1:
                    self.ball_vel_z *= -1

                if self.b_loc[1] - self.b_radius < 1 / self.cube_size:
                    if ((self.p_loc[0] + self.p_radius > self.b_loc[0] > self.p_loc[0] - self.p_radius) and (
                            self.p_loc[2] + self.p_radius > self.b_loc[2] > self.p_loc[2] - self.p_radius)):
                        self.ball_vel_y *= -1

                if self.b_loc[1] - self.b_radius < 0:
                    if not ((self.p_loc[0] + self.p_radius > self.b_loc[0] > self.p_loc[0] - self.p_radius) and (
                            self.p_loc[2] + self.p_radius > self.b_loc[2] > self.p_loc[2] - self.p_radius)):
                        self.failed = True

                        self.done()

            # Player moving
            self.player_action = Direction.direction
            if self.player_action is not None:
                if self.player_action == Direction.Direction.UP:

                    api.cuboid_off(self.p_loc, self.p_size, 1, self.p_size)

                    if self.p_loc[0] + self.mov_val <= 1:
                        self.p_loc[0] += self.mov_val
                    else:
                        self.p_loc[0] = 0.99

                    api.cuboid_on(self.p_loc, self.p_size, 1, self.p_size)
                if self.player_action == Direction.Direction.DOWN:
                    api.cuboid_off(self.p_loc, self.p_size, 1, self.p_size)

                    if self.p_loc[0] - self.mov_val >= 0:
                        self.p_loc[0] -= self.mov_val
                    else:
                        self.p_loc[0] = 0.01

                    api.cuboid_on(self.p_loc, self.p_size, 1, self.p_size)
                if self.player_action == Direction.Direction.RIGHT:
                    api.cuboid_off(self.p_loc, self.p_size, 1, self.p_size)

                    if self.p_loc[2] + self.mov_val <= 1:
                        self.p_loc[2] += self.mov_val
                    else:
                        self.p_loc[2] = 0.99

                    api.cuboid_on(self.p_loc, self.p_size, 1, self.p_size)
                if self.player_action == Direction.Direction.LEFT:
                    api.cuboid_off(self.p_loc, self.p_size, 1, self.p_size)

                    if self.p_loc[2] - self.mov_val >= 0:
                        self.p_loc[2] -= self.mov_val
                    else:
                        self.p_loc[2] = 0.01

                    api.cuboid_on(self.p_loc, self.p_size, 1, self.p_size)
                Direction.direction = None



            # Turn on new position
            # api.led_on(self.ball_loc)
            api.ball_on(self.b_loc)
            api.cuboid_on(self.p_loc, self.p_size, 1, self.p_size)

            api.display()

            counter = (counter + 1) % 8

            print(counter)

            time.sleep(0.1)

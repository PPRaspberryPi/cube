import threading
import time

import Animations
import Direction
import FrameCollection2D as Frames
import Game
import vCubeAPI as api


class PongMulti(Game.CubeGame, threading.Thread):
    _name = 'PongMultiplayer'
    _version = 'v0.2'

    _menu_frame = [0, 1, 0, 0, 0, 1, 0, 0,
                   0, 0, 1, 0, 1, 0, 0, 0,
                   1, 0, 0, 1, 0, 0, 0, 0,
                   1, 0, 1, 0, 1, 0, 0, 0,
                   1, 1, 0, 0, 0, 1, 0, 1,
                   0, 0, 1, 0, 0, 0, 1, 1,
                   0, 0, 0, 1, 0, 1, 0, 1,
                   0, 0, 0, 0, 1, 0, 0, 0]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)

        self.an = None


        # Ball
        self.ball_size = 1
        self.ball_loc = [0.250, 0.5, 0.250]
        self.ball_radius = (self.ball_size / self.cube_size) / 2
        self.ball_vel_x = 0.125
        self.ball_vel_y = 0.125
        self.ball_vel_z = 0.125

        # Player1
        self.player1_loc = [0.5, 0.5, 0]  # Left Side P1
        self.player1_size = 2
        self.player1_radius = (self.player1_size / self.cube_size) / 2
        self.player1_action = None
        self.player1_score = 0

        # Player2
        self.player2_loc = [0.5, 0.5, 1]  # Right Side P2
        self.player2_size = 2
        self.player2_radius = (self.player2_size / self.cube_size) / 2
        self.player2_action = None
        self.player2_score = 0

        self.failed = False

        self.mov_val = (1 / (self.cube_size - 1))

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        self.an = Animations.TickerAnimation("pongmulti")
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

            api.cuboid_off(self.ball_loc, self.ball_size, self.ball_size, self.ball_size)

            if counter == 7:
                # Ball moving
                self.ball_loc[0] += self.ball_vel_x
                self.ball_loc[1] += self.ball_vel_y
                self.ball_loc[2] += self.ball_vel_z

                changed = False

                # Ball turning on wall impact
                if self.ball_loc[0] - self.ball_radius < 0 or self.ball_loc[0] + self.ball_radius > 1:
                    self.ball_vel_x *= -1
                    changed = True

                if self.ball_loc[1] - self.ball_radius < 0 or self.ball_loc[1] + self.ball_radius > 1:
                    self.ball_vel_y *= -1
                    changed = True

                if self.ball_loc[2] - self.ball_radius < 0 or self.ball_loc[2] + self.ball_radius > 1:
                    self.ball_vel_z *= -1
                    changed = True

                if self.ball_loc[2] - self.ball_radius < 1 / self.cube_size and not changed:
                    if ((self.player1_loc[1] + self.player1_radius * 2 > self.ball_loc[1] > self.player1_loc[
                            1] - self.player1_radius * 2) and (
                                self.player1_loc[0] + self.player1_radius * 2 > self.ball_loc[0] > self.player1_loc[
                            0] - self.player1_radius * 2)):
                        self.ball_vel_z *= -1

                if self.ball_loc[2] + self.ball_radius > 1 - (1 / self.cube_size) and not changed:
                    if ((self.player2_loc[1] + self.player2_radius * 2 > self.ball_loc[1] > self.player2_loc[
                            1] - self.player2_radius * 2) and (
                                self.player2_loc[0] + self.player2_radius * 2 > self.ball_loc[0] > self.player2_loc[
                            0] - self.player2_radius * 2)):
                        self.ball_vel_z *= -1

            # Player moving
            self.player1_action = Direction.direction

            if self.player1_action is not None:
                if self.player1_action == Direction.Direction.UP:
                    api.cuboid_off(self.player1_loc, self.player1_size, self.player1_size, 1)

                    if self.player1_loc[1] + self.mov_val <= 1:
                        self.player1_loc[1] += self.mov_val
                    else:
                        self.player1_loc[1] = 0.99

                    api.cuboid_on(self.player1_loc, self.player1_size, self.player1_size, 1)

                if self.player1_action == Direction.Direction.DOWN:
                    api.cuboid_off(self.player1_loc, self.player1_size, self.player1_size, 1)

                    if self.player1_loc[1] - self.mov_val >= 0:
                        self.player1_loc[1] -= self.mov_val
                    else:
                        self.player1_loc[1] = 0.01

                    api.cuboid_on(self.player1_loc, self.player1_size, self.player1_size, 1)

                if self.player1_action == Direction.Direction.LEFT:
                    api.cuboid_off(self.player1_loc, self.player1_size, self.player1_size, 1)

                    if self.player1_loc[0] + self.mov_val <= 1:
                        self.player1_loc[0] += self.mov_val
                    else:
                        self.player1_loc[0] = 0.99

                    api.cuboid_on(self.player1_loc, self.player1_size, self.player1_size, 1)

                if self.player1_action == Direction.Direction.RIGHT:
                    api.cuboid_off(self.player1_loc, self.player1_size, self.player1_size, 1)

                    if self.player1_loc[0] - self.mov_val >= 0:
                        self.player1_loc[0] -= self.mov_val
                    else:
                        self.player1_loc[0] = 0.01

                    api.cuboid_on(self.player1_loc, self.player1_size, self.player1_size, 1)

                Direction.direction = None



            if self.player1_score == 8 or self.player2_score == 8:
                self.failed = True
                api.change_face(api.Face.LEFT, 0, Frames.number_to_frame(int(self.player1_score)))
                api.change_face(api.Face.RIGHT, 0, Frames.number_to_frame(int(self.player2_score)))

                self.done()

            # Turn on new position
            # api.led_on(self.ball_loc)
            api.cuboid_on(self.ball_loc, self.ball_size, self.ball_size, self.ball_size)
            api.cuboid_on(self.player1_loc, self.player1_size, self.player2_size, 1)
            api.cuboid_on(self.player2_loc, self.player2_size, self.player2_size, 1)

            api.display()

            counter = (counter + 1) % 8

            time.sleep(0.1)

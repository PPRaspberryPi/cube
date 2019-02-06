import threading
import time

import Direction
import api
import requests
import Animations
import Game


class Weather(Game.CubeGame, threading.Thread):
    _name = 'Weather'
    _version = 'v0.1'

    _menu_frame = [0, 0, 1, 1, 0, 0, 0, 0,
                   0, 0, 1, 1, 1, 1, 0, 0,
                   0, 1, 1, 1, 1, 1, 1, 0,
                   0, 0, 0, 0, 1, 0, 0, 0,
                   0, 0, 1, 0, 1, 0, 0, 0,
                   0, 0, 1, 1, 0, 0, 0, 0,
                   0, 0, 0, 1, 0, 1, 0, 0,
                   0, 0, 0, 0, 0, 1, 0, 0]

    def __init__(self, cube_size, frame_size):
        Game.CubeGame.__init__(self, cube_size, frame_size, self._name)
        threading.Thread.__init__(self)

        self.an = None

        self.failed = False

        self.url = "http://api.openweathermap.org/data/2.5/weather?id=2934691&units=metric&appid" \
                   "=ec6a8c233a22cc97020c5f60c46fb90f"

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        self.an = Animations.TickerAnimation("weather")
        self.an.start()

    def close_animation(self):
        self.an.stop()

    def stopped_animation(self):
        return self.an.stopped()

    def is_animation_alive(self):
        return self.an.is_alive()

    def done(self):
        pass

    def run(self):
        weather_data = requests.get(self.url).json()
        weather = weather_data["weather"][0]["main"]
        print(weather)
        # 2xx Thunderstorm
        # 3xx Drizzle
        # 5xx Rain
        # 6xx Snow
        # 7xx Atmosphere (Fog)
        # 800 Clear
        # 80x Clouds

        Direction.direction_p_1.value = 0
        if weather == Thunderstorm:
            anim = Animations.Rain(1, self.cube_size, 1)
        elif weather == Drizzle:
            anim = Animations.Rain(0.2, self.cube_size, 1)
        elif weather == Rain:
            anim = Animations.Rain(0.5, self.cube_size, 1)
        elif weather == Snow:
            anim = Animations.Snow(0.7, self.cube_size, 1)
        elif weather == Fog:
            anim = Animations.Fog(0.5, self.cube_size, 1)
        elif weather == Clear:
            anim = Animations.Sun()
        elif weather == Clouds:
            anim = Animations.Clouds(1, self.cube_size, 1)
        anim.start()
        anim.join()
        Direction.direction_p_1.value = 0

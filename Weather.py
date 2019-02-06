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
        rain = Animations.Rain(1, self.cube_size, 1)
        rain.start()
        rain.join()


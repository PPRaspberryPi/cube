import threading
import time

import Direction
import vCubeAPI as api
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
        self.failed = False

        self.url = "http://api.openweathermap.org/data/2.5/weather?q=Duisburg&appid=ec6a8c233a22cc97020c5f60c46fb90f"

    def get_menu_frame(self):
        return self._menu_frame

    def has_menu_animation(self):
        return True

    def start_game(self):
        pass

    def play_animation(self):
        an = Animations.TickerAnimation("weather")
        an.start()
        an.join()

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
        while not self.failed:
            self.direction = Direction.direction
            if self.direction == Direction.Direction.DOWN:
                self.failed = True
            api.display()
            time.sleep(0.2)

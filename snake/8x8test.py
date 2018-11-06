from threading import Thread

import pygame
import sys
import random
import time

pygame.init()
length = 600
width = 600
tile_size = 75
window = pygame.display.set_mode((length, width))
pygame.display.set_caption("8x8 Test")

window.fill((255, 255, 255))
pygame.display.update()


# Unnötige Scheiße von Leon
class Color:
    r: int = 0
    g: int = 0
    b: int = 0

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


# 1 Feld
class Tile:
    pos_x: int = 0
    pos_y: int = 0
    size: int = 0
    color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def __init__(self, pos_x, pos_y, size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def draw(self):
        pygame.draw.rect(window, (self.color.r, self.color.g, self.color.b),
                         (self.pos_x * tile_size, self.pos_y * tile_size, self.size, self.size))

    def change_color(self, color: Color):
        self.color = color
        self.draw()


class GameTicks(Thread):
    k = 0

    def __init__(self, tick_speed, g_tiles):
        pass

        Thread.__init__(self)
        self.tick_speed = tick_speed
        self.g_tiles = g_tiles

    def run(self):
        while True:
            time.sleep(self.tick_speed)


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

tiles = [Tile(m, n, tile_size) for n in range(0, length // tile_size) for m in range(0, width // tile_size)]


def grid():
    gridcolor = BLACK
    for i in range(tile_size):
        pygame.draw.rect(window, (gridcolor.r, gridcolor.g, gridcolor.b), (i * tile_size, 0, 1, length))
    for i in range(tile_size):
        pygame.draw.rect(window, (gridcolor.r, gridcolor.g, gridcolor.b), (0, i * tile_size, width, 1))


def keypressed(key):
    return pygame.key.get_pressed()[key]


k = 0
grid()

### MAIN LOOP ###
while True:
    if k < 64:
        tiles[k].draw()
        grid()
    else:
        k = 0

    pygame.display.update()

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                k += 1
            elif event.key == pygame.K_a:
                k -= 1
            elif event.key == pygame.K_w:
                k -= 8
            elif event.key == pygame.K_s:
                k += 8
        if event.type == pygame.MOUSEBUTTONDOWN:
            tiles[k].change_color(Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

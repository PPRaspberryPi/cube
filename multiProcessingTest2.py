import multiprocessing
import time

cube_size = 8
buffer_leds = [x % 2 for x in range(cube_size)]
leds = multiprocessing.Array('i', cube_size)


def display(leds):
    """for i, num in enumerate(buffer_leds):
        leds[i] = num """
    leds[:] = buffer_leds
    print("changed array")


def print_registers(leds):
    while True:
        print(leds[:])
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=print_registers, args=(leds,))
    p.start()
    time.sleep(2)
    display(leds)
    time.sleep(2)
    buffer_leds = [x % 3 for x in range(cube_size)]
    display(leds)
    p.join()

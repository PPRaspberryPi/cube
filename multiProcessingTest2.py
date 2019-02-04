import multiprocessing
from inputs import get_gamepad
import Direction
import time


def print_registers():
    while True:
        print(Direction.direction)
        try:
            events = get_gamepad()
        except Exception:
            print("no gamepad found")
        for eve in events:
            if eve.code == "ABS_HAT0Y" and eve.state == -1:
                Direction.direction = Direction.Direction.UP
            if eve.code == "ABS_HAT0Y" and eve.state == 1:
                Direction.direction = Direction.Direction.DOWN
            if eve.code == "ABS_HAT0X" and eve.state == 1:
                Direction.direction = Direction.Direction.RIGHT
            if eve.code == "ABS_HAT0X" and eve.state == -1:
                Direction.direction = Direction.Direction.LEFT
            if eve.code == "BTN_NORTH" and eve.state == 1:
                Direction.direction = Direction.Direction.BACK
            if eve.code == "BTN_SOUTH" and eve.state == 1:
                Direction.direction = Direction.Direction.FORTH

            # if eve.code is not "SYN_REPORT":
            #     print("Code: ", eve.code, "|", "State: ", eve.state)


def print_direction():
    while 1:
        print(Direction.direction)
        time.sleep(1)


if __name__ == '__main__':
    p = multiprocessing.Process(target=print_registers)
    p.start()
    p.join()

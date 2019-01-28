# import evdev
from evdev import InputDevice, categorize
from multiprocessing import Pool


def main(device):
    # creates object 'gamepad' to store the data
    # you can call it whatever you like
    gamepad = InputDevice('/dev/input/event' + str(device))

    # prints out device info at start
    print(gamepad)

    # evdev takes care of polling the controller in a loop

            
    for event in gamepad.read_loop():
        print("Pad",device,">>>", categorize(event))

p = Pool(2)
p.map(main,[17,18])
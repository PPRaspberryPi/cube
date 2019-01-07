from Ablage08012019 import main as cube


def led_on(*target_leds):
    """
    Schaltet beliebige Menge an LED's an
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        cube.buffer_cubes[(x[0] % 8) + ((x[1] % 8) * 8) + ((x[2] % 8) * 64)].setOn()


def led_off(*target_leds):
    """
    Schaltet beliebige Menge an LED's aus
    :param target_leds: [<layer>, <Zeile im Layer>, <LED in der Zeile>]
    :return: none
    """
    for x in target_leds:
        cube.buffer_cubes[(x[0] % 8) + ((x[1] % 8) * 8) + ((x[2] % 8) * 64)].setOff()


def start():
    cube.main()

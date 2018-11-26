import unittest

import numpy as np

import api


class TestLED(unittest.TestCase):
    def test_initialise(self):
        led = api.initialise()
        vgl = np.zeros(520, dtype=int)
        self.assertEqual(led.cube_array.all(), vgl.all())

    def test_nth_layer(self):
        led = api.initialise()
        led.nth_layer(1)
        self.assertFalse(led.cube_array[0 + 512], 1)
        self.assertEqual(led.cube_array[1+512], 1)
        self.assertFalse(led.cube_array[2 + 512], 1)

    def test_transmission(self):
        led = api.initialise()
        led.cube_array = np.ones(520, dtype=int)
        vgl = np.ones(520, dtype=int)
        led.transmission()
        self.assertEqual(led.buffer_array.all(), vgl.all())

    def test_turn_on(self):
        led = api.initialise()
        led.turn_on(1, 0, 0)
        self.assertEqual(led.cube_array[1], 1)
        led.turn_on(0, 2, 0)
        self.assertEqual(led.cube_array[2*64], 1)
        led.turn_on(0, 0, 3)
        self.assertEqual(led.cube_array[3 * 8], 1)
        led.turn_on(1, 2, 3)
        self.assertEqual(led.cube_array[1 + 2 * 64 + 3 * 8], 1)
        led.turn_on(7, 7, 7)
        self.assertEqual(led.cube_array[7 + 7 * 64 + 7 * 8], 1)

    def test_turn_off(self):
        led = api.initialise()
        led.cube_array = np.ones(520, dtype=int)
        led.turn_off(1, 0, 0)
        self.assertEqual(led.cube_array[1], 0)
        led.turn_off(0, 2, 0)
        self.assertEqual(led.cube_array[2*64], 0)
        led.turn_off(0, 0, 3)
        self.assertEqual(led.cube_array[3 * 8], 0)
        led.turn_off(1, 2, 3)
        self.assertEqual(led.cube_array[1 + 2 * 64 + 3 * 8], 0)
        led.turn_off(7, 7, 7)
        self.assertEqual(led.cube_array[7 + 7 * 64 + 7 * 8], 0)

    def test_toggle_state(self):
        led = api.initialise()
        led.cube_array = np.ones(520, dtype=int)
        led.toggle_state(1, 0, 0)
        self.assertEqual(led.cube_array[1], 0)
        led.toggle_state(0, 2, 0)
        self.assertEqual(led.cube_array[2*64], 0)
        led.toggle_state(0, 0, 3)
        self.assertEqual(led.cube_array[3 * 8], 0)
        led.toggle_state(1, 2, 3)
        self.assertEqual(led.cube_array[1 + 2 * 64 + 3 * 8], 0)
        led.toggle_state(1, 0, 0)
        self.assertEqual(led.cube_array[1], 1)
        led.toggle_state(0, 2, 0)
        self.assertEqual(led.cube_array[2 * 64], 1)
        led.toggle_state(0, 0, 3)
        self.assertEqual(led.cube_array[3 * 8], 1)

    def test_turn_off_all(self):
        led = api.initialise()
        led.cube_array = np.ones(520, dtype=int)
        list1 = led.cube_array
        led.turn_off_all()
        list2 = led.cube_array
        self.assertEqual(list1.all(), list2.all())

    def test_turn_on_all(self):
        led = api.initialise()
        list1 = led.cube_array
        led.turn_on_all()
        list2 = led.cube_array
        self.assertEqual(list1.all(), list2.all())

    def test_move_led(self):
        led = api.initialise()
        led.cube_array[0] = 1
        led.move_led(0, 0, 0, 7, 7, 7)
        self.assertEqual(led.cube_array[0], 0)
        self.assertEqual(led.cube_array[7 + 7 * 64 + 7 * 8], 1)

def main():
    unittest.main()


if __name__ == "__main__":
    main()

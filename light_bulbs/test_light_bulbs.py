import unittest
from light_bulbs import Room, LightBulb, InvalidColourException


class TestLigthBulb(unittest.TestCase):

    def test_can_create_light_bulb_object(self):
        self.bedroom_light = LightBulb()

    def test_is_on_returns_false(self):
        self.bedroom_light = LightBulb()
        self.assertEqual(self.bedroom_light.is_on(), False)

    def test_is_on_returns_true_when_is_on_is_called(self):
        self.bedroom_light = LightBulb()
        self.bedroom_light.turn_on()
        self.assertEqual(self.bedroom_light.is_on(), True)

    def test_is_on_returns_false_when_is_off_is_called(self):
        self.bedroom_light = LightBulb()
        self.bedroom_light.turn_off()
        self.assertEqual(self.bedroom_light.is_on(), False)

    def test_set_colour_changes_the_colour_of_the_light(self):
        self.bedroom_light = LightBulb("Green", ["White", "Red"])
        self.bedroom_light.colour = "Red"
        self.assertEqual(self.bedroom_light.colour, "Red")

    def test_an_assertion_is_raised(self):
        self.bedroom_light = LightBulb()
        with self.assertRaises(InvalidColourException) as cm:
            self.bedroom_light.colour = "Red"


class TestRoom(unittest.TestCase):

    def test_can_create_a_room_with_light_bulbs(self):
        light_1 = LightBulb()
        light_2 = LightBulb()
        self.living_room = Room("living_room", [light_1, light_2])

    def test_is_on_returns_true_when_all_the_lights_in_a_room_are_on(self):
        light_1 = LightBulb()
        light_2 = LightBulb()
        living_room = Room("living_room", [light_1, light_2])
        living_room.turn_on()
        self.assertEqual(light_1.is_on(), True)
        self.assertEqual(light_2.is_on(), True)
        self.assertEqual(living_room.is_on(), True)

    def test_is_on_returns_false_when_all_the_lights_in_a_room_are_off(self):
        light_1 = LightBulb()
        light_2 = LightBulb()
        self.living_room = Room("living_room", [light_1, light_2])
        self.living_room.turn_off()
        self.assertEqual(self.living_room.is_on(), False)


if __name__ == '__main__':
    unittest.main()

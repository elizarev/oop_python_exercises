
class InvalidColourException(Exception):
    """Raised when the colour is invalid """

    def __init__(self, input_colour, valid_colours):
        super().__init__(
            f"The colour {input_colour} is not valid, the valid colours are ")


class LightBulb:

    def __init__(self, input_colour="White", valid_colours=["White"]):
        self.status = False
        self._colour = input_colour
        self.valid_colours = valid_colours

    def is_on(self):
        return self.status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    # using property decorator
    # a getter function
    @property
    def colour(self):
        return self._colour

     # a setter function
    @colour.setter
    def colour(self, input_colour):
        if input_colour not in self.valid_colours:
            raise InvalidColourException(input_colour, self.valid_colours)
        self._colour = input_colour


class Room:

    def __init__(self, room, lights):
        self.name = room
        self._status = False
        self.lights = lights

    def is_on(self):
        return self._status

    def turn_on(self):
        for light in self.lights:
            light.turn_on()
        self._status = True

    def turn_off(self):
        for light in self.lights:
            light.turn_off()
        self._status = False

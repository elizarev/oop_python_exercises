# OOP practice exercise

## First Task
You have a Lightbulb class. The lightbulb has 3 methods: turnOn, turnOff, isOn

isOn should return false initially.

Once you call turnOn, isOn should return true

If you call turnOff again then isOn should return false.

Then you should add a setColour and a getColour methods.

setColour should change the colour of the light so when you call getColour you get the new colour.

A bit more advanced: If you call setColour with an invalid colour an InvalidColorException should be thrown

Or a default colour of white should be assigned or the method should have no effect

## Second Task

You have a Room class that accepts Lightbulb classes.

You should be able to call the turnOn and turnOff methods of the room to turn on or turn of all the lights in the room

#!/usr/bin/env python3
from pyfreebody import Freebody, Direction

body = Freebody("test", 30) # name, mass
body.addForce("Normal", 300, Direction.up) # name, magnitude, theta
body.addForce("Friction", 100, Direction.left) # name, magnitude, theta
body.diagram() # creates the diagram

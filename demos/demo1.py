from pyfreebody import Freebody, Direction
import math


body = Freebody("test", 30)
body.addForce("Normal", 30, Direction.up)
body.diagram()

from pyfreebody import Freebody, Direction

sysinc = math.pi/6
body = Freebody("inclinedplane", 20, SystemType.inclinedPlane, sysinc)
body.addForce("Normal", 200, sysinc + math.pi/2)
body.diagram()

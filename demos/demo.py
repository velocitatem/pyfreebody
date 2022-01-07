from pyfreebody import freebody
import math

testObj = {
    "name":"test",
    "forces": [
        {
            "name": "Friction",
            "magnitude": 40,
            "theta": math.pi
        },
        {
            "name": "Pull",
            "magnitude": 30,
            "theta": math.pi / 4
        },
        {
            "name": "Normal",
            "magnitude": 50,
            "theta": math.pi / 2
        }
    ]
}

freebody(testObj)

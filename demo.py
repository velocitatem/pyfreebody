import freebody
import math

testObj = {
    "name":"test",
    "forces": [
        {
            "name": "Friction",
            "magnitude": 20,
            "theta": math.pi / 2
        },
        {
            "name": "Pull",
            "magnitude": 10,
            "theta": math.pi/4
        }
    ]
}

freebody.freebody(testObj)

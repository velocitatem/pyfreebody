# pyFreeBody

**pyFreeBody** is an advanced and user-friendly free-body diagram generator for Python.

![simple demo](./examples/simple.png)

## Installation

Install pyFreeBody using pip:

```bash
pip3 install pyfreebody
```

## Features

- Generate free-body diagrams with ease.
- Supports various system types including basic and inclined planes.
- Customizable force magnitudes and directions.

## Quick Start

Here's a simple example to get you started:

```python
from pyfreebody.pyfreebody import Freebody, Direction, SystemType
import math

sysinc = math.pi/4
body = Freebody("inclinedplane", 20, SystemType.inclinedPlane, sysinc)
body.addForce("Normal", 200, sysinc + math.pi/2)
body.diagram()
```

This setup produces the following output:

![simple demo output](./examples/simple.out.png)

For detailed documentation, please refer [here](./docs.org).

## Dependencies

- Pillow

## Contributing

We welcome contributions! If you find a bug or have suggestions, please open an issue. If you'd like to contribute code, please fork the repository and submit a pull request.

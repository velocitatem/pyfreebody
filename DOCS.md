# pyfreebody Documentation

Welcome to the documentation for **pyfreebody**, a Python package for generating free-body diagrams programmatically. This package allows you to create, customize, and visualize free-body diagrams for various physical systems, such as basic objects under forces and objects on inclined planes.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Importing the Package](#importing-the-package)
  - [Creating a Freebody Instance](#creating-a-freebody-instance)
  - [Adding Forces](#adding-forces)
  - [Generating the Diagram](#generating-the-diagram)
- [Classes and Enums](#classes-and-enums)
  - [Freebody Class](#freebody-class)
  - [SystemType Enum](#systemtype-enum)
  - [LegendType Enum](#legendtype-enum)
  - [Direction Enum](#direction-enum)
- [Examples](#examples)
  - [Basic Freebody Diagram](#basic-freebody-diagram)
  - [Inclined Plane Diagram](#inclined-plane-diagram)
- [Customization](#customization)
  - [Colors](#colors)
  - [Legends](#legends)
  - [Arrow Styles](#arrow-styles)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

## Introduction

**pyfreebody** is a Python package designed to simplify the creation of free-body diagrams. It leverages the [Pillow](https://python-pillow.org/) library for image generation and allows you to define bodies, apply forces, and visualize the resulting diagrams with ease.

## Installation

You can install **pyfreebody** using `pip`:

```bash
pip install pyfreebody
```

## Quick Start

Here's a quick example to generate a simple free-body diagram:

```python
from pyfreebody import Freebody, Direction

# Create a freebody object
fb = Freebody(name="Block", mass=10)

# Add forces
fb.addForce(name="Gravity", magnitude=98.1, theta=Direction.down)
fb.addForce(name="Normal", magnitude=98.1, theta=Direction.up)

# Generate and display the diagram
fb.diagram()
```

This will create and display a free-body diagram of a block with gravitational and normal forces acting upon it.

## Usage

### Importing the Package

First, import the necessary classes from the package:

```python
from pyfreebody import Freebody, SystemType, LegendType, Direction
```

### Creating a Freebody Instance

Create an instance of the `Freebody` class:

```python
fb = Freebody(
    name="Block",           # Name of the body
    mass=10,                # Mass of the body in kg
    sysType=SystemType.basic  # Type of the system (default is basic)
)
```

#### Parameters:

- **name** *(str)*: The name of the body.
- **mass** *(float)*: The mass of the body.
- **sysType** *(SystemType)*: The type of system (e.g., `SystemType.basic`, `SystemType.inclinedPlane`).
- **incline** *(float)*: Incline angle in radians (used if `sysType` is `SystemType.inclinedPlane`).
- **arrows** *(bool)*: Whether to display arrowheads on forces.
- **color** *(function)*: Function to determine the color of the forces.
- **legend** *(LegendType)*: Type of legend to display.
- **path** *(str)*: Path to save the generated diagram.

### Adding Forces

Use the `addForce` method to apply forces to the body:

```python
fb.addForce(
    name="Applied Force",    # Name of the force
    magnitude=50,            # Magnitude of the force
    theta=Direction.right    # Direction of the force
)
```

#### Parameters:

- **name** *(str)*: Name of the force.
- **magnitude** *(float)*: Magnitude of the force.
- **theta** *(float or Direction)*: Direction of the force in radians or using `Direction` enum.

### Generating the Diagram

Generate and display the diagram using the `diagram` method:

```python
fb.diagram()
```

This method will create the diagram and either display it or save it to a specified path.

## Classes and Enums

### Freebody Class

The main class used to create and manage free-body diagrams.

#### Constructor Parameters:

- **name** *(str, default="empty")*: Name of the body.
- **mass** *(float, default=24)*: Mass of the body.
- **sysType** *(SystemType, default=SystemType.basic)*: Type of system.
- **incline** *(float, default=math.pi/6)*: Incline angle in radians.
- **arrows** *(bool, default=False)*: Display arrowheads if `True`.
- **color** *(function, default=randomColor)*: Function to determine force colors.
- **legend** *(LegendType, default=LegendType.default)*: Type of legend to display.
- **path** *(str, default=None)*: File path to save the diagram.

#### Methods:

- **addForce(name, magnitude, theta)**: Adds a force to the body.
- **diagram()**: Generates and displays/saves the diagram.

### SystemType Enum

Defines the type of system:

- **SystemType.basic**: Represents a basic system with no incline.
- **SystemType.inclinedPlane**: Represents an inclined plane system.

### LegendType Enum

Defines the legend display type:

- **LegendType.default**: Displays text in the top-left corner.
- **LegendType.arrow**: Displays text and magnitude with arrows.

### Direction Enum

Provides commonly used directions:

- **Direction.up**: Upward direction (π/2 radians).
- **Direction.down**: Downward direction (3π/2 radians).
- **Direction.left**: Leftward direction (π radians).
- **Direction.right**: Rightward direction (0 radians).

## Examples

### Basic Freebody Diagram

```python
from pyfreebody import Freebody, Direction

# Create a freebody object
fb = Freebody(name="Crate", mass=50)

# Add forces
fb.addForce(name="Gravity", magnitude=490.5, theta=Direction.down)
fb.addForce(name="Normal Force", magnitude=490.5, theta=Direction.up)
fb.addForce(name="Pull", magnitude=100, theta=Direction.right)
fb.addForce(name="Friction", magnitude=100, theta=Direction.left)

# Generate the diagram
fb.diagram()
```

This example creates a free-body diagram of a crate with gravity, normal force, applied pull, and friction forces.

### Inclined Plane Diagram

```python
import math
from pyfreebody import Freebody, SystemType, Direction

# Create a freebody object on an inclined plane
fb = Freebody(
    name="Block on Incline",
    mass=20,
    sysType=SystemType.inclinedPlane,
    incline=math.radians(30)  # 30 degrees incline
)

# Add forces
fb.addForce(name="Gravity", magnitude=196.2, theta=Direction.down)
fb.addForce(name="Normal Force", magnitude=169.7, theta=math.radians(120))
fb.addForce(name="Friction", magnitude=98.1, theta=math.radians(210))

# Generate the diagram
fb.diagram()
```

This example demonstrates a block on an inclined plane with gravity, normal force, and friction acting upon it.

## Customization

### Colors

You can customize the colors of the forces by providing a color function:

```python
def customColor():
    return (255, 0, 0)  # Red color

fb = Freebody(color=customColor)
```

### Legends

Choose how the legends are displayed using the `legend` parameter:

- **LegendType.default**: Default legend in the corner.
- **LegendType.arrow**: Legends displayed near the arrows.

```python
from pyfreebody import LegendType

fb = Freebody(legend=LegendType.arrow)
```

### Arrow Styles

Toggle the display of arrowheads using the `arrows` parameter:

```python
fb = Freebody(arrows=True)
```

This combined might produce something like:

![Untitled](https://github.com/user-attachments/assets/8335dfb0-aa01-4bf4-96c6-fa9aa45fb0e0)

## Troubleshooting

- **Image Not Displaying**: Ensure that your environment supports image display. In some cases, you may need to save the image to a file and open it manually.
- **Incorrect Force Directions**: Verify that the angles provided to `theta` are correct. Remember that angles are in radians.
- **Dependencies**: Make sure you have the required dependencies installed:

  ```bash
  pip install pillow==10.4.0
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute code, please open an issue or submit a pull request on the [GitHub repository](https://github.com/velocitatem/pyfreebody).

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Push your changes to your fork.
5. Submit a pull request describing your changes.

# Thank you for using pyfreebody!

We hope this package helps you in your projects. Happy diagramming!

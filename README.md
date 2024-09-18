# pyfreebody

[![PyPI version](https://img.shields.io/pypi/v/pyfreebody.svg)](https://pypi.org/project/pyfreebody/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python version](https://img.shields.io/pypi/pyversions/pyfreebody.svg)](https://pypi.org/project/pyfreebody/)
[![Downloads](https://pepy.tech/badge/pyfreebody)](https://pepy.tech/project/pyfreebody)

*Generate free-body diagrams with ease using Python!*

---

## Introduction

**pyfreebody** is a Python package that simplifies the creation of free-body diagrams for physics and engineering applications. Whether you're a student learning mechanics, a teacher preparing course materials, or an engineer visualizing forces, **pyfreebody** makes it easy to generate and customize free-body diagrams programmatically.

---

## Features

- 🌟 **Easy to Use**: Simple API for creating bodies and adding forces.
- 🎨 **Customizable Diagrams**: Adjust colors, labels, and styles to fit your needs.
- 🧭 **Supports Inclined Planes**: Handle basic systems and inclined planes effortlessly.
- 🎲 **Randomized Colors**: Automatically generate visually distinct force vectors.
- 💾 **Save and Display Diagrams**: Save diagrams to files or display them directly.
- 🔧 **Extensible**: Built with flexibility in mind for future enhancements.

---

## Installation

Install **pyfreebody** using `pip`:

```bash
pip install pyfreebody
```

---

## Quick Start

Here's how to create a basic free-body diagram:

```python
from pyfreebody import Freebody, Direction

# Create a free-body diagram for a block
fb = Freebody(name="Block", mass=10)

# Add forces acting on the block
fb.addForce(name="Gravity", magnitude=98.1, theta=Direction.down)
fb.addForce(name="Normal", magnitude=98.1, theta=Direction.up)
fb.addForce(name="Applied Force", magnitude=50, theta=Direction.right)
fb.addForce(name="Friction", magnitude=30, theta=Direction.left)

# Generate and display the diagram
fb.diagram()
```

This code will generate a free-body diagram of a block with gravitational, normal, applied, and frictional forces.
You can find the [documentation here](DOCS.md)

---


## Contributing

We welcome contributions! If you'd like to improve **pyfreebody**, please follow these steps:

1. **Fork** the repository.
2. **Create** a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes with descriptive messages:
   ```bash
   git commit -am 'Add new feature: your-feature-name'
   ```
4. **Push** to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Submit** a pull request to the main branch.

Please ensure your code follows best practices and includes appropriate tests.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

**pyfreebody** - Making physics diagrams effortless! 🚀

Bring your physics problems to life with clear and precise free-body diagrams. Happy diagramming!

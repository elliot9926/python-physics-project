# python-physics-project
An interactive n-body gravitational physics simulator written in Python

# Description
This project allows us to simulate the motion of three bodies that interact only through gravity
This problem has no exact, single solution, meaning the project will take the input of initial velocities masses, and positions of the objects to simulate their movement through space with reference to their mutual center of gravity

# Requirements
- Python 3.10.x
- VPython 7.6.5 - Used for vector math and for creating an interactive 3D environment 
- MatPlotLib 3.10.8 - Used for generating a graph of results after the simulation is run

# Installation
1. Download the appropriate version of Python onto your system
2. Clone the repository with 
```
git clone https://github.com/elliot9926/python-physics-project
```
3. Navigate into the `python-physics-project` directory and create a `venv` with
```
[path-to-your-python-executable] -m venv .venv_physics
```
4. Activate the venv using
```
source .venv_physics/bin/activate
```
5. Finally, install the required packages using 
```
pip install -r requirements.txt
```

# Usage
Execute runtime.py to launch the software. Click on the 'Run' button to begin the simulation.

To be added: UI-Based editing of body attributes

# Features
- Adjustable mass, initial velocity, and position
- Animated visualization in VPython

# Examples/demos
- Default system of 3 bodies included in default_objects.py

# License
Distributed under CC BY-SA 4.0

# Contributors/Contact
Elliot Lyons: e.lyons@student.maastrichtuniversity.nl
Kelly Bowker: k.Bowker@student.maastrichtuniversity.nl
Tomáš Bursík: t.bursik@student.maastrichtuniversity.nl
Cas Kitzen: k.kitzen@student.maastrichtuniversity.nl
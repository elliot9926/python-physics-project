# python-physics-project
An interactive n-body gravitational physics simulator written in Python

# Description
This project allows the user to simulate gravitational interactions between several bodies. Its main purpose is to display the non-deterministic and chaotic nature of the three-body problem.
This problem has no exact, single solution, meaning the project will take the input of initial velocities masses, and positions of the objects to simulate their movement through space with reference to their mutual center of gravity

# Requirements
- Python 3.10.x
- VPython 7.6.5 - Used for vector math and for creating an interactive 3D environment 
- MatPlotLib 3.10.8 - Used for generating a graph of results after the simulation is run

# Installation
1. Install the appropriate version of Python onto your system
2. Clone the repository with 
```
git clone https://github.com/elliot9926/python-physics-project
cd python-physics-project
```
3. Create a virtual environment with
```
[path-to-your-python-executable] -m venv .venv_physics
source .venv_physics/bin/activate
```
4. Finally, install the required packages using 
```
pip install -r requirements.txt
```

# Usage
While in the `python-physics-project` directory, run
```
python src/runtime.py
```
Use the Run button to begin the simulation.

Navigating the viewport:
- Right click + drag to rotate
- Scroll wheel to zoom
- Shift + left click to pan

# Features
- Dynamically change physical attributes such as mass, velocity, and position through the UI
- Editable visual attributes such as name, color, and radius
- Animated visualization in VPython
- Ability to create a plot of average distances within the system using matplotlib
    - Why average distances? As the final state of a 3+ body system in this simulation will see one or more bodies ejected, the average distance between bodies is a clear indicator of when the system loses relative stability.

# Examples/demos
A stable system of two equal-mass stars is created by default. Try adding a third body to see what happens!

# License
Distributed under CC BY-SA 4.0

# Contributors/Contact
Elliot Lyons: e.lyons@student.maastrichtuniversity.nl
Kelly Bowker: k.Bowker@student.maastrichtuniversity.nl
Tomáš Bursík: t.bursik@student.maastrichtuniversity.nl
Cas Kitzen: k.kitzen@student.maastrichtuniversity.nl
import numpy as np
import vpython as vp    # Seems like a decent library for 3d physics simulations, we'll use its vectors for our math

class Simulation:
        """Highest-level control loop which actually runs the simulation"""
        def __init__(self, system, dt):
             self.system = system
             self.dt = dt # Delta time
             self.time = 0.0 # Starts at 0 when we initialize

        def step(self, dt): # Steps towards the next moment in time
             pass

class System(Simulation):
     """The overall system including the bodies and the forces"""
     def __init__(self, bodies, integrator):
          pass
     

class  Integrator(Simulation):  # Verlet integrator, I still need to read more about this but it seems like the standard
     pass

class Body(System):
    """A class to represent a spherical rigid body"""
    def __init__(self, mass, radius, velocity, position, force):
        self.mass = mass            # Body's mass in kg
        self.radius = radius        # Body's radius in meters
        self.velocity = velocity    # Body's initial velocity as a 3D vector in m/s
        self.position = position    # Body's position in 3D Cartesian space
        self.force = force          # The sum of forces currently acting on the body



    def update(time):
        pass

def write_file(system):
     """Updates a file with the current states of all bodies in the system"""
     pass



 

import vpython as vp    # seems like a decent library for 3d physics simulations

class Simulation:
        """Highest-level control loop which actually runs the simulation"""
        def __init__(self, system, dt):
             self.system = system
             self.dt = dt # Delta time
             self.time = 0.0 # Starts at 0 when we initialize

        def step(self, dt): # Steps towards the next moment in time
             pass

class System:
     """The overall system including the bodies and the forces"""
     def __init__(self, bodies, integrator):
          pass
     

class  Integrator:  # Verlet integrator, I still need to read more about this but it seems like the standard
     pass

class Body:
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

# An example object to test the class
earth = Body(5.972e24, 6.371e6, vp.vector(30000, 0, 0), vp.vector(0,0,0))

 

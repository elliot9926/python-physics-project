import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import vpython as vp    # Seems like a decent library for 3d physics simulations, we'll use its vectors for our math

class Simulation:
        """Highest-level control loop which actually runs the simulation"""
        def __init__(self, system, dt, total_time, write_positions=False):
             self.system = system
             self.dt = dt # Delta time
             self.total_time = total_time
             self.time = 0.0 # Starts at 0 when we initialize
             self.write_positions = write_positions
             

        def step(self): # Steps towards the next moment in time
             self.system.integrator.step(self.system.bodies, self.system.gravity_system, self.dt)

             if self.write_positions:
               for body in self.system.bodies:
                    body.write_position()
        
        @property
        def step_count(self):
          return int(np.floor(self.total_time / self.dt))
        
        def plot_results(self):
          bodies = self.system.bodies
          fig = plt.figure()
          ax = fig.add_subplot(111, projection='3d')

          for body in bodies:
               x, y, z = [], [], []

               for i in body.position_history:
                    x.append(i.x)
                    y.append(i.y)
                    z.append(i.z)

               ax.scatter(x, y, z, cmap='viridis', marker='o')

          plt.show()
               
               

class System:
     """The overall system including the bodies and the forces"""
     def __init__(self, bodies, integrator, gravity_system):
          self.__bodies = bodies
          self.integrator = integrator
          self.gravity_system = gravity_system

     @property
     def bodies(self):
          return self.__bodies
     

class Body:
    """A class to represent a spherical rigid body"""
    def __init__(self, mass, radius, velocity, position, acceleration = vp.vector(0,0,0)):
          self.mass = mass                     # Body's mass in kg
          self.radius = radius                 # Body's radius in meters
          self.velocity = velocity             # Body's initial velocity as a 3D vector in m/s
          self.position = position             # Body's position in 3D Cartesian space
          self.acceleration = acceleration     # Total acceleration of the body
          self.position_history = []
    

    def write_position(self):
         self.position_history.append(self.position)
     

class GravitySystem:
     G = 6.6743e-11      # Gravitational constant
     
     def __init__(self):
          pass
     
     def compute_accelerations(self, bodies):
          accelerations = []

          for body_i in bodies:
               total_acceleration = vp.vector(0, 0, 0)      # The sum of accelerations acting on this body 

               for body_j in bodies:
                    if body_i == body_j:                    
                         continue
                    
                    r = body_j.position - body_i.position   # Get the difference vector between the position vectors of the two bodies
                    distance = vp.mag(r + vp.vector(1e-10, 1e-10, 1e-10)    )        # The magnitude of the difference vector is the distance between the bodies

                    total_acceleration += self.G * body_j.mass * r / distance**3     
               
               accelerations.append(total_acceleration)

          return accelerations
          
     

class  VelocityIntegrator:  # Verlet integrator, I still need to read more about this but it seems like the standard
     def __init__(self):
          pass
     def step(self, bodies, gravity_system, dt):
           # 1. Compute current accelerations of all bodies
          accelerations = gravity_system.compute_accelerations(bodies)

          # 2. Update positions
          for body, acc in zip(bodies, accelerations):
                    body.position += body.velocity * dt + 0.5 * acc * dt**2

          # 3. Compute new accelerations
          new_accelerations = gravity_system.compute_accelerations(bodies)

          # 4. Update velocities
          for body, acc_old, acc_new in zip(bodies, accelerations, new_accelerations):
               body.velocity += 0.5 * (acc_old + acc_new) * dt




def write_file(system):
     """Updates a file with the current states of all bodies in the system"""
     pass



 


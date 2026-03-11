import vpython as vp
import math

class Simulation:
        """Highest-level control loop which actually runs the simulation"""
        def __init__(self, system, dt,  ui_helper=None, graph_helper=None, write_positions=False, is_running=False, visualizer=None):
             self.system = system
             self.dt = dt # Delta time
             self.time = 0.0 # Starts at 0 when we initialize
             self.write_positions = write_positions # TODO: remove this line
             self.is_running = is_running
             self.visualizer = visualizer
             self.ui_helper = ui_helper
             self.graph_helper = graph_helper
             
               # Used to create a graph of the average distances in the simulation
             self.average_distances = []
             self.average_distances_times = [] 

             

        def step(self): 
             """Steps forward one dt in time"""
             self.system.integrator.step(self.system.bodies, self.system.gravity_system, self.dt)

             self.time += self.dt

             self.average_distances.append(self.system.calculate_average_distances(self.system.bodies))
             self.average_distances_times.append(math.floor(self.time/(3600*24)))

        def create_graph(self):
             self.graph_helper.draw_graph(self.average_distances_times, self.average_distances)
            
class System:
     """The overall system including the bodies and the forces"""
     def __init__(self, bodies, integrator, gravity_system):
          self.__bodies = bodies
          self.integrator = integrator
          self.gravity_system = gravity_system

     @property
     def bodies(self):
          return self.__bodies
     
     def add_new_body(self, sim):
          """Adds a new body to the simulation after initialization"""
          new_body = Body(
               mass=1.989e30, 
               radius=695700e3, 
               velocity=vp.vector(0, 0, 0), 
               position=vp.vector(0, 0, 0),
               name='New Body'
          )

          print(f"\n\nSimulation: {sim}\nSim visualizer:{sim.visualizer}\n\n")
          self.__bodies.append(new_body)
          sim.visualizer.append_body(new_body)

          return new_body
     
     @staticmethod
     def calculate_average_distances(bodies):
          """Calculates the average distance between bodies from a given list"""
          total = 0

          for body_i in bodies:
               my_avg = 0

               for body_j in bodies:
                    if body_i == body_j:                    
                         continue
                    my_avg += vp.mag(body_i.position - body_j.position)
               my_avg = my_avg / (len(bodies) - 1)

               total += my_avg
          
          total = total / (len(bodies) - 1)

          return total
     

class Body:
    """A class to represent a spherical rigid body"""
    def __init__(self, mass, radius, velocity, position, acceleration = vp.vector(0,0,0), name='None', vis_object=None):
          self.mass = mass                     # Body's mass in kg
          self.radius = radius                 # Body's radius in meters
          self.velocity = velocity             # Body's initial velocity as a 3D vector in m/s
          self.position = position             # Body's position in 3D Cartesian space
          self.acceleration = acceleration     # Total acceleration of the body
          self.position_history = []
          self.name = name
          self.vis_object = vis_object         # The VPython sphere used to represent this body
    
    def __str__(self):
          return self.name

    def write_position(self): # TODO: remove this block
         self.position_history.append(self.position)

     

class GravitySystem:
     """Implementation of Newtonian gravity"""
     G = 6.6743e-11      # Gravitational constant
     
     def __init__(self):
          pass
     
     @staticmethod
     def compute_accelerations(bodies):
          """Iterates through the bodies and calculates their gravitational acceleration"""
          accelerations = []

          for body_i in bodies:
               total_acceleration = vp.vector(0, 0, 0)      # The sum of accelerations acting on this body 

               for body_j in bodies:
                    if body_i == body_j:                    
                         continue
                    
                    r = body_j.position - body_i.position   # Get the difference vector between the position vectors of the two bodies
                    distance = vp.mag(r + vp.vector(1e-10, 1e-10, 1e-10))        # The magnitude of the difference vector is the distance between the bodies

                    total_acceleration += GravitySystem.G * body_j.mass * r / distance**3     
               
               accelerations.append(total_acceleration)

          return accelerations
          
     

class  VelocityIntegrator:  # Verlet integrator, I still need to read more about this but it seems like the standard
     """Integrator which updates the positions and velocities of the given bodies"""
     def __init__(self):
          pass

     def step(self, bodies, gravity_system, dt):
          """Changes the positions and velocities of the bodies"""
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
     """Updates a file with the current states of all bodies in the system (may be removed)"""
     pass



 


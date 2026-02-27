import vpython as vp

class Visualizer:
    def __init__(self, simulation):
        self.simulation = simulation
        self.vis_bodies = []

        # Initialize a list of vpython objects to represent the bodies
        for body in simulation.system.bodies:
            new_sphere = vp.simple_sphere(pos=body.position, radius=body.radius, make_trail=True, retain=50)
            self.vis_bodies.append(new_sphere)




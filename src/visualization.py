import vpython as vp

class Visualizer:
    """Used to initialize the 3D objects within the VPython UI"""
    def __init__(self, simulation):
        self.simulation = simulation
        self.vis_bodies = []

        # Create a list of vpython sphere objects to visually represent the bodies
        for body in simulation.system.bodies:
            new_sphere = vp.simple_sphere(pos=body.position, radius=body.radius, make_trail=True, retain=50)
            self.vis_bodies.append(new_sphere)




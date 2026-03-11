import vpython as vp

class Visualizer:
    """Used to initialize the 3D objects within the VPython UI"""
    def __init__(self, simulation):
        self.simulation = simulation
        self.vis_bodies = []

        # Sets the display window size
        scene_width = 1200 # Width of the display window in pixels
        
        vp.scene.width = scene_width
        vp.scene.height = scene_width*(0.5)

        # Create a list of vpython sphere objects to visually represent the bodies
        for body in simulation.system.bodies:
            self.append_body(body)
    
    def append_body(self, body):
        """Used to add a new body to the visualization list"""
        new_sphere = vp.simple_sphere(pos=body.position, radius=body.radius, make_trail=True, retain=500)
        body.vis_object = new_sphere
        self.vis_bodies.append(new_sphere)
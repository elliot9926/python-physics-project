import vpython as vp

class Visualizer:
    """Used to display 3D object representations of bodies using VPython"""
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
        """Adds a new body to the visualization list"""
        new_sphere = vp.simple_sphere(
            pos=body.position, 
            radius=body.radius, 
            make_trail=True, 
            #retain=1000, 
            color=vp.color.blue, 
            trail_color=vp.color.white,
            )
        
        body.vis_object = new_sphere
        self.vis_bodies.append(new_sphere)
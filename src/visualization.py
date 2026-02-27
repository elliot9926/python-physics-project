import vpython as vp


# Initialize a list of vpython objects to represent the bodies
def initialize_visualization(simulation):
    vis_bodies = []

    for body in simulation.system.bodies:
        new_sphere = vp.simple_sphere(pos=body.position, radius=body.radius, make_trail=True, retain=50)
        vis_bodies.append(new_sphere)
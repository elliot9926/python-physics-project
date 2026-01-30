class Body:
    """A class to represent a spherical rigid body"""
    def __init__(self, mass, radius, velocity):
        self.mass = mass            # Body's mass in kg
        self.radius = radius        # Body's radius in meters
        self.velocity = velocity    # Body's initial velocity as a 3D vector in m/s



# An example object to test the class
earth = Body(5972000000000000000000000, 6371000, [30000, 0, 0]) #ok maybe the earth is a bit large for the units i'm using

 

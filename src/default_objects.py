import simulation_classes
import draw_ui
import vpython as vp

def create_defaults():
    """Initializes all required objects and adds default bodies (earth and sun) to the system"""
    sol = simulation_classes.Body(
        mass=1.989e30, 
        radius=6957000e3, 
        velocity=vp.vector(-1e4, 1e4, 0),     # We're defining x and y as the plane of earth's orbit
        position=vp.vector(8.7e10, 1.2e11, 0),
        name='Sol'
        )
        
    sun = simulation_classes.Body(
        mass=1.989e30,
        radius=6957000e3, 
        velocity=vp.vector(1e4, -1e4, 0), 
        position=vp.vector(0, 0, 0),
        name='Sun'
        )

    bodies = [sol, sun]

    gravity_system = simulation_classes.GravitySystem()
    integrator = simulation_classes.VelocityIntegrator()


    system = simulation_classes.System(bodies, integrator, gravity_system)

    simulation = simulation_classes.Simulation(
        system=system, 
        dt=3600*12.0 # Length of a time step, hardcoded as 12 hours
        )

    return simulation
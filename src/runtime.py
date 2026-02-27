import classes
import vpython as vp

earth = classes.Body(
    mass=5.97e24, 
    radius=6371e3, 
    velocity=vp.vector(-2.43e4, 1.77e4, 0),     # For now, I'm defining x and y as the plane of earth's orbit
    position=vp.vector(8.7e10, 1.2e11, 0)
    )
    
sun = classes.Body(
    mass=1.989e30, 
    radius=695700e3, 
    velocity=vp.vector(0, 0, 0), 
    position=vp.vector(0, 0, 0)
    )

sun2 = classes.Body(
    mass=1.989e29, 
    radius=695700e3, 
    velocity=vp.vector(2.43e4, -1.77e4, -3e3),     # For now, I'm defining x and y as the plane of earth's orbit
    position=vp.vector(-8.7e10, 1.2e11, 10e7)
    )

bodies = [earth, sun, sun2]

gravity_system = classes.GravitySystem()
integrator = classes.VelocityIntegrator()

system = classes.System(bodies, integrator, gravity_system)

sim = classes.Simulation(system, 3600*12.0, 3600*24*365.0, True)
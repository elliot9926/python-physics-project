import vpython as vp
import default_objects as objects
import visualization
import ui_functions
import draw_ui

# Initialize default objects (including default bodies)
simulation = objects.create_defaults()

bodies = simulation.system.bodies

# Initialize 3D objects for each body
visualizer = visualization.Visualizer(simulation)

# Draw the initial UI
ui_functions.set_simulation(simulation)

draw_ui.initial_draw(bodies)



while True:
    """VPython will always be running, at a rate of 30 updates/second"""
    vp.rate(30)

    if simulation.is_running:
        simulation.step()

        # Updates visual representation for each body
        for body in bodies:
            visualizer.vis_bodies[bodies.index(body)].pos = body.position
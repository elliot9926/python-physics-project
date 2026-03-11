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
simulation.visualizer = visualizer

ui_helper = draw_ui.UiHelper(bodies)
simulation.ui_helper = ui_helper

# Pass the simulation into ui_functions
ui_functions.set_simulation(simulation)


while True:
    """VPython will always be running, at a rate of 30 updates/second"""
    vp.rate(30)

    if simulation.is_running:
        simulation.step()
        
      #  simulation.ui_helper.disable_buttons()

    # Updates visual representation for each body
        for body in bodies:
            visualizer.vis_bodies[bodies.index(body)].pos = body.position
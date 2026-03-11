import vpython as vp
import math
import default_objects as objects
import visualization
import ui_functions
import draw_ui
import create_graph


# Initialize default objects (including default bodies)
simulation = objects.create_defaults()

bodies = simulation.system.bodies

# Initialize 3D objects for each body
visualizer = visualization.Visualizer(simulation)
simulation.visualizer = visualizer

ui_helper = draw_ui.UiHelper(bodies)
simulation.ui_helper = ui_helper

graph_helper = create_graph.GraphHelper
simulation.graph_helper = graph_helper

# Pass the simulation into ui_functions
ui_functions.set_simulation(simulation)


while True:
    """VPython will always be running, at a rate of 30 updates/second"""
    vp.rate(30)

    # Updates visual representation for each body
    for body in bodies:
            visualizer.vis_bodies[bodies.index(body)].pos = body.position

    if simulation.is_running:
        simulation.step()
        
        for body in bodies:
            visualizer.vis_bodies[bodies.index(body)].make_trail = True
    

        # Update the visual timer
        time_in_days = math.floor(simulation.time/(3600*24))
        ui_helper.timer.text = f"Simulation time: {time_in_days} days"
    else:
        pass
        for body in bodies:
            visualizer.vis_bodies[bodies.index(body)].make_trail = False

    
        
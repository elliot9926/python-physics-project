import vpython as vp
import default_objects as objects
import visualization
import draw_ui




# Initialize default objects (including default bodies)
simulation = objects.create_defaults()

bodies = simulation.system.bodies

# Initialize 3D objects for each body
visualization.initialize_visualization(simulation)

# Draw the initial UI
draw_ui.first_draw(bodies)



while True:
    vp.rate(30)

    if simulation.is_running:
        simulation.step()

        for body in bodies:
            visualization.vis_bodies[bodies.index(body)].pos = body.position
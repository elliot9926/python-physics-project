import vpython as vp
import ui_functions

def initial_draw(bodies):
    """Initializes Run button and UI elements for default bodies"""
    run_button = vp.button(bind=ui_functions.run_button, text='Run')
    vp.scene.append_to_caption('\n\n')

    for body in bodies:
        draw_body_row(body)

rows = []
colors = ["Blue", "Yellow", "Green", "Orange", "Red", "White"]

def draw_body_row(body):
    """Draws a row of buttons and other inputs to modify a specific body's attributes"""
    buttons = []
    
    # Name input
    name_input = vp.winput(bind=lambda w: ui_functions.name_input(w, body), type='string', width=50, text=body.name)
    buttons.append(name_input)
    vp.scene.append_to_caption("    ")

    # Color input
    vp.scene.append_to_caption("Color: ")
    color_input = vp.menu(bind=lambda w: ui_functions.color_input(w, body), choices=colors)
    vp.scene.append_to_caption("    ")

    # Mass input
    vp.scene.append_to_caption("Mass: ")
    mass_input = vp.winput(bind=lambda w: ui_functions.mass_input(w, body), type='numeric', text=body.mass) # We have to use a lambda function in order to pass the body object to the button function
    buttons.append(mass_input)
    vp.scene.append_to_caption("    ")

    # Position input
    vp.scene.append_to_caption("Position: ")

    vp.scene.append_to_caption("X: ")
    pos_x = vp.winput(bind=lambda w: ui_functions.position_input(w, body, 'x'), type='numeric', text=f"{body.position.x: .1e}", width=75)
    vp.scene.append_to_caption("  ")

    vp.scene.append_to_caption("Y: ")
    pos_y = vp.winput(bind=lambda w: ui_functions.position_input(w, body, 'y'), type='numeric', text=f"{body.position.y: .1e}", width=75)
    vp.scene.append_to_caption("  ")

    vp.scene.append_to_caption("Z: ")
    pos_z = vp.winput(bind=lambda w: ui_functions.position_input(w, body, 'z'), type='numeric', text=f"{body.position.z: .1e}", width=75)
    
    buttons.extend([pos_x, pos_y, pos_z])
    vp.scene.append_to_caption("    ")

    # Velocity input
    vp.scene.append_to_caption("Velocity: ")

    vp.scene.append_to_caption("X: ")
    vel_x = vp.winput(bind=lambda w: ui_functions.velocity_input(w, body, 'x'), type='numeric', text=f"{body.velocity.x: .1e}", width=75)
    vp.scene.append_to_caption("  ")

    vp.scene.append_to_caption("Y: ")
    vel_y = vp.winput(bind=lambda w: ui_functions.velocity_input(w, body, 'y'), type='numeric', text=f"{body.velocity.y: .1e}", width=75)
    vp.scene.append_to_caption("  ")

    vp.scene.append_to_caption("Z: ")
    vel_z = vp.winput(bind=lambda w: ui_functions.velocity_input(w, body, 'z'), type='numeric', text=f"{body.velocity.z: .1e}", width=75)
    
    buttons.extend([vel_x, vel_y, vel_z])
    vp.scene.append_to_caption("    ")

    

    
    
    vp.scene.append_to_caption('\n\n')
    rows.append(buttons)

def disable_buttons():
    """Disables all attribute-editing buttons, to be called when the simulation starts"""
    for row in rows:
        for button in row:
            button.disabled = True




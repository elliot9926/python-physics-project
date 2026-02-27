import vpython as vp
import ui_functions

def initial_draw(bodies):
    run_button = vp.button(bind=ui_functions.run_button, text='Run')
    vp.scene.append_to_caption('\n\n')

    for body in bodies:
        draw_body_row(body)

def draw_body_row(body):
    name_input = vp.winput(bind=ui_functions.name_input, type='string', width=50, text=body.name)
    vp.scene.append_to_caption("    ")

    vp.scene.append_to_caption("Mass: ")
    mass_input = vp.winput(bind=ui_functions.mass_input, type='numeric', text=body.mass)
    
    vp.scene.append_to_caption('\n\n')


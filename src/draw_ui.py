import vpython as vp
import ui_functions

class UiHelper:
    def __init__(self, bodies):
        """Initializes buttons and UI elements for default bodies"""
        self.rows = []
        self.colors = ["Blue", "Yellow", "Green", "Orange", "Red", "White"]

        buttons = []  # List of temporary buttons which will deactivate when the simulation is started
        
        run_button = vp.button(bind=ui_functions.run_button, text='Run')
        vp.scene.append_to_caption("    ")

        add_button = vp.button(bind=ui_functions.add_button, text='Add body')
        vp.scene.append_to_caption("    ")

        graph_button = vp.button(bind=ui_functions.graph_button, text='Create Graph')
        vp.scene.append_to_caption("    ")


        self.timer = vp.wtext(text=f"Simulation time: 0 days")

        vp.scene.append_to_caption('\n\n')
        self.rows.append(buttons)

    
        for body in bodies:
            self.draw_body_row(body)
        
    def draw_body_row(self, body):
        """Draws a row of buttons and other inputs to modify a specific body's attributes"""
        buttons = []
        
        # Name input
        name_input = vp.winput(bind=lambda w: ui_functions.name_input(w, body), type='string', width=50, text=body.name)
        buttons.append(name_input)
        vp.scene.append_to_caption("    ")

        # Color input
        vp.scene.append_to_caption("Color: ")
        color_input = vp.menu(bind=lambda w: ui_functions.color_input(w, body), choices=self.colors)
        vp.scene.append_to_caption("    ")

        # Mass input
        vp.scene.append_to_caption("Mass (kg): ")
        mass_input = vp.winput(bind=lambda w: ui_functions.mass_input(w, body), type='numeric', text=body.mass) # We have to use a lambda function in order to pass the body object to the button function
        buttons.append(mass_input)
        vp.scene.append_to_caption("    ")

        # Radius input
        vp.scene.append_to_caption("Radius (m): ")
        radius_input = vp.winput(bind=lambda w: ui_functions.radius_input(w, body), type='numeric', text=body.radius) 
        buttons.append(radius_input)
        vp.scene.append_to_caption("    ")

        # Position input
        vp.scene.append_to_caption("Position (m): ")

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
        vp.scene.append_to_caption("Velocity (m/s): ")

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
        self.rows.append(buttons)

    def disable_buttons(self):
        """Disables all attribute-editing buttons, to be called when the simulation starts"""
        for row in self.rows:
            for button in row:
                button.disabled = True




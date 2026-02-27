import vpython as vp

def set_simulation(sim):
    """Gets a reference to the Simulation object so the buttons can affect its attributes"""
    global simulation
    simulation = sim

def run_button(button):
    """Simple pause/play button for the simulation"""
    if button.text == 'Pause':
        button.text = 'Run'
        simulation.is_running = False
    else:
        button.text = 'Pause'
        simulation.is_running = True

# TODO: implement mass and name input functions
def mass_input(input):
    """Allows for user to change a body's mass"""
    pass

def name_input(input):
    """Allows for user to change a body's name"""
    pass
        
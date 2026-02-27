import vpython as vp

def set_simulation(sim):
    global simulation
    simulation = sim

def run_button(button):
    if button.text == 'Pause':
        button.text = 'Run'
        simulation.is_running = False
    else:
        button.text = 'Pause'
        simulation.is_running = True

# TODO: implement mass and name input functions
def mass_input(input):
    pass

def name_input(input):
    pass
        
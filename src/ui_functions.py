import vpython as vp

def set_simulation(sim):
    global simulation
    simulation = sim


def run_button(button):
    if button.text == 'Pause':
        button.text = 'Run'

        print("Running")

        simulation.is_running = False
    else:
        button.text = 'Pause'

        print("Pausing")

        simulation.is_running = True

def mass_input(input):
    pass

def name_input(input):
    pass
        
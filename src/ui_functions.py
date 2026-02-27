import vpython as vp
import runtime



def run_button(button):
    if button.text == 'Pause':
        button.text = 'Run'

        print("Running")

        runtime.sim.is_running = False
    else:
        button.text = 'Pause'

        print("Pausing")

        runtime.sim.is_running = True

def mass_input(input):
    pass

def name_input(input):
    pass
        
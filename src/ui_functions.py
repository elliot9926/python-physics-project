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

def mass_input(input, body):
    """Allows for user to change a body's mass"""
    body.mass = float(input.number)

def name_input(input, body):
    """Allows for user to change a body's name"""
    body.name = input

def color_input(input, body):
    """Allows for user to change a body's color"""
    color_dict = {"Blue": vp.color.blue, "Yellow": vp.color.yellow, "Green": vp.color.green, "Orange": vp.color.orange, "Red": vp.color.red, "White": vp.color.white}
    
    print(f"\n\nInput: {input}\n\n")
    body.vis_object.color = color_dict[input]

def position_input(input, body, axis):
    """Allows for user to change a body's initial position"""
    if axis == 'x':
        body.position.x = float(input.number)
    elif axis == 'y':
        body.position.y = float(input.number)
    elif axis == 'z':
        body.position.z = float(input.number)

def velocity_input(input, body, axis):
    """Allows for user to change a body's initial velocity"""
    if axis == 'x':
        body.velocity.x = float(input.number)
    elif axis == 'y':
        body.velocity.y = float(input.number)
    elif axis == 'z':
        body.velocity.z = float(input.number)
        


        
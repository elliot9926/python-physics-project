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

def add_button(button):
    """Used to add a new body to the simulation before starting"""
    new_body = simulation.system.add_new_body(simulation)

    print(f"\n\nNew body info:\n{repr(new_body)}")     # For debugging
    simulation.ui_helper.draw_body_row(new_body)

def graph_button(button):
    """Button to generate an average distance graph"""
    simulation.create_graph()

def mass_input(input, body):
    """Allows for user to change a body's mass"""
    try:
        body.mass = float(input.number)
    except TypeError:
        print("\nInvalid input for mass: numerical inputs only.\n")

def radius_input(input, body):
    """Allows for user to change a body's radius"""
    try:
        new_radius = float(input.number)
        
        body.radius = new_radius
        body.vis_object.radius = new_radius
    except TypeError:
        print("\nInvalid input for radius: numerical inputs only.\n")

def name_input(input, body):
    """Allows for user to change a body's name"""
    body.name = input

def color_input(input, body):
    """Allows for user to change a body's color"""
    color_list = [vp.color.blue, vp.color.yellow, vp.color.green, vp.color.orange, vp.color.red, vp.color.white]

    print(f"\n\nInput: {input}\n\n")
    body.vis_object.color = color_list[input.index]

def position_input(input, body, axis):
    """Allows for user to change a body's initial position"""
    try:
        if axis == 'x':
            body.position.x = float(input.number)
        elif axis == 'y':
            body.position.y = float(input.number)
        elif axis == 'z':
            body.position.z = float(input.number)
    except TypeError:
        print("\nInvalid input for position: numerical inputs only.\n")

def velocity_input(input, body, axis):
    """Allows for user to change a body's initial velocity"""
    try:
        if axis == 'x':
            body.velocity.x = float(input.number)
        elif axis == 'y':
            body.velocity.y = float(input.number)
        elif axis == 'z':
            body.velocity.z = float(input.number)
    except TypeError:
        print("\nInvalid input for velocity: numerical inputs only.\n")
        


        
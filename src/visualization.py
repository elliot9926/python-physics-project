import vpython as vp
import runtime

# Initialize a list of vpython objects to represent the bodies
vis_bodies = []

for body in runtime.bodies:
    new_sphere = vp.simple_sphere(pos=body.position, radius=body.radius, make_trail=True, retain=50)
    vis_bodies.append(new_sphere)

dt = runtime.sim.dt


while True:
    vp.rate(30)

    runtime.sim.step()

    for body in runtime.bodies:
        vis_bodies[runtime.bodies.index(body)].pos = body.position



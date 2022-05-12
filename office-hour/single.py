from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.05, exposure=5)
scene.set_background_color((1, 1, 1))
scene.set_directional_light((.4,1,.4), 0.1, (.4, .4, .4)) # direction, noise, color

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    pos = vec3(0, 0, 0)
    color = vec3(.2, .8, .5)
    scene.set_voxel(pos, 1, color)


initialize_voxels()

scene.finish()

from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.05, exposure=5)
scene.set_floor(-1.0, (.8, .8, .8)) # height, color
scene.set_background_color((1, 1, 1))
scene.set_directional_light((.4,1,.4), 0.1, (.4, .4, .4)) # direction, noise, color

@ti.func
def wave(): # Make a wave base for the scene
    for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        h = 7*ti.sin(ti.cast(i, ti.f32)/50*3.14)*ti.sin(ti.cast(j, ti.f32)/45*3.14)-35
        if k < h:
            scene.set_voxel(vec3(i,k,j), 1, (0.42,.62,1.))

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    wave()


initialize_voxels()

scene.finish()

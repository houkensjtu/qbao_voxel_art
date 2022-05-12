from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.05, exposure=5)
scene.set_floor(-1.0, (.8, .8, .8)) # height, color
scene.set_background_color((1, 1, 1))
scene.set_directional_light((.4,1,.4), 0.1, (.4, .4, .4)) # direction, noise, color

@ti.func
def sphere(pos, r, mat, color):
    # Place a sphere at pos with radius = r
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if (i-pos[0])**2 + (j-pos[1])**2 + (k-pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    pos = vec3(0, 0, 0)
    color = vec3(213./255, 255./255, 13./255)
    sphere(pos, 15, 1, color)


initialize_voxels()

scene.finish()

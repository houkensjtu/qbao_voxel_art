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
    # scene.set_voxel(vec3(0, 10, 0), 2, vec3(0.9, 0.1, 0.1))    # idx, mat, color
    for s in range(50): # Place 50 spheres
        # Randomly pick the position
        pos = [(ti.random()-0.5)*100, (ti.random()-0.5)*100, (ti.random()-0.5)*100]
        # Randomly set the radius and rgb color for each sphere
        sphere(pos, ti.random()*15 , 1, vec3(ti.random(), ti.random(), ti.random()))

        
initialize_voxels()

scene.finish()

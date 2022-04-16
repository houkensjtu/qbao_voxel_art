from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=10)
scene.set_floor(-1.0, (1.0, 1.0, 1.0)) # height, color
scene.set_background_color((1, 1, 1))
scene.set_direction_light((1,1,1), 0.1, (.3, .3, .3)) # direction, noise, color

@ti.func
def sphere(pos, r, mat, color):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if (i-pos[0])**2 + (j-pos[1])**2 + (k-pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.func
def box(pos, size, mat, color):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if ti.abs(i-pos[0]) < size[0] and ti.abs(j-pos[1]) < size[1] and ti.abs(k-pos[2]) < size[2]:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    # scene.set_voxel(vec3(0, 10, 0), 2, vec3(0.9, 0.1, 0.1))    # idx, mat, color
    for s in range(64):
        pos = [(ti.random()-0.5)*128, (ti.random()-0.5)*128, (ti.random()-0.5)*128]
        sphere(pos, ti.random()*15 , 1, vec3(ti.random(), ti.random(), ti.random()))

    for r in range(32):
        pos = [(ti.random()-0.5)*128, (ti.random()-0.5)*128, (ti.random()-0.5)*128]
        size = [ti.random()*10, ti.random()*10, ti.random()*10]
        box(pos, size, 1, vec3(ti.random(), ti.random(), ti.random()))

initialize_voxels()

scene.finish()

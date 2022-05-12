from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=4)
scene.set_floor(-1, (1., 1., 1.)) # height, color
scene.set_background_color((1., 1., 1.))
scene.set_directional_light((.8,1.,.8), 0.1, (.3, .3, .3)) # direction, noise, color

@ti.func
def sphere(pos, r, mat, color): # Make a sphere at pos with radius = r
    for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        if (i - pos[0])**2 + (j - pos[1])**2 + (k - pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.kernel
def initialize_voxels():
    for t in range(-64, 64):
        tt = ti.cast(t, ti.f32) / 16 * 3.14
        i = ti.cast(16 * ti.sin(tt), ti.i32)
        j = ti.cast(16 * ti.cos(tt), ti.i32)
        k = t
        sphere(vec3(i,k,j), 4, 1, vec3(240./255, 193./255, 255./255))

initialize_voxels()

scene.finish()

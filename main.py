from scene import Scene
import taichi as ti
from taichi.math import *

dark_mode = 0 # 0 for light-mode; 1 for dark-mode
scene = Scene(exposure=6)
scene.set_floor(-1, (1., 1., 1.)) # height, color
scene.set_background_color((1., 1., 1.))
if dark_mode:
    scene.set_directional_light((.8,1.,.8), 0.1, (.01, .01, .01)) # direction, noise, color
else:
    scene.set_directional_light((.8,1.,.8), 0.1, (.3, .3, .3)) # direction, noise, color
    
@ti.func
def sphere(pos, r, mat, color): # Make a sphere at pos with radius = r
    for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        if (i - pos[0])**2 + (j - pos[1])**2 + (k - pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,j,k), mat, color)
            
@ti.func
def box(pos, size, mat, color): # Make a box at pos
    for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        if ti.abs(i - pos[0]) <= size[0] / 2 and ti.abs(j - pos[1]) <= size[1] / 2 \
           and ti.abs(k - pos[2]) <= size[2] / 2:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.func
def wave(): # Make a wave base for the scene
    for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        h = 7*ti.sin(ti.cast(i, ti.f32)/50*3.14)*ti.sin(ti.cast(j, ti.f32)/45*3.14)-35
        if k < h and k > -63:
            scene.set_voxel(vec3(i,k,j), 1, (0.42,.62,1.))
            
@ti.func
def lighting_bulb(r, num, dark_mode): # Make num lighting bulbs of size r on the wave
    white = vec3(1., 1., 1.)
    black = vec3(0.15, 0.15, 0.15)
    for b in range(num):
        x = (128-2*r) * (ti.random() - 0.5)
        y = (128-2*r) * (ti.random() - 0.5)
        z = 7*ti.sin(ti.cast(x, ti.f32)/50*3.14)*ti.sin(ti.cast(y, ti.f32)/45*3.14)-35
        pos = vec3(x, z, y)
        if b % 2 == 0:
            if dark_mode:
                sphere(pos, r, 2, white)
            else:
                sphere(pos, r, 1, white)                
        else:
            sphere(pos, r, 1, black)

@ti.kernel
def initialize_voxels():
    r = 30
    white = vec3(1., 1., 1.) # Color must be floats
    black = vec3(0.1, 0.1, 0.1)
    for t in range(r): # Make the Taichi logo
        tt = ti.cast(t, ti.f32) / r * 3.14
        x = ti.cast(32 * ti.sin(tt), ti.i32)
        y = ti.cast(32 * ti.cos(tt), ti.i32) + r/2 + 10
        z = 0.
        if t == r-1:
            sphere(vec3(x,y,z), t*0.6, 1, white)
            if dark_mode:
                sphere(vec3(x,y,z+13), t*0.2, 2, white)
                sphere(vec3(x,y,z-13), t*0.2, 2, white)
            else:
                sphere(vec3(x,y,z+13), t*0.2, 1, black)
                sphere(vec3(x,y,z-13), t*0.2, 1, black)
        else:
            sphere(vec3(x,y,z), t*0.6, 1, white)
    for t in range(r): # Make the Taichi logo
        tt = ti.cast(t, ti.f32) / r * 3.14
        x = - ti.cast(32 * ti.sin(tt), ti.i32)
        y = - ti.cast(32 * ti.cos(tt), ti.i32)
        z = 0. 
        if t == r-1:
            sphere(vec3(x,y,z), t*0.6, 1, black)
            if dark_mode:
                sphere(vec3(x,y,z+13), t*0.2, 2, white)
                sphere(vec3(x,y,z-13), t*0.2, 2, white)
            else:
                sphere(vec3(x,y,z+13), t*0.2, 1, white)
                sphere(vec3(x,y,z-13), t*0.2, 1, white)
        else:
            sphere(vec3(x,y,z), t*0.6, 1, black)
    wave()
    if dark_mode:
        box(vec3(0,-63,0), [120.,1.,120.], 2, [1.,1.,1.])
    lighting_bulb(3, 32, dark_mode)

    
initialize_voxels()

scene.finish()

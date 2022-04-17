from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=10)
scene.set_floor(-1, (1.0, 1.0, 1.0)) # height, color
scene.set_background_color((1, 1, 1))
scene.set_directional_light((1,1,1), 0.1, (.3, .3, .3)) # direction, noise, color

@ti.func
def sphere(pos, r, mat, color): # pos: vec3, r: i32, mat: 0/1, color: list
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if (i-pos[0])**2 + (j-pos[1])**2 + (k-pos[2])**2 < r*r:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.func
def box(pos, size, mat, color):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if ti.abs(i-pos[0]) <= size[0]/2 \
           and ti.abs(j-pos[1]) <= size[1]/2 \
           and ti.abs(k-pos[2]) <= size[2]/2:
            scene.set_voxel(vec3(i,j,k), mat, color)

@ti.func
def chicken(pos): # pos: vec3
    white = [.4,.4,.4]
    grey  = [.2,.2,.2]
    black = [.05,.05,.05]    
    red   = [.25,.0,.0]
    yellow= [.4,.3,.0]    
    # Body
    box(vec3(0,0,0)+pos, vec3(10,10,10), 1, white)
    box(vec3(0,0,10)+pos, vec3(10,10,10), 1, white)
    box(vec3(0,10,10)+pos, vec3(10,10,10), 1, white)
    # Wings
    box(vec3(0,0,3)+pos, [15, 6, 15], 1, grey)  # Closed wings
    # box(vec3(0,0,3)+pos, [25, 2, 15], 1, grey)  # Flying wings
    # Eyes
    box(vec3(0,12,12)+pos, [10,2,2], 1, black)
    # Head
    box(vec3(0,16,11)+pos, [2,2,6], 1, red)
    # Beak
    box(vec3(0,10,16)+pos, [2,6,6], 1, yellow)
    # Legs
    box(vec3(-4,-8,5)+pos, [1,6,2], 1, red)
    box(vec3(3,-8,5)+pos, [1,6,2], 1, red)
    box(vec3(-4,-12,6)+pos, [4,1,12], 1, red)
    box(vec3(4,-12,6)+pos, [4,1,12], 1, red)        
            
            
@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    # scene.set_voxel(vec3(0, 10, 0), 2, vec3(0.9, 0.1, 0.1))    # idx, mat, color
    for c in range(80):
        pos = vec3((ti.random()-0.5)*120,((ti.random()-0.5)*120),(ti.random()-0.5)*120)
        chicken(pos)

initialize_voxels()

scene.finish()

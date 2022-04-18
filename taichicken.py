from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0.03, exposure=7)
scene.set_floor(-0.2, (1.0, 1.0, 1.0)) # height, color
scene.set_background_color((1, 1, 1))
scene.set_directional_light((1,1,1), 0.1, (.4, .4, .4)) # direction, noise, color


@ti.func
def box(pos, size, mat, color):
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if ti.abs(i-pos[0]) <= size[0]/2 \
           and ti.abs(j-pos[1]) <= size[1]/2 \
           and ti.abs(k-pos[2]) <= size[2]/2:
            scene.set_voxel(vec3(i,j,k), mat, color)

            
@ti.func
def chicken(pos): # pos: vec3
    white  = [.4,.4,.4]
    grey   = [.2,.2,.2]
    black  = [.05,.05,.05]    
    red    = [.25,.0,.0]
    yellow = [.4,.3,.0]    
    # Body
    box(vec3(0,0,0)+pos, vec3(10,10,10), 1, white)
    box(vec3(0,0,10)+pos, vec3(10,10,10), 1, white)
    box(vec3(0,10,10)+pos, vec3(10,10,10), 1, white)
    # Wings
    box(vec3(0,0,3)+pos, [15, 6, 15], 1, grey)  # Closed wings
    # box(vec3(0,0,3)+pos, [25, 2, 15], 1, grey)  # Flying wings
    # Eyes
    box(vec3(0,12,12)+pos, [10,2,2], 1, black)
    # Hat
    box(vec3(0,16,11)+pos, [2,2,6], 1, red)
    # Beak
    box(vec3(0,10,16)+pos, [2,6,6], 1, yellow)
    # Legs
    box(vec3(-4,-8,5)+pos, [1,6,2], 1, red)
    box(vec3(4,-8,5)+pos, [1,6,2], 1, red)
    box(vec3(-4,-12,6)+pos, [4,1,12], 1, red)
    box(vec3(4,-12,6)+pos, [4,1,12], 1, red)        
            
            
@ti.kernel
def initialize_voxels():
    chicken(vec3(0,0,0))

    
initialize_voxels()

scene.finish()

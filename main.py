from scene import Scene
import taichi as ti
from taichi.math import *
import numpy as np
scene = Scene(exposure=10)
scene.set_floor(-0.05, (1.0, 1.0, 1.0))
scene.set_background_color((1.0, 0, 0))
scene.set_direction_light((1,1,1), 0.1, (.2, 0.4,0.2))

@ti.kernel
def initialize_voxels():
    # Your code here! :-)
    # scene.set_voxel(vec3(0, 10, 0), 2, vec3(0.9, 0.1, 0.1))
    for i,j in ti.ndrange(50, 50):
        for k in range(50):
            ii = i - 25
            jj = j - 25
            kk = k - 25
            if (ii*ii + jj*jj + kk*kk < 300):
                scene.set_voxel(vec3(i, k, j), 1, vec3(0.1, .1, .1))


initialize_voxels()

scene.finish()

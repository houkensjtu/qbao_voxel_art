import taichi as ti
from taichi.math import *

ti.init(arch=ti.cpu)

@ti.kernel
def test_vector():
    v1 = vec3(1,2,2)
    v2 = vec3(0,0,0)    
    print('v1 =', v1)
    print('v2 =', v2)
    print('v1+v2 =', v1+v2)

    print('v1[0] =', v1[0])
    print('v1[1] =', v1[1])
    print('v1[2] =', v1[2])

    print('v1.x =', v1.x)
    print('v1.y =', v1.y)
    print('v1.z =', v1.z)

test_vector()          

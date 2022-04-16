import taichi as ti

ti.init(arch=ti.cpu) # print not working with Vulkan backend

@ti.kernel
def print_random():
    print('Print 10 ti.random(ti.i32)')
    for i in range(10):
        num = ti.random(ti.i32)
        print(num)
        
    print('Print 10 ti.random(ti.f32)')
    for i in range(10):
        num = ti.random(ti.f32)
        print(num)
        
    print('Print 10 ti.random()')
    for i in range(10):
        num = ti.random()
        print(num)


print_random()

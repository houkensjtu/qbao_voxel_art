import taichi as ti

ti.init(arch=ti.cpu) # print not working with Vulkan backend

@ti.kernel
def print_random():
    for i in range(10):
        num = ti.random(ti.i32)
        print(num)


print_random()

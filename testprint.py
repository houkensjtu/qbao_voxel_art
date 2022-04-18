import taichi as ti

ti.init(arch=ti.vulkan)
# ti.init(arch=ti.cpu)

@ti.kernel
def test_print():
    print('Inside the kernel.')
    
test_print()
print('Outside the kernel.')

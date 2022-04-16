import taichi as ti

ti.init(arch=ti.cpu)

@ti.kernel
def wave():
    for i,j,k in ti.ndrange((-64,64),(-64,64),(-64,64)):
        if k > 128*ti.sin(ti.cast(i, ti.f32) / 64 * 3.14)*128*ti.sin(ti.cast(j, ti.f32) / 64 * 3.14):
            print(i, j, k)
        


wave()        

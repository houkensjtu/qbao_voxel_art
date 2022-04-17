import taichi as ti

ti.init(arch=ti.cpu)

@ti.kernel
def testrange():
    print('Printing with range(10)')
    for i in range(10):
        print(i)

    print('Printing with range(2,10)')        
    for j in range(2,10):
        print(j)

    print('Printing with ti.ndrange(10)')
    for k in ti.ndrange(10):
        print(k)

    print('Printing with ti.ndrange((2,10))')
    for l in ti.ndrange((2,10)):
        print(l)


testrange()        

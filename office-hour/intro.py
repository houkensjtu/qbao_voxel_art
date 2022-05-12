slides = []

slides.append( """











    --------------------------------------------------------------------------------------------------------------      
 
                                                   体素挑战经验分享

                                                      2022/05/13
                                                         包乾

    --------------------------------------------------------------------------------------------------------------      








"""
)


slides.append( """


    1. 创建你的第一个体素
    --------------------------------------------------------------------------------------------------------------      


    -  创建一个场景
       scene = Scene(voxel_edges=0.05, exposure=5)

    -  在 (i,j,k) 位置放置一个体素
       scene.set_voxel(vec3(i,j,k), material, color)

 
       @ti.kernel
       def initialize_voxels():
           scene.set_voxel(vec3(0, 0, 0), material, vec3(1.0, 1.0, 1.0))



                                                                                                 +------+
                                                                                               .'     .'|
                                                                                              +------+  | 
                                                                                              |      |  +
                                                                                              |      |.' 
                                                                                              +------+


""")

slides.append( """


    2. 构造基本几何体
    --------------------------------------------------------------------------------------------------------------      


    -  用太极func构造一个球体

       # 遍历空间中的点 (i,j,k) 当其到原点距离小于r时, 放置一个体素

       @ti.func
       def sphere(pos, r, mat, color):
           for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
               if (i-pos[0])**2 + (j-pos[1])**2 + (k-pos[2])**2 < r*r:
                   scene.set_voxel(vec3(i,j,k), mat, color)
 
                                                                                                  ......::*o
       @ti.kernel                                                                              ...........:!*oe
       def initialize_voxels():                                                              .............:!*oee
           pos = vec3(0, 0, 0)                                                             ..............:!!*oeee
           color = vec3(213./255, 255./255, 13./255)                                       .............::!*ooeee
           sphere(pos, 15, 1, color)                                                       :...........:!!*ooeeee
                                                                                            *::....:::!!**ooeeeee
                                                                                             o*!!!!!***oooeeeeee
                                                                                              eooooooooeeeeeee
                                                                                                 eeeeeeeeee.

""")


slides.append( """


    3. 构造参数曲面
    --------------------------------------------------------------------------------------------------------------      


    -  考虑如下的一个参数曲面

       z(x,y) = sin(x) * sin(y)

       # 遍历空间中的点 (i,j,k) 当其高度小于 z(i,j) 时, 放置一个体素

       @ti.func
       def wave():
           for i,j,k in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
               h = 7 * ti.sin(ti.cast(i, ti.f32) / 50 * 3.14) * ti.sin(ti.cast(j, ti.f32) / 45 * 3.14) - 35
               if k < h:
                   scene.set_voxel(vec3(i,k,j), 1, (0.42,.62,1.))

      
       @ti.kernel
       def initialize_voxels():
           wave()




""")

slides.append( """


    4. 扫掠参数曲线
    --------------------------------------------------------------------------------------------------------------      


    -  考虑如下的参数曲线

       t = 1, 2, 3, 4 ...
       x = sin(t)
       y = cos(t)
       z = t

       # 沿着参数曲线上的点, 反复放置球体

       @ti.kernel
       def initialize_voxels():
           for t in range(-64, 64):
               tt = ti.cast(t, ti.f32) / 32 * 3.14
               x = ti.cast(16 * ti.sin(tt), ti.i32)
               y = t
               z = ti.cast(16 * ti.cos(tt), ti.i32)
               sphere(vec3(x,y,z), 4, 1, vec3(0., 224./255, 150./255))




""")

slides.append( """


    谢谢观看
    --------------------------------------------------------------------------------------------------------------      


    - RGB Color Picker: https://www.w3schools.com/colors/colors_rgb.asp

    - ASCII Art Archive: https://www.asciiart.eu/art-and-design/geometries


















""")

slide = iter(slides)

def nextslide(s):
  print(next(s))

def showslide(p):
    print(slides[p])

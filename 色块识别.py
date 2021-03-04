# 单颜色识别，RGB565模式

import sensor, image, time, math


red = (0,52,-128,127,21,127)  # 红色阈值
green =(0,100,-33,-48,-128,127)  # 绿色阈值
blue = (44,100,-128,127,-128,-25)  # 蓝色阈值


# 设置摄像头
sensor.reset()  # 初始化感光元件
sensor.set_pixformat(sensor.RGB565)  # 设置为彩色模式
sensor.set_framesize(sensor.QVGA)   # 设置图像的大小
sensor.skip_frames(time = 2000)
#sensor.set_auto_gain(False) # 关闭自动增益
#sensor.set_auto_whitebal(False) # 关闭白平衡
clock = time.clock()

x1_points = [[],[],[]]
x2_points = [[],[],[]]
while(True):
    clock.tick()
    img = sensor.snapshot()  # 拍摄一张照片，img为一个image对象
    for blob in img.find_blobs([red,green,blue],merge=False, pixels_threshold=200, area_threshold=200):

        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
        #print(blob.cy())
        if blob.code() == 1 and blob.cy() < 75:  # 红
            x1_points[0].append(blob.cx())

        if blob.code() == 2 and blob.cy() < 75:  # 绿
            x1_points[1].append(blob.cx())
        if blob.code() == 4 and blob.cy() < 75:  # 蓝
            x1_points[2].append(blob.cx())
        #print(blob.code())
        if blob.code() == 1 and blob.cy() > 75:  # 红
            x2_points[0].append(blob.cx())
        if blob.code() == 2 and blob.cy() >75:  # 绿
            x2_points[1].append(blob.cx())
        if blob.code() == 4 and blob.cy() > 75:  # 蓝
            x2_points[2].append(blob.cx())

        if len(x1_points[0]) > 0 and len(x1_points[1]) > 0 and len(x1_points[2]) > 0:
            r1x = sum(x1_points[0])/len(x1_points[0])
            g1x = sum(x1_points[1])/len(x1_points[1])
            b1x = sum(x1_points[2])/len(x1_points[2])

            if r1x<g1x and r1x<b1x and g1x<b1x:
                print(123)

            if r1x<b1x and b1x<g1x and r1x<g1x:
                print(132)

            if g1x<r1x and r1x<b1x and g1x<b1x:
                print(213)

            if g1x<b1x and b1x<r1x and g1x<r1x:
                print(231)

            if b1x<g1x and g1x<r1x and b1x<r1x:
                print(321)

            if b1x<r1x and r1x<g1x and b1x<g1x:
                print(312)

        if len(x2_points[0]) > 0 and len(x2_points[1]) > 0 and len(x2_points[2]) > 0:
            r2x = sum(x2_points[0])/len(x2_points[0])
            g2x = sum(x2_points[1])/len(x2_points[1])
            b2x = sum(x2_points[2])/len(x2_points[2])

            if r2x<g2x and r2x<b2x and g2x<b2x:
                print(123)

            if r2x<b2x and b2x<g2x and r2x<g2x:
                print(132)

            if g2x<r2x and r2x<b2x and g2x<b2x:
                print(213)

            if g2x<b2x and b2x<r2x and g2x<r2x:
                print(231)

            if b2x<g2x and g2x<r2x and b2x<r2x:
                print(321)

            if b2x<r2x and r2x<g2x and b2x<g2x:
                print(312)





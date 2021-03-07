# 单颜色识别，RGB565模式

import sensor, image, time, math
from pyb import UART
import pyb

red = (0, 100, 4, 127, 24, 127)  # 红色阈值
green =(0,100,-33,-48,-128,127)  # 绿色阈值
blue = (0, 43, -128, 127, -9, -32)  # 蓝色阈值


# 设置摄像头
sensor.reset()  # 初始化感光元件
sensor.set_pixformat(sensor.RGB565)  # 设置为彩色模式
sensor.set_framesize(sensor.QVGA)   # 设置图像的大小
sensor.skip_frames(time = 2000)
#sensor.set_auto_gain(False) # 关闭自动增益
#sensor.set_auto_whitebal(False) # 关闭白平衡

def sekuai():
    rl = []
    gl = []
    bl = []
    while(True):
        rl.clear()
        gl.clear()
        bl.clear()
        img = sensor.snapshot()  # 拍摄一张照片，img为一个image对象
        for blob in img.find_blobs([red,green,blue],merge=False, pixels_threshold=200, area_threshold=200):

            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            if blob.code() == 1:  # 红
                #rl.append(blob.cy())
                rl.append(blob.cx())
            if blob.code() == 2:  # 绿
                #gl.append(blob.cy())
                gl.append(blob.cx())
            if blob.code() == 4:  # 蓝
                #bl.append(blob.cy())
                bl.append(blob.cx())

        if len(rl) == 1 and len(gl) == 1 and len(bl) == 1:
            #if rl[0] < rl[2]:
                #rux = rl[1]
                #rdx = rl[3]
            #else:
                #rux = rl[3]
                #rdx = rl[1]
            #if gl[0] < gl[2]:
                #gux = gl[1]
                #gdx = gl[3]
            #else:
                #gux = rl[3]
                #gdx = rl[1]
            #if bl[0] < bl[2]:
                #bux = bl[1]
                #bdx = bl[3]
            #else:
                #bux = rl[3]
                #bdx = rl[1]
            rux = rl[0]
            gux = gl[0]
            bux = bl[0]
            uart1 = UART(3, 115200)
            if gux < bux and bux < rux and gux < rux:
                uart1.write("123\n")
            if rdx < bdx and bdx < gdx and rdx < gdx:
                uart1.write("312\n")
            if rux < bux and bux < gux and rux < gux:
                uart1.write("132\n")
            if gux < rux and rux < bux and gux < bux:
                uart1.write("213\n")
            if gux < bux and bux < rux and gux < rux:
                uart1.write("231\n")
            if bux < gux and gux < rux and bux < rux:
                uart1.write("321\n")


uart = UART(3, 115200)
while(True):
    if uart.any():
        a = uart.read().decode()
        if a == "start!":
            #print(a)
            led1 = pyb.LED(1)
            led1.on()
            time.sleep_ms(150)
            led1.off()
            led1.on()
            time.sleep_ms(150)
            led1.off()
            uart.write("123\n")







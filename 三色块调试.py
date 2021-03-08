# 单颜色识别，RGB565模式

import sensor, image, time, math
from pyb import UART
import pyb

red = (0, 100, 4, 127, 24, 127)  # 红色阈值
green =(0, 100, -128, -22, -128, 127) # 绿色阈值
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
        for blob in img.find_blobs([red,green,blue],merge=False, pixels_threshold=600, area_threshold=1100):

            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            if blob.code() == 1:  # 红
                #rl.append(blob.cy())
                rl.append(blob.cx())
                #print("hong")
                #print(blob.area())
            if blob.code() == 2:  # 绿
                #gl.append(blob.cy())
                #print("lv")
                gl.append(blob.cx())
                #print(blob.area())
            if blob.code() == 4:  # 蓝
                #bl.append(blob.cy())
                bl.append(blob.cx())
                #print("lan")
                #print(blob.area())


        if len(rl) == 1 and len(gl) == 1 and len(bl) == 1:
            rux = rl[0]
            gux = gl[0]
            bux = bl[0]
            #uart1 = UART(3, 115200)
            if gux < bux and bux < rux and gux < rux:
                #uart1.write("123\n")
                return "231"
            if bux < rux and rux < gux and bux < gux:
                #uart1.write("312\n")
                return "312"
            if rux < gux and gux < bux and rux < bux:
                #uart1.write("132\n")
                return "123"
            if gux < rux and rux < bux and gux < bux:
                #uart1.write("213\n")
                return "213"
            if rux < bux and bux < gux and rux < gux:
                #uart1.write("231\n")
                return "123"
            if bux < gux and gux < rux and bux < rux:
                #uart1.write("321\n")
                return "321"

led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
uart = UART(3, 115200)
while(True):
    if uart.any():
        a = uart.read().decode()
        if a == "start!":

            led1.on()
            time.sleep_ms(250)
            led2.on()
            time.sleep_ms(250)
            led2.off()
            led1.off()
            led1.on()
            time.sleep_ms(250)
            led2.on()
            time.sleep_ms(250)
            led2.off()
            led1.off()
            str_uart = sekuai()
            uart.write(str_uart)
            led1.on()
            time.sleep_ms(250)
            led2.on()
            time.sleep_ms(250)
            led2.off()
            led1.off()
            led1.on()
            time.sleep_ms(250)
            led2.on()
            time.sleep_ms(250)
            led2.off()
            led1.off()






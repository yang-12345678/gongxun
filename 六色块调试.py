# 单颜色识别，RGB565模式

import sensor, image, time, math
from pyb import UART
import pyb

red = (0, 19, 3, 127, -128, 127)  # 红色阈值
green =(0, 36, -128, -29, -128, 127) # 绿色阈值
blue = (15, 37, -15, 127, -128, -13)  # 蓝色阈值


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
        number = 0
        rl.clear()
        gl.clear()
        bl.clear()
        img = sensor.snapshot()  # 拍摄一张照片，img为一个image对象
        for blob in img.find_blobs([red,green,blue],merge=False, pixels_threshold=130, area_threshold=265):

            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            if blob.code() == 1:  # 红
                rl.append(blob.cy())
                rl.append(blob.cx())
            if blob.code() == 2:  # 绿
                gl.append(blob.cy())
                gl.append(blob.cx())
            if blob.code() == 4:  # 蓝
                bl.append(blob.cy())
                bl.append(blob.cx())

        if len(rl) == 4 and len(gl) == 4 and len(bl) == 4:
            if rl[0] < rl[2]:
                rux = rl[1]
                rdx = rl[3]
            else:
                rux = rl[3]
                rdx = rl[1]
            if gl[0] < gl[2]:
                gux = gl[1]
                gdx = gl[3]
            else:
                gux = rl[3]
                gdx = rl[1]
            if bl[0] < bl[2]:
                bux = bl[1]
                bdx = bl[3]
            else:
                bux = rl[3]
                bdx = rl[1]

            uart1 = UART(3, 19200)
            str=""
            # 123
            if rux < gux and gux < bux and rux < bux:
                str+="123"
            if rdx < gdx and gdx < bdx and rdx < bdx:
                str+="123\n"
            # 132
            if rux < bux and bux < gux and rux < gux:
                str+="132"
            if rdx < bdx and bdx < gdx and rdx < gdx:
                str+="132\n"
            # 213
            if gux < rux and rux < bux and gux < bux:
                str+="213"
            if gdx < rdx and rdx < bdx and gdx < bdx:
                str+="213\n"
            # 231
            if gux < bux and bux < rux and gux < rux:
                str+="231"
            if gdx < bdx and bdx < rdx and gdx < rdx:
                str+="231\n"
            # 312
            if bux < rux and rux < gux and bux < gux:
                str+="312"
            if bdx < rdx and rdx < gdx and bdx < gdx:
                str+="312\n"
            # 321
            if bux < gux and gux < rux and bux < rux:
                str+="321"
            if bdx < gdx and gdx < rdx and bdx < rdx:
                str+="321\n"
            return str
        else:
            i+=1
            time.sleep_ms(1000)
        if i > 5:
            print("*********")
            return "213+213"

uart = UART(3, 19200)
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






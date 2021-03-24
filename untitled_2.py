# 单颜色识别，RGB565模式

import sensor, image, time, math
from pyb import UART
import pyb


red = (0, 100, -5, 127, 9, 127) # 红色阈值
#green = (0, 32, -41, -22, -128, 32) # 绿色阈值
blue = (0, 56, -10, 10, -128, -12)  # 蓝色阈值


# 设置摄像头
sensor.reset()  # 初始化感光元件
sensor.set_pixformat(sensor.RGB565)  # 设置为彩色模式
sensor.set_framesize(sensor.QVGA)   # 设置图像的大小
sensor.skip_frames(time = 800)
#sensor.set_auto_gain(False) # 关闭自动增益
#sensor.set_auto_whitebal(False) # 关闭白平衡

right = 258
left = 140
leng = 120
short = 65

def sekuai():
    rl = []
    bl = []
    while(True):

        rl.clear()
        bl.clear()
        img = sensor.snapshot()  # 拍摄一张照片，img为一个image对象
        for blob in img.find_blobs([red,blue],merge=False, pixels_threshold=180, area_threshold=180):

            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            if blob.code() == 1:  # 红
                #print("hong")
                rl.append(blob.cy())
                rl.append(blob.cx())
                #print(blob.cx())
            if blob.code() == 2:  # 蓝
                #print(blob.cx())
                #print("lan")
                bl.append(blob.cy())
                bl.append(blob.cx())

            if len(rl) == 4 and len(bl) == 4:
                if rl[0] < rl[2]:
                    rx = rl[1]
                else:
                    rx = rl[3]

                if bl[0] < bl[2]:
                    bx = bl[1]
                else:
                    bx = bl[3]

                x = bx - rx
                #print(x)

                if (x in range(leng-20, leng+20)) and x > 0:
                    return "123\n"
                    print(123)
                if (-x in range(leng-20, leng+20)) and x < 0:
                    return "321\n"
                    print(321)
                if x < 0 and ((-x) in range(short-40, short + 40)) and (rx in range(right-30, right+30)):
                    return "231\n"
                    print(231)
                if x < 0 and ((-x) in range(short-40, short + 40)) and (bx in range(left-30, left+30)):
                    return "312\n"
                    print(312)
                if x > 0 and (x in range(short-40, short + 40)) and (rx in range(left-30, left+30)):
                    return "132\n"
                    print(132)
                if x > 0 and (x in range(short-20, short + 20)) and (bx in range(right-30, right+30)):
                    print(213)
                    return "213\n"



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
#while True:
    #sekuai()




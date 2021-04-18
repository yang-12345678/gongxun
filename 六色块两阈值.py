# 单颜色识别，RGB565模式

import sensor, image, math
import time
from pyb import UART
import pyb

# 上层
red = (0, 33, 32, 127, -128, 127)  # 红色阈值
green = (0, 100, -128, -21, -128, 127)  # 绿色阈值
blue = (0, 45, -128, 12, -128, -30)  # 蓝色阈值

# 下层
red1 = (0, 33, 32, 127, -128, 127)  # 红色阈值
green1 = (0, 100, -128, -21, -128, 127)  # 绿色阈值
blue1 = (0, 45, -128, 12, -128, -30)

# ROI
roiu = (75, 56, 186, 54)
roid = (75, 150,186,54)

# 设置摄像头
sensor.reset()  # 初始化感光元件
sensor.set_pixformat(sensor.RGB565)  # 设置为彩色模式
sensor.set_framesize(sensor.QVGA)  # 设置图像的大小
# sensor.set_windowing((640, 80))
sensor.skip_frames(time=800)


# sensor.set_auto_gain(False) # 关闭自动增益
# sensor.set_auto_whitebal(False) # 关闭白平衡


def sekuai():
    rlu = []
    glu = []
    blu = []
    rld = []
    gld = []
    bld = []
    # 标志
    flagu = 0
    flagd = 0
    i = 0
    while (True):
        rlu.clear()
        glu.clear()
        blu.clear()
        rld.clear()
        gld.clear()
        bld.clear()
        img = sensor.snapshot()  # 拍摄一张照片，img为一个image对象
        # 上层
        img.draw_rectangle(roiu)
        img.draw_rectangle(roid)
        for blob in img.find_blobs([red, green, blue], merge=False, pixels_threshold=200, area_threshold=200, roi=roiu):

            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            if blob.code() == 1:  # 红

                rlu.append(blob.cx())

                print("hong")
                print(blob.area())
                print(blob.pixels())
            if blob.code() == 2:  # 绿

                print("lv")

                glu.append(blob.cx())

                print(blob.area())
                print(blob.pixels())
            if blob.code() == 4:  # 蓝

                blu.append(blob.cx())

                print("lan")
                print(blob.area())
                print(blob.pixels())

        if len(rlu) == 1 and len(glu) == 1 and len(blu) == 1 and flagu == 0:
            rux = rlu[0]
            gux = glu[0]
            bux = blu[0]
            flagu = 1

            if gux < bux and bux < rux and gux < rux:
                str_temp = "231"

            if bux < rux and rux < gux and bux < gux:
                str_temp = "312"

            if rux < gux and gux < bux and rux < bux:

                str_temp = "123\n"
            if gux < rux and rux < bux and gux < bux:

                str_temp = "213\n"
            if rux < bux and bux < gux and rux < gux:

                str_temp = "132\n"
            if bux < gux and gux < rux and bux < rux:
                str_temp = "321\n"

        # 下层
        for blob in img.find_blobs([red1, green1, blue1], merge=False, pixels_threshold=200, area_threshold=200,roi=roid):

            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())

            if blob.code() == 1:  # 红

                rld.append(blob.cx())

                print("hong")
                print(blob.area())
                print(blob.pixels())
            if blob.code() == 2:  # 绿

                print("lv")

                gld.append(blob.cx())
                print(blob.area())
                print(blob.pixels())
            if blob.code() == 4:  # 蓝

                bld.append(blob.cx())

                print("lan")
                print(blob.area())
                print(blob.pixels())

        if len(rld) == 1 and len(gld) == 1 and len(bld) == 1 and flagd == 0:
            rdx = rld[0]
            gdx = gld[0]
            bdx = bld[0]
            flagd = 1

            if gdx < bdx and bdx < rdx and gdx < rdx:
                str_temp += "+231\n"

            if bdx < rdx and rdx < gdx and bdx < gdx:
                str_temp += "+312\n"

            if rdx < gdx and gdx < bdx and rdx < bdx:

                str_temp += "+123\n"
            if gdx < rdx and rdx < bdx and gdx < bdx:

                str_temp += "+213\n"
            if rdx < bdx and bdx < gdx and rdx < gdx:

                str_temp += "+132\n"
            if bdx < gdx and gdx < rdx and bdx < rdx:
                str_temp += "+321\n"

        if flagu == 1 and flagd == 1:
            return str_temp
        else:
            i = i + 1
            time.sleep(1000)
        if i > 5:
            print("**************")
            return "213+123\n"


led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)
uart = UART(3, 115200)
#while (True):
    #if uart.any():
        #a = uart.read().decode()
        #if a == "start!":
            #led1.on()
            #time.sleep_ms(250)
            #led2.on()
            #time.sleep_ms(250)
            #led2.off()
            #led1.off()
            #led1.on()
            #time.sleep_ms(250)
            #led2.on()
            #time.sleep_ms(250)
            #led2.off()
            #led1.off()
            #str_uart = sekuai()
            #uart.write(str_uart)
            #led1.on()
            #time.sleep_ms(250)
            #led2.on()
            #time.sleep_ms(250)
            #led2.off()
            #led1.off()
            #led1.on()
            #time.sleep_ms(250)
            #led2.on()
            #time.sleep_ms(250)
            #led2.off()
            #led1.off()
while True:
    print(sekuai())

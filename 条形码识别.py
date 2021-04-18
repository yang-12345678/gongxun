import sensor, image, time, math
from pyb import UART
import pyb

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA) # High Res!
#sensor.set_windowing((640, 80)) # V Res of 80 == less work (40 for 2X the speed).
sensor.skip_frames(30)
clock = time.clock()

roi1= (0,203,660,111) # 上
roi2= (2,2,2,2) # 下
#roi3= (,,,)  # 上右

flagu = 0
flagd = 0

one = []
two = []
three = []

oned = []
twod = []
threed = []


def cenx(tu):
    x = tu[0]
    y = tu[1]
    w = tu[2]
    h = tu[3]
    cx = x + w/2
    cy = y + h/2
    return cx,cy

def barcode_name(code):
    if(code.type() == image.EAN2):
        return "EAN2"
    if(code.type() == image.EAN5):
        return "EAN5"
    if(code.type() == image.EAN8):
        return "EAN8"
    if(code.type() == image.UPCE):
        return "UPCE"
    if(code.type() == image.ISBN10):
        return "ISBN10"
    if(code.type() == image.UPCA):
        return "UPCA"
    if(code.type() == image.EAN13):
        return "EAN13"
    if(code.type() == image.ISBN13):
        return "ISBN13"
    if(code.type() == image.I25):
        return "I25"
    if(code.type() == image.DATABAR):
        return "DATABAR"
    if(code.type() == image.DATABAR_EXP):
        return "DATABAR_EXP"
    if(code.type() == image.CODABAR):
        return "CODABAR"
    if(code.type() == image.CODE39):
        return "CODE39"
    if(code.type() == image.PDF417):
        return "PDF417"
    if(code.type() == image.CODE93):
        return "CODE93"
    if(code.type() == image.CODE128):
        return "CODE128"
s = ''
def func():
    global flagu
    flagu = 0
    global flagd
    flagd = 0
    global s
    s = ''
    k = 0
    while(True):
        if flagu == 0 and flagd == 0:
            s = ''

        one.clear()
        two.clear()
        three.clear()
        oned.clear()
        twod.clear()
        threed.clear()
        i = 0
        j = 0

        img = sensor.snapshot()
        img.draw_rectangle(roi1)
        img.draw_rectangle(roi2)
        codes = img.find_barcodes(roi1)
        codess = img.find_barcodes(roi2)
        # 上层
        for code in codes:
            img.draw_rectangle(code.rect())
            # 数据类型 有效载值 旋度 次数
            #print_args = (barcode_name(code), code.payload(), (180 * code.rotation()) / math.pi, code.quality(), clock.fps())
            #print("Barcode %s, Payload \"%s\", rotation %f (degrees), quality %d, FPS %f" % print_args)
            if code.payload() == '1':
                one.append(cenx(code.rect())[0])
                i+=1
            if code.payload() == '2':
                two.append(cenx(code.rect())[0])
                i+=1
            if code.payload() == '3':
                three.append(cenx(code.rect())[0])
                i+=1

        if i == 3 and flagu == 0:
            u1 = one[0]
            u2 = two[0]
            u3 = three[0]
            if min(u1,u2,u3) == u1:
                if u2 < u3:
                   s =  "123" + s
                   flagu = 1
                else:
                   s = "132" + s
                   flagu = 1
            elif min(u1, u2, u3) == u2:
                if u1 < u3:
                   s = "213" + s
                   flagu = 1
                else:
                   s = "231" + s
                   flagu = 1
            else:
                if u1 < u2:
                   s = "312" + s
                   flagu = 1
                else:
                   s = "321" + s
                   flagu = 1

        #if i == 2 and flagu == 0:
            #if len(one) == 0:


        # 下层
        for code in codess:
            img.draw_rectangle(code.rect())
            # 数据类型 有效载值 旋度 次数
            #print_args = (barcode_name(code), code.payload(), (180 * code.rotation()) / math.pi, code.quality(), clock.fps())
            #print("Barcode %s, Payload \"%s\", rotation %f (degrees), quality %d, FPS %f" % print_args)
            if code.payload() == '1':
                oned.append(cenx(code.rect())[0])
                j+=1
            if code.payload() == '2':
                twod.append(cenx(code.rect())[0])
                j+=1
            if code.payload() == '3':
                threed.append(cenx(code.rect())[0])
                j+=1

        if j == 3 and flagd == 0:
            u1 = oned[0]
            u2 = twod[0]
            u3 = threed[0]
            if min(u1,u2,u3) == u1:
                if u2 < u3:
                   s +=  "123"
                   flagd = 1
                else:
                   s += "132"
                   flagd = 1
            elif min(u1, u2, u3) == u2:
                if u1 < u3:
                   s += "213"
                   flagd = 1
                else:
                   s += "231"
                   flagd = 1
            else:
                if u1 < u2:
                   s += "312"
                   flagd = 1
                else:
                   s += "321"
                   flagd = 1

        if flagu and flagd:
            return s
        else:
            k += 1
            time.sleep_ms(500)
        if k == 10:
            if flagu and flagd == 0:
                return s + "213"
            if flagu == 0 and flagd:
                return "213" + s
            if flagu == 0 and flagd == 0:
                return "213" + "132"

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
            str_uart = func()
            uart.write(str_uart)
            #print(str_uart)
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
    #print(func())

'''
跳一跳手动辅助脚本
'''

import subprocess
import random
import time
import PIL
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

need_update = True

def get_screen():
    '''
    获取屏幕截图
    '''

    subprocess.run('adb shell screencap -p > auto.png',shell=True)
    # subprocess.run('adb pull /sdcard/auto.png',shell=True)
    # 返回图片数据
    return numpy.array(PIL.Image.open('auto.png'))

def jump_to_next(coor1,coor2):
    '''
    计算两点之间的距离，并跳跃
    '''

    x1,y1 = coor1; x2,y2 = coor2
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    subprocess.run('adb shell input swipe {0} {1} {0} {1} {2}'.format(random.randint(300,500),\
    random.randint(1350,1550),int(distance*1.35)),shell=True)
    

def onclick(envent,coor=[]):
    '''
    点击的时候，添加点击的坐标；当开始坐标和结束坐标都点了的时候，进行跳跃
    '''

    global need_update
    coor.append((envent.xdata,envent.ydata))
    if len(coor)==2:
        jump_to_next(coor.pop(),coor.pop())
        need_update = True

def update_screen(frame,axes_image):
    # 利用这个方法直接刷新图片
    global need_update
    if need_update:
        # 延迟1秒，等待跳完
        time.sleep(1)
        axes_image.set_array(get_screen())
        need_update = False
    return axes_image,



def operation(img):
    '''操作函数，进行跳跃'''

    # 创建一个空白的图片对象
    figure = plt.figure()
    # 把图片放进坐标轴
    axes_image = plt.imshow(img,animated=True)
    # 给点击图片添加事件，调用onclick函数进行处理
    figure.canvas.mpl_connect('button_press_event',onclick)
    # 刷新图片
    # figure:刷新的对象，update_screen：执行的动作
    ani = FuncAnimation(figure,update_screen,interval=50,blit=True,fargs=(axes_image,))
    # 显示整个图片对象
    plt.show()


def run():
    # 获取屏幕截图
    img = get_screen()

    # 进行操作
    operation(img)


if __name__ == '__main__':
    print("脚本正在运行...")
    run()
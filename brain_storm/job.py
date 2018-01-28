import time
import subprocess

# 点击时间设置
click_time = 4.5
next_cycle_time = 8

def auto_touch(op):
    '''
    自到寻找最优答案，选择答案
    '''
    # stand_answer = 3
    # max_count = 0
    # for i,j in enumerate(op):
    #     if j > max_count:
    #         max_count = j
    #         stand_answer = i+1
    stand_answer = op.index(max(op))+1

    click(stand_answer)
    

def next_cycle():
    '''
    一轮结束后，点击下一轮
    '''
    time.sleep(next_cycle_time)
    subprocess.run("adb shell input swipe 520 1400 520 1400 1",shell=True)
    # subprocess.run("adb shell input swipe 520 800 520 800 1",shell=True)


def click(num):
    '''
    点击答案
    '''
    time.sleep(click_time)
    subprocess.run("adb shell input swipe 520 {0} 520 {0} 1".format(200*num+840),shell=True)
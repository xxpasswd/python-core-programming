import sys
import os
import schedule
import time
import yaml
import threading


conf_file = 'loglog'

def check_conf_change(filename):
    mtime = lambda p: os.stat(p).st_mtime
    lmtime = None
    if lmtime is None:
        lmtime = mtime(filename)
    
    def check(filename):
        nonlocal lmtime
        if mtime(filename) > lmtime:
            lmtime = mtime(filename)
            return True
        return False
    return check


def run():
    c = ScheduleTask()
    threading.Thread(target=c.auto_run).start()
    change = check_conf_change(conf_file)
    while True:
        time.sleep(1)
        if change(conf_file):
            print('restart ...')
            c.restart()


class ScheduleTask:
    def __init__(self):
        self.stop = False

    def auto_run(self):
        while True:
            self.run()

    def run(self):
        schedule.clear()
        self.get_tasks()
        while True:
            schedule.run_pending()
            time.sleep(1)
            if self.stop:
                self.stop = False
                break

    def restart(self):
        self.stop = True

    def get_tasks(self):
        self.parser_conf()

    def parser_conf(self):
        f = open('loglog', 'r')
        content = yaml.load(f)
        for i in content.values():
            schedule.every().day.at(i).do(job)


def job():
    print('aaa')


run()


"""
master-worker模式的一个简单示例
"""
import sys
import os


def run():
    import subprocess
    import time

    if not os.environ.get('MASTER_PID'): # master
        while True:
            env = os.environ.copy()
            env['MASTER_PID'] = str(os.getpid())
            args = [sys.executable] + sys.argv
            p = subprocess.Popen(args, env=env)
            while p.poll() is None:
                time.sleep(2)
        return

    print(os.environ.get('MASTER_PID'))
    time.sleep(5)

run()
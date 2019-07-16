"""
整体思路：
使用一个主进程用来不断生成子进程（入口函数需要判断子进程和主进程，子进程执行子进程代码，主进程执行主进程代码）

参考了django的autoreload的机制
"""
import subprocess
import sys
import threading
import os
import time


def run_with_reloader(main_fun, *args, **kwargs):
	if os.environ.get('AUTOLOAD_ENV') == 'true':
		# 子进程会执行这个分支，主进程会执行下面的分支
		reloader = StatReloader('main.txt')
		print('start')
		run_fun(reloader, main_fun, *args, **kwargs)
	else:
		restart_with_reloader()


def restart_with_reloader():
	args = [sys.executable] + sys.argv
	new_environ = {**os.environ, 'AUTOLOAD_ENV': 'true'}
	while True:
		exit_code = subprocess.call(args, env=new_environ)


def run_fun(reloader, main_fun, *args, **kwargs):
	main_thread = threading.Thread(target=main_fun, args=args, kwargs=kwargs, name='main_thread')
	main_thread.setDaemon(True)
	main_thread.start()

	reloader.run_loop()


class StatReloader:
	"""
	文件修改后，退出
	"""
	def __init__(self, file_path):
		self.file_path = file_path

	def run_loop(self):
		old_time = None
		mtime = lambda p: os.stat(p).st_mtime
		while True:
			if old_time is None:
				# file first seen time
				old_time = mtime(self.file_path)
				continue
			elif mtime(self.file_path) > old_time:
				sys.exit(3)
			time.sleep(1)


def test_fun():
	print('test')


if __name__ == '__main__':
	run_with_reloader(test_fun)
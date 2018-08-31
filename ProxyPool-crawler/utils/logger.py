# coding: utf-8
import logging
from os.path import abspath, dirname, join
from os import mkdir

base_dir = dirname(dirname(abspath(__file__)))
try:
    mkdir(join(base_dir, 'log'))
except:
    pass
log_file = join(base_dir, 'log/all.log')

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s :: %(lineno)d] %(funcName)s : %(message)s')

# consle handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# 文件 handler
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

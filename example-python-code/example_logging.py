import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(pathname)s %(filename)s [line:%(lineno)s] %(levelname)s %(message)s',
                    filename='/tmp/test.log',
                    filemode='w')

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

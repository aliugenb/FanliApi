# -*- coding: utf-8 -*-
# __author__ = Roger
import logging
import logging.config

logging.config.fileConfig("logging.conf")  # 采用配置文件

# create logger
logger = logging.getLogger("simpleExample")

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

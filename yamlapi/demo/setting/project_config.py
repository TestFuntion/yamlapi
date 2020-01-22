"""
整个工程的配置文件
"""

import os
import sys
import time

from loguru import logger

parameter = sys.argv[1]
# 从命令行获取参数

environment = os.getenv("measured_environment", parameter)
# 环境变量

if environment == "dev":
    service_domain = "http://www.dev.com"
    # 开发环境
    db_host = 'mysql.dev.com'
    db_port = 3306
elif environment == "test":
    service_domain = "http://www.test.com"
    # 测试环境
    db_host = 'mysql.test.com'
    db_port = 3307
elif environment == "pre":
    service_domain = "http://www.pre.com"
    # 预生产环境
    db_host = 'mysql.pre.com'
    db_port = 3308
elif environment == "formal":
    service_domain = "https://www.formal.com"
    # 生产环境
    db_host = None
    db_port = None

db_user = 'root'
db_password = '123456'
db_database = ''
# MySQL数据库配置


current_path = os.path.dirname(os.path.dirname(__file__))
# 获取当前目录的父目录的绝对路径
# 也就是整个工程的根目录
case_path = os.path.join(current_path, "case")
# 测试用例的目录
yaml_path = os.path.join(current_path, "resource")
# yaml文件的目录
today = time.strftime("%Y-%m-%d", time.localtime())
# 年月日

report_path = os.path.join(current_path, "report")
# 测试报告的目录
if os.path.exists(report_path):
    pass
else:
    os.mkdir(report_path, mode=0o777)

log_path = os.path.join(current_path, "log")
# 日志的目录
if os.path.exists(log_path):
    pass
else:
    os.mkdir(log_path, mode=0o777)

logging_file = os.path.join(log_path, "log{}.log".format(today))

logger.add(
    logging_file,
    format="{time:YYYY-MM-DD HH:mm:ss}|{level}|{message}",
    level="INFO",
    rotation="500 MB",
    encoding="utf-8",
)
# loguru日志配置
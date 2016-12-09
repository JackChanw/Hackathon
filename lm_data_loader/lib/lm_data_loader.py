#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import logging.config
import datetime
import argparse

# 处理str时unicodeEncodeERROR问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 获取默认的运行时路径，并设置运行时需要加到sys.path的模块
exePath = os.path.realpath(os.path.dirname(__file__))
basepath = os.path.realpath(os.path.dirname(__file__) + "/../")
sys.path.append(exePath)



if __name__ == "__main__":
    # ================= 命令行参数解析 ===================
    ap = argparse.ArgumentParser(description = "dsa_daily_report service")
    # -d，即指定该模块的运行时目录
    ap.add_argument("-d", "--executeDir", type = str,
            help = "dsa_daily_report service execute directory",
            default = basepath)
    # -t，即目标时间，格式为%Y-%m-%d %H:%M:%S，例如2014-08-27 12:00:00
    ap.add_argument("-t", "--timestamp", type = str,
            help = "",
            default = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    args = ap.parse_args()

    os.chdir(args.executeDir)
    print "Run lm_data_loader at %s" % args.executeDir

    sys.path.append("conf")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.conf import settings
    # ===================================================
    # Let's rock 'n roll!
    from lm_data_loader_service import LmDataLoaderService
    lml = LmDataLoaderService()
    lml.run()


# -*- coding: utf-8 -*-

import logging
import time
import signal
import sys
from Queue import Queue
import threading
from datetime import datetime, timedelta

from topic_loader.topic_loader import TopicLoader
from topic_loader.topic_writer import TopicWriter

GLOBAL_RUNNING=True

class LmDataLoaderService(object):
	'''
	LmDataLoader Service
	'''
	def __init__(self):
		# 正常的运行时日志Logger
		self.logger = logging.getLogger('domob.lightmoon')
		self.running = False
		self.initSignalHandler()
		self.queue = Queue()
		self.topic_loader = TopicLoader(self.queue)
		self.topic_writer = TopicWriter(self.queue)

	# 删除不需要处理的信号，以及增加需要处理的信号
	# 并且设置不同的处理方法
	# 这里默认处理了SIGTERM和SIGINT，并且尝试停止service
	# SIGINT = 2，可使用kill -2 pid 或 当CTRL+C终止程序时发出
	# SIGTERM = 15，可使用kill -15 pid发出
	def initSignalHandler(self):
		signals = (signal.SIGTERM, signal.SIGINT)
		self.signalHandlers = {}
		for sig in signals:
			self.signalHandlers[sig] = signal.getsignal(sig)
			signal.signal(sig, self.handleSignal)

	def handleSignal(self, signal, frame):
		self.logger.info('Handle signal %d, stop service', signal)
		self.logger.info('Try to stop all workers.')
		self.stop()
		self.logger.info('Bye-bye.')
		sys.exit(0)

	def run(self):
		'''
		实时将kafka的数据取出
		然后通过iploader查询需要的ip地址经纬度
		形成kafka数据，放入kafka
		'''
		print 'Hackathon Good Luck!'
		reader = threading.Thread(target=self.topic_loader.run)
		reader.daemon = True
		writer = threading.Thread(target=self.topic_writer.run)
		writer.daemon = True
		writer.start()
		reader.start()
		writer.join()
		reader.join()

	def stop(self):
		self.logger.info('Lmdataloader service will stop.')
		GLOBAL_RUNNING=False
		self.running = False

# vim: set noexpandtab ts=4 sts=4 sw=4 :

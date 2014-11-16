# -*- coding:utf-8 -*-
import unittest
import time
from uiautomator import device as d

class PerformanceTest(unittest.TestCase):
	"""
		performance test for caijing app
	"""
	def setUp(self):
		super(PerformanceTest,self).setUp()
		#d.watcher("AUTO_EXIT").when(text="退出").click(text="确定")
		self.__pressback(4)
	def tearDown(self):
		super(PerformanceTest,self).tearDown()
		#d.watcher("AUTO_EXIT").when(text="退出").click(text="确定")
		self.__pressback(4)
	def test_P0001(self):
		"""
			caseId:  P0001
			doc   :  test app lanuch and exit
			step  :  1.lanuch app
				     2.exit app
		"""
		#step 1
		self.__launchApp()
		#step 2
		self.__pressback(4)
	def test_P0002(self):
		"""
			caseId:  P0002
			doc	  :  test open the same magazine 10 times
			step  :  1.lanuch app
					 2.enter magazine store
					 3.open one magazine 10 times
					 4.exit app
		"""
		#step 1
		self.__launchApp()
		#step 2
		d(className="android.widget.ImageView")[2].click()
		time.sleep(3)
		#step 3
		for i in range(10):
			d(className="android.widget.ListView",packageName="com.caijing"). \
				child(className="android.widget.RelativeLayout")[0].click.wait.exists(timeout=3000)
			d(textContains="年第").sibling(className="android.widget.ImageView").click()
		#step 4 
		self.__pressback(4)
	def test_P0003(self):
		"""
			caseId:  P0003
			doc   :  test open magazine store and close
			step  :  1.launch app
			         2.enter magazine store 
			         3.tap return key to exit magazine
			     	 4.exit app
		"""
		#step 1
		self.__launchApp()
		#step 2
		d(className="android.widget.ImageView")[2].click()
		time.sleep(3)
		#step 3
		d(className="android.widget.ImageView")[0].click()
		#step 4
		self.__pressback(4)
   
	def __launchApp(self):
		#find app
		self.__findApp()
		# launch app
		d(text="财经杂志",packageName="com.android.launcher").click()
		time.sleep(3)
		assert d(className="android.widget.ImageView", \
			packageName="com.caijing")[0]
	def __findApp(self):
		"""
			different mobile phone different find method
		"""
		assert d(description="Apps",packageName="com.android.launcher")
		d(description="Apps",packageName="com.android.launcher").click()
		d(text="Apps",className="android.widget.TextView", \
			packageName="com.android.launcher").click()
		for i in range(3):
			d(className="android.view.View")[0].swipe.right()
		while(not d(text="财经杂志",packageName="com.android.launcher").exists):
			d(className="android.view.View")[0].swipe.left()
		assert d(text="财经杂志",packageName="com.android.launcher").exists
	def __pressback(self,c):
		for i in range(c):
			d.press.back()
			if d(text="退出").exists:
				d(text="确定",className="android.widget.Button").click()
				time.sleep(3)
				break

if __name__ == '__main__':
	unittest.main()
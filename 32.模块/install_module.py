#第三方模块的安装与使用
#安装方法: pip install 模块名
#第三方模块的使用 import 模块名
import schedule #这个schedule刚刚安装的模块
import time

def job():
    print("哈哈")

schedule.every(3).seconds.do(job) #每3秒运行一次job()函数
while 1:
    schedule.run_pending()
    time.sleep(1)#休眠一秒
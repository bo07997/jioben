import time


class Timer:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.use_time = 0
        self.pause_tag = False

    # 计时开始
    def start(self):
        self.begin = time.time()

    # 计时停止
    def stop(self):
        self.use_time = time.time() - self.begin
        self.begin = 0
        self.end = 0
        return self.use_time

    # 计时暂停
    def wait(self):
        self.pause_tag = True
        self.end = time.time()
        return True

    # 计时恢复
    def notify(self):
        if self.pause_tag is False:
            print("请先进行暂停操作")
            return False
        self.pause_tag = False
        self.begin = time.time() - self.end + self.begin

    # 获取计时
    def get_time(self):
        return time.time() - self.begin

    def if_wait(self):
        return self.pause_tag


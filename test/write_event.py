import pythoncom
import pyHook
from jioben.test import read_config
from jioben.test.common.Timer import Timer


class WriteEvent:
    def __init__(self):
        # 创建计时器
        self.timer = Timer()
        # 打开日志文件
        file_name = read_config.location
        self.file_obj = open(file_name, 'w')
        self.exit = set()
        return

    def OnMouseEvent(self, event):
        "处理鼠标事件"
        self.file_obj.writelines('mouse' + '\n')
        self.file_obj.writelines(str(self.timer.get_time()) + '\n')
        self.file_obj.writelines(str(event.Position[0]) + '\n')
        self.file_obj.writelines(str(event.Position[1]) + '\n')
        return True

    def OnKeyboardEvent(self, event):
        "处理键盘事件"
        if str(event.Key) not in self.exit:
            # 加入存在集合
            self.exit.add(str(event.Key))
            if event.Key == read_config.pause:
                # 暂停时间或者恢复
                if self.timer.if_wait():
                    self.timer.notify()
                else:
                    self.timer.wait()
            if str(event.MessageName) == 'key down' and event.Key != read_config.pause:
                self.file_obj.writelines('keyboard' + '\n')
                self.file_obj.writelines(str(self.timer.get_time()) + '\n')
                self.file_obj.writelines(str(event.MessageName) + '\n')
                self.file_obj.writelines(str(event.Key + '\n'))
                print(str(event.Key + '\n'))
            else:
                # str(event.MessageName) == 'key down' and event.Key == read_config.pause
                return True
                # self.exit.remove(str(event.Key))
        elif str(event.MessageName) == 'key up':
            self.file_obj.writelines('keyboard' + '\n')
            self.file_obj.writelines(str(self.timer.get_time()) + '\n')
            self.file_obj.writelines(str(event.MessageName) + '\n')
            self.file_obj.writelines(str(event.Key + '\n'))
            self.exit.remove(str(event.Key))
            if event.Key == read_config.stop:
                # 关闭日志文件
                self.file_obj.close()
                exit(0)
        else:
            # 长按情况，前面处理了
            return True
        return True

    def OnKeyboardUpEvent(self, event):
        self.exit.remove(str(event.Key))

    def begin(self):
        '''
           Function:操作SQLITE3数据库函数
           Input：NONE
           Output: NONE
           author: socrates
           blog:http://blog.csdn.net/dyx1024
           date:2012-03-1
           '''
        # 打开日志文件
        file_name = "D:\\hook_log.txt"
        self.file_obj = open(file_name, 'w')

        # 创建hook句柄
        hm = pyHook.HookManager()
        # 启动计时器
        self.timer.start()
        # 监控键盘
        hm.KeyAll = self.OnKeyboardEvent
        hm.HookKeyboard()
        # # 监控鼠标
        hm.MouseAllButtonsDown = self.OnMouseEvent
        hm.HookMouse()
        # # 循环获取消息
        pythoncom.PumpMessages()


if __name__ == "__main__":
    write_event = WriteEvent()
    write_event.begin()



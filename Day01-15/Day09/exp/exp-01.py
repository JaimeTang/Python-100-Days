"""
Author: Tang
Date: 2019-05-19

定义一个类描述数字时钟
"""
import time

class Clock(object):

    def __init__(self, hour, minute, second):
        """

        :param hour: 时  
        :param minute: 分  
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour +=1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        print("当前时间 {}:{}:{}".format(self._hour,self._minute,self._second))


def main():
    clock = Clock(23,59,58)
    while True:
        clock.show()
        time.sleep(1)
        clock.run()



if __name__=='__main__':
    main()
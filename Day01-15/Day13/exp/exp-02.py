from time import time, sleep
from threading import Thread
from random import randint

class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("下载{}".format(self._filename))
        sleep_time = randint(5,10)
        sleep(sleep_time)
        print("{}下载完成，耗时{}".format(self._filename, sleep_time))

def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__=="__main__":
    main()



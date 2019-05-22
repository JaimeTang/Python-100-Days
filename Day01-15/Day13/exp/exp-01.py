from multiprocessing import Process
from os import getpid
from time import time,sleep
from random import randint


def down_file(filename):
    print('启动下载进程，进程号{}.'.format(getpid()))
    print('开始下载{}...'.format(filename))
    sleep_time = randint(5,10)
    sleep(sleep_time)

def main():
    start = time()
    p1 = Process(target=down_file, args=('Python入门.pdf', ))
    p1.start()
    p2 = Process(target=down_file, args=('Python精通.pdf', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("总共耗时{:.2f}".format(end-start))



if __name__=='__main__':
    main()
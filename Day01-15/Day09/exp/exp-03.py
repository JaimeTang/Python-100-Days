"""
Author: Tang
Date: 2019-05-20

某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractclassmethod

def Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @abstractclassmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass


class Manager(Employee):
    
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    
    def __init__(self, name, working_hour=0):
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour
    
    @working_hour.setter
    def working_hous(self, hour):
        return self._working_hour = hour if hour > 0 else 0

    def get_salary(self):
        return self._working_hour*150.0



class Salesman(Employee):
    pass


def main():
    pass

if __name__=='__main__':
    main()
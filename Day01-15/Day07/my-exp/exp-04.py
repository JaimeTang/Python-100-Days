"""
Author: Tang

Date: 2019-05-18

计算指定的年月日是这一年的第几天
"""

def which_day(year, month, day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year%4==0 and year%100 != 0) or year%400 == 0 :
        days[1] = 29
        whichday = days[:month-1]
        whichday = sum(whichday)+day
    
    else:
        whichday = days[:month-1]
        whichday = sum(whichday)+day
    
    return whichday

def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))

if __name__=="__main__":
    main()
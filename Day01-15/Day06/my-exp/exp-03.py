"""
Author: Tang
Date: 2019-05-17
Target: 计算两个数的最大公约数和最小公倍数

"""

# def gcd(x,y):



def gcd(x, y):
    a = x if x > y else y
    for factor in range(a, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)

if __name__=='__main__':
    x = 6
    y = 15
    gcd_re = gcd(x,y)
    print(gcd_re)

    lcm_re = lcm(x,y)
    print(lcm_re)
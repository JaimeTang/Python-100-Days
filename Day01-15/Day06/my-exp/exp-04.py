"""
Author: Tang
Date: 2019-05-17
Target: 判断是否为回文数

"""

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == "__main__":
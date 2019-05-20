"""
Author: Tang

Date: 2019-05-19

大乐透选号

"""
from random import sample

def random_select(num=3):
    balls = []
    red_balls = [x for x in range(1,36)]
    blue_balls = [x for x in range(1,13)]
    for _ in range(num):
        ball = []
        ball.append(sorted(sample(red_balls,5)))
        ball.append(sorted(sample(blue_balls,2)))
        balls.append(ball)

    return balls


def main():
    n = int(input("机选几注："))
    my_num = random_select()
    print("我选择的号码：")
    for num in my_num:
        print(num)


if __name__=="__main__":
    main()
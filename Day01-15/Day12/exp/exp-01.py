import re

def main():
    username = input("输入用户名：（6-20位数字、字母）")
    qq = input("输入QQ号：（4-11位数字）")

    m1 = re.match(r'^[0-9a-zA-Z]{6,20}$',username)
    m2 = re.match(r'^[0-9]{4,11}$',qq)

    if not m1:
        print('输入的有户名不对。')
    if not m2:
        print('输入的QQ号不对。')
    if m1 and m2:
        print('输入信息正确。')

    

if __name__=='__main__':
    main()
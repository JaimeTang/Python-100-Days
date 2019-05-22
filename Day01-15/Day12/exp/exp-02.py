import re

def main():

    patter = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    message = '''
    重要的事情说3遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，t的手机号才是15600998765。
    '''

    mylist = re.findall(patter,message)
    print(mylist)

    print('------------------------')
    for temp in patter.finditer(message):
        print(temp.group())
    
    m = patter.search(message)
    while m:
        print(m.group())
        m = patter.search(message, m.end())



if __name__=='__main__':
    main()
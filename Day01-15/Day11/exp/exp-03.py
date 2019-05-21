import json

def main():
    mydict = {
        'name': 'Tang',
        'age': 31,
        'qq': 957658,
        'friends': ['wtx', 'byf'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8' ) as fj:
            json.dump(mydict, fj)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__=='__main__':
    main()
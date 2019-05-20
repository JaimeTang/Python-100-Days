"""
Author: Tang
Date: 2019-05-20

定义一个类描述数字时钟
"""


class Person(object):

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age >= 18:
            print("Play the games.")
        else:
            print("Don`t play the games.")

class Student(Person):

    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,grade):
        self._grade = grade
    
    def study(self):
        if self._grade >= 6:
            print("Name:{} Age:{} Grade:{} is studing".format(self._name, self._age, self._grade))
        else:
            print("Playing...")


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name,age)
        self._title = title
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title
    
    def study(self):
        print("Name:{} Age:{} Title:{} is teaching".format(self._name, self._age, self._title))


def main():
    person = Person('Tang',15)
    person.play()

    person.age = 20
    person.play()

    student = Student('Tang',15,4)
    student.play()
    student.study()
    student.age = 20
    student.grade = 8
    student.play()
    student.study()


if __name__=='__main__':
    main()
    


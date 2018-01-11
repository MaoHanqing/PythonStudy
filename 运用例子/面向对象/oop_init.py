class Person:

    def __init__(self,name):
        #创建属性只需要self.name 即可
            self.name = name
    def say_hi(self):
        print('Hello,my name is',self.name)

p = Person('Swaroop')
p.say_hi()
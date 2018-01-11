#创建简单的类
class Person:
    #Python 无参数方法也需要存在一个self
    def say_hi(self):
        print('Hello,how are u')

p = Person()
p.say_hi()

#coding = UTF-8
#命名约定：任何在类或对象之中使用的变量命名都应以下划线开头
#其它所有非此格式的名称都将是公开的
#双下划线前缀的为私有变量

class Robot:
    '''表示有一个带有名字的机器人'''
    #类变量可以被属于该类的所有实例访问。该类变量只有一个副本
    # 当任何一个对象对变量作出改变时
    # 发生的变动将在其它所有的实例中得到体现
    population = 0
    #以双下划线作为前缀的变量为私有变量
    __privater = 1
    def __init__(self,name):
        #对象变量
        #由类的每一个对立的对象或实例所拥有
        # 每个对象都拥有他自己的副本
        #不会以任何方式与其它不同实例中的相同字段产生关联
        self.name = name
        print('(Initializing {})'.format(self.name))
        Robot.population += 1  # 等价self.__class__.population  +=1
    def die(self):
        print('{} is being destroyed!'.format(self.name))
        Robot.population -= 1  #等价self.__class__.population  -=1

        if Robot.population == 0:
            print('{} was the last one'.format(self.name))
        else:
            print('There are still {:d} robots working.'.format(Robot.population))
    def say_hi(self):
        print('Greetings,my masters call me {}'.format(self.name))
    @classmethod
    #类方法
    def how_many(cls):
        print('We have {:d} robots'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()
droid2 = Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some work here')
print('Robots have finished their work.So let\'s destroy them')
droid1.die()
droid2.die()
Robot.how_many()

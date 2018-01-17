#函数定义使用def 函数名（参数）：
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

#空函数什么都不做的函数 用pass结尾
def nop():
    pass
# pass可以作为占位符 目前未想好做什么 保证代码可以正常运行起来

#参数检测：
#内置函数isinstance()来进行类型检查
def check(x):
    if not isinstance(x,(int,float)):
        #raise 为抛出异常 typeError 为类型错误异常
        raise TypeError('bad operand type')
    else:
        print('good operand type')

#返回多个值
def move(x,y):
    return x+1,y-2
#实际返回为tuple 元组 但是语法上元组可以省略括号
#多个变量接受同一个元组按顺序赋值
r = move(1,4)

x,y = move(1,4)

print(x,y)

#位置参数 默认参数 可变参数
def methond(a,b = 2):
    #a为位置参数，b为默认参数
    print(a,b)

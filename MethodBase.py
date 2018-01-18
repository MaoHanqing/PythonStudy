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

#可变参数 就是传入的参数个数可变
#对象分为可变对象和不可变对象
#List和tuple为可变对象 传入函数后在函数内对其进行修改外面的也会跟着改变
#而其它的为不可变遍对象，传入函数后函数内修改无影响，相当于创建了一个新的对象

#按一般的传入
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#传入list或tuple
calc([1,2,3])
#按可变参数
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc1(1,2,3,4)
#如果存在list或tuple 可以在前面加*传入
num = [1,2,3]
calc1(*num)


#关键字参数
#关键字参数允许你传入人一个含参数名的参数，这些关键字参数在函数内自动组成一个dic
def person(name,age,**kw):
    print('name',name,'age:',age,'other:',kw)
#可以传入任意个数的关键字参数
person('Michael',30)
person('Bob',35,city ='BeiJing')
person('Adam',45,gender = 'M',job ='Engineer')

extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)
#命名关键字参数
#如果要限制关键字参数的名字，可以用命名关键字参数
#函数带*后的参数为关键字参数
#例如只接受city和job作为关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

#带有关键字参数函数调用时必须将关键字显示输出
person('Jack',24,city='Beijing',job='Engnineer')

#如果函数中定义了一个可变参数，其后的参数便是关键字参数
def person1(name,age,*args,city,job):
    print(name,age,args,city,job)

person1('Mon',24,2,4,5,city='ZZ',job='XX')#等价于person1('Mon',24,*(2,4,5),city='ZZ',job='XX')

person('jack',22,city='ShangHai',job='Paternar')
#命名关键字参数可以有默认值
def person2(name,age,*,city = 'Shanghai',job ):
    print(name,age,city,job)
person2('Amar',33,job='Creator')

#参数组合
#python定义的函数中，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#递归函数
#如果一个函数在内部调用自己本身，这个函数就是递归函数
def fact(n):
    #表示阶乘 n！= 1 * 2 * 3 ...* n
    if n == 1:
        return 1
    return  n * fact(n - 1)
#使用递归函数需要注意防止栈溢出。
#在计算机中，函数的调用通过栈这种数据结构实现的
#当进入一个函数调用，栈就会加一层栈帧
#每当函数返回，栈就会减一层栈桢
#由于栈的大小不是无限的
#所以递归调用的次数过多，会导致栈溢出。例如
fact(1000)
#解决递归调用栈溢出的方法是通过尾递归优化
#尾递归是指在函数返回时，调用函数本身，return不包含语句表达式
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num -1,num*product)


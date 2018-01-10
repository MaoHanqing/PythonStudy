#python中函数都默认会return none 除非重写return语句。
def return_func():#无参有返回值函数
    return 1
def pass_func():#用pass短语，表示无内容函数
    pass
def say_hello():#   无参无返回值函数
    #该块属于这一函数
    print('hello world')
#函数结束

def print_max(a,b):#有参无返回值函数
    if a > b:
        print(a)
    elif a<b:
        print(b)
    else:
        print(a,'is equal to',b)

x = 50
def func():
    x = 3
    print(x)

func()

def key_func(a,b = 10,c = 20):
        print('a is',a,'and b is',b,'and c is',c)
key_func(3)# 包含默认值函数
key_func(3,4)#如果不指定参数 将会按顺序依次赋值



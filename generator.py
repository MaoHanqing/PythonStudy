#python中一边循环，一边计算的机制称为生成器
#要创建一个generator有多种方法
#第一种为将list的[]换为（）
l = (x * x for x in range(10))
#如果要打印怵generator 的每一次元素得用
next(l)
#一般用for循环，generator是可迭代的对象
for n in l:
    print(n)
#定义generator的另一种方法时如果函数关键词中包含yield关键字
#那么这个函数就不再时一个普通函数而是一个generator
#generator和函数执行流程不一样，函数遇到return就返回
#generator函数，在每次调用next时候执行，
#遇到yield语句返回，再次执行时候从上次返回的yield语句处继续执行
def fib(max):
    n, a ,b = 0, 0 ,1
    while n < max:
        yield b
        a,b = b , a+b
        n = n+1
    return 'done'


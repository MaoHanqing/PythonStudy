#python中一边循环，一边计算的机制称为生成器
#要创建一个generator有多种方法
#第一种为将list的[]换为（）
l = (x * x for x in range(10))
#如果要打印怵generator 的每一次元素得用
next(l)
#一般用for循环，generator是可迭代的对象
for n in l:
    print(n)

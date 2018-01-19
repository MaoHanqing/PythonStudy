#列表生成式是python内置的创建list的生成式
#生成list[1,2,3,4,5] 可以用
list(range(1,5))
#如果生成[1*1,2*2,3*3...,10*10]
#方法一 利用for循环
l = []
for x in range(1,11):
    l.append(x * x)
# 方法二
#把要生成的元素x*x放在前面 后面跟for循环
[x * x for x in range(1,11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#for循环后还可以加上if判断，例如筛选结果为偶数的
[x * x for x in range(1,11) if x % 2  == 0]
#[4, 16, 36, 64, 100]

#还可以使用双层循环
[m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
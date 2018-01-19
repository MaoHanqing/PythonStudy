#python循环有两种
#一种为for...in
names = ['Michale','Bob','Tracy']
for name in names:
    print(name)

numSum = 0
for x in [0,1,2,3,4,5]:
    numSum = numSum + x

print(numSum)

numSum = 0

for x in list(range(6)):
    numSum = numSum + x
print(numSum)


#range 函数会自动生成整数序列
for i in range(6):
    print('A',i)
#range(6）表示从0<x<6个整数序列
#range（1，6）表示从1<x<6
#range(1,6,2)1<x<6，间隔为2


#python内的enumerate可以把list变成索引元素
for i,value in enumerate(['A','B','C']):
    print(i,value)


#dic迭代
d = {'a' : 1 ,'b':2,'c' :3}
#迭代key
for key in d:
    print(key)
#迭代valye
for value in d.values():
    print(value)
#同时迭代key value
for k,v in d.items():
    print(k,v)

#字符串也是可以的迭代的对象

#可以通过collections模块的Iterable类型判断：是否可以迭代
from collections import  Iterable
isinstance('abbc',Iterable)
isinstance(123,Iterable)


#第二种为while
#满足条件就一直运行下去 不满足条件时跳出 break continue 语句依旧可以用
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)

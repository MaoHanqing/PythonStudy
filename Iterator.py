#迭代器
#for循环的数据类型有以下几种：
#1:集合类数据类型，如list、tuple、dict、set、str
#2:generator 包括生成器和带yield的函数
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
#可以使用isinstance（）判断一个对象是否时Iterable对象

from collections import Iterable
isinstance([],Iterable)
isinstance({},Iterable)
isinstance('ANC',Iterable)
isinstance((x for x in range(10)),Iterable)

#而生成器不但可以作用于for循环还可以被next（）函数不断调用并返回下一个值
#直到最后抛出StopIteration错误表示无法继续返回下一个值了
#可以被next（）函数调用并不断返回下一个值的对象称为迭代器：Iterator
#可以使用isinstance（）判读一个对象是否是Iterator
from collections import Iterator
isinstance((x for x in range(10)),Iterator)#true
isinstance([],Iterator)#false
#生成器对象都是Iterator 但是Iterable不一定是Iterator
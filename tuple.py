#tuple 为元组：一旦初始化后将不可以修改
#定义一个tuple时，tuple的元素就必须被确定下来，例如
t = (1,2)
#如果定义一个空的tuple
empty = ()
#但是如果定义只有一个元素的tuple则
one = (1,)
#定义one（1）tuple 意义为元组中1这个数字而不是元组内元素数量
#tuple内只有一个元素时结尾会带，以免早层误会

#一种'可变的'tuple
var = ('a','b',['A','B'])
var[2][0] = 'X'
var[2][1] = 'Y'
var[2].append('V')
print(var)
#元组内的list改变了 而元组一开始指向的list并未变为其它list
#元组在元素内存意义上并未改变
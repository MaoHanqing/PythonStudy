age = 20
name = 'swaroop'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('why is {0} playing with that python?'.format(name))
print('ddd' + 'aa' +'dddd{0}'.format('dd'))
print('{name} wrote {book}'.format(name = name,book = 'ddd'))
print('a',end=" ") #每个print结尾都以/n结束 可以用空格替换/n
a = 3
b = 4
print(a//b )#//为整除
print(a**b)#**为乘方

guess = int(input('enter'))

for i in range(1,5,2): #range中最后一个参数指函数以2来递增
    print(i)

# 字符长度函数len()
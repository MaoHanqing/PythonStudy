shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'
#[]中直接数字为索引 -1为序列中倒数第一个 -2 为倒数第二个
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1])
print('Item -2 is',shoplist[-2])
print('Character 0 is',name[0])
# [:]为切片操作 第一个数字为开始位置默认为从头开始 第二个为结束位置默认为到结尾
print('Item 1 to 3 is',shoplist[1:3])
print('Item 2 to end is',shoplist[2:])
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start To end is',shoplist[:])
#
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to -1 is',name[1:-1])
print('characters start to end is',name[:])
#第三个参数为切片的步长 默认为1 
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::-1])#为-1的情况可以实现序列反转



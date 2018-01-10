print('Simple Assignment')
shoplist= ['apple','mango','carrot','banana']
mylist = shoplist
del shoplist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)

print('copy by making a full slice')
#切片会生成制作一份新的列表副本
mylist = shoplist[:]
del  mylist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)

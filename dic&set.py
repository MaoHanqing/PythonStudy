d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 通过 d['Jack']这种方式取值 如果value不存在则会报错
# d['Jack']
#通过get（）取值 如果key不存在返回None或者自己指定的value
d.get('Thomas')
d.get('Thomas','defaultValue')
#删除一个key用pop（）
d.pop('Bob')


#set 会自动过滤掉存在的元素
s = set([1,1,2,3,4])
s.add(5)
s.remove(3)
#set 可以看成数学意义上的无须无重复的元素集合，因此两个set可以取并或交
s1 = set([2,3,4])
s2 = set([3,4,5,6])

print(s1 & s2)
print(s1 | s2)

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
#range(6）表示从0<x<6个整数序列
#range（1，6）表示从1<x<6
#range(1,6,2)1<x<6，间隔为2

#第二种为while
#满足条件就一直运行下去 不满足条件时跳出 break continue 语句依旧可以用
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n -2
print(sum)

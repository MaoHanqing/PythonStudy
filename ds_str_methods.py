name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes,the string starts with "Swa"')
if 'a' in name:
    print('Yes,it contains the spring a')
if name.find('war') != -1 :
    #find 方法用于定位字符串中给定的子字符串的位置。如果找不到相应的子字符串就会返回-1
    print('Yes,it contains the spring "war"')


delimter = '_*_'
mylist = ['Brazil','Russia','India','China']
mydic = {
    'dd':'ddddd',
    'aa':'aaaaa'
}

#join会将字符串作为每一个项目（数组，集合，字符串等均可）间的分隔符，返回一串更大的字符串

print(delimter.join(mylist))

#print(delimter.join(mydic))    Brazil_*_Russia_*_India_*_China

#print(delimter.join(name))     S_*_w_*_a_*_r_*_o_*_o_*_p

#print(delimter.join(mydic))    dd_*_aa

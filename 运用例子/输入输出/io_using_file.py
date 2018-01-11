poem = '''\
Programming is fun
When the work is done 
if you wanna make your work also fun:
    use Python!
'''
#打开可以是阅读模式（'r'），写入模式（'w'），追加模式（'a'）
f = open('poem.txt','w')
help(open)

f.write(poem)
f.close()


f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    print(line,end='')
f.close()

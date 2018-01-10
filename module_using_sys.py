import sys
print('the command line arguments are:')

for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')

from  math import sqrt
#这种导入方式可以省去math.sqrt 的调用形式 但不推荐
print('square root of 16 is',sqrt(16))
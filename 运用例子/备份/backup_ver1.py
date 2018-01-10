import os
import time

#1.需要备份的文件和目录将被指定在一个列表中。
sources  = ['/Users/maohanqing/Desktop/UI']
#2.备份文件必须储存在一个主备份目录中
target_dir = '/Users/maohanqing/Desktop'
#3.备份文件打包成zip文件
#4.zip文件的文件名由当前日期和时间构成
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#如果目标目录不存在，则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
#5 使用zip命令将文件打包ZIP格式
zip_command = 'zip -r {} {}'.format(target,''.join(sources))
#运行备份
print('zip command is:')
print(zip_command)
print('runnung:')
if os.system(zip_command) == 0:
    print('Successful backup to ',target)
else:
    print('backup Failed')

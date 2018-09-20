#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: phy time:2018/9/

# 任务——将image文件夹下所有的图片名'-‘后面的数字写到一个1.txt文件夹下
# 一个图片名出来的数字写在一行，读取1.txt文件，打印出里面每一行的内容

# 1、读取文件夹图片目录
import os
filepath = ".\image"
filename = os.listdir(filepath)
del filename[0]
print 'filename: ', filename

# 2、打开txt文件，准备写入
# 3、通过for循环，分割两次列表元素名称
# 4、将分割好的数字写入txt文件

with open('1.txt','w') as f:
    for fileindex,fileval in enumerate(filename):
#         print ('fileval: ',fileval)
        delfront = fileval.split('-')
#         print ('delfront: ',delfront[1])
        delfinal = delfront[1].split('.')
        print 'delfinal: ', delfinal[0]
        # for write in delfinal[0]:
        f.writelines( delfinal[0] + '\n')

# 5、打开txt文件，读取所有行，返回列表
# 6、按行打印内容并关闭文件
with open('1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print 'each line: ', line
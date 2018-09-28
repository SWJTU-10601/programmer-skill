# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:09:22 2018

@author: Afini
"""
import os
#定义类Add，初始化成员文档路径txt_dir,函数Write实现主要功能。

class Add():
    txt_dir = ''
    def __init__(self, Dir):
        self.txt_dir = Dir
        
    def Write(self):
        with open('./result.txt','w') as f:
            print(self.txt_dir)
            for file in os.listdir(self.txt_dir):
                num = open('./data/'+file,'r')
                num = num.read()
                f.write(file[:-4].strip()+num+'\n')

#以下为继承类
class Add_inherit(Add):
    txt_dir = ''
    def __init__(self, Dir):
        #调用父类的构造函数
        Add.__init__(self, Dir)
        self.txt_dir = Dir
    #复写父类函数    
    def Write(self):
        with open('./result.txt','w') as f:
            print(self.txt_dir)
            for file in os.listdir(self.txt_dir):
                num = open('./data/'+file,'r')
                num = num.read()
                f.write(file[:-4].strip()+num+'\n')    

Home = Add_inherit('./data')
Home.Write()                


















               
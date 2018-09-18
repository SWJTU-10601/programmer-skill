import os
clip_imgdir = r'./data'

# generator列表生成器
# 生成的是一个对象，不会把数据直接创建出来，当for遍历的时候，生成器对象会调用next()函数，获取下一个要生成的数据

with open('./result.txt', 'w') as f:
    generator_file = (file for file in os.listdir(clip_imgdir))#保存到列表生成器generator_file，通过下一行for循环读取文件名。
    #print(generator_file)测试
    for i in range(4):     
        file = next(generator_file)
        num = open('./data/'+file, 'r')
        num = num.read()
        f.write(file[:-4].strip() + num + '\n')
'''    
    for file in generator_file:
        num = open('./data/'+file, 'r')
        num = num.read()
        f.write(file[:-4].strip() + num + '\n')
'''  
'''
with open('./result.txt', 'w') as f:
    list_file = [file for file in os.listdir(clip_imgdir)]#保存到列表生成式list_file，通过下一行for循环读取文件名。
    #print(generator_file)测试
    for file in list_file:
        num = open('./data/'+file, 'r')
        num = num.read()
        f.write(file[:-4].strip() + num + '\n')        
'''        
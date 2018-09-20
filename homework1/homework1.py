# 把data文件夹下的的每个txt，文件名-后面的数字加上文档里面的数字 依次写到result文件夹下的result.txt

import os
home = os.path.abspath('.')
data_path = os.path.join(home,'data')
txt_list = []
txt_num = []

result_dirpath = os.path.join(home,'result')
if not os.path.exists(result_dirpath):
    os.mkdir(result_dirpath)

sum_list = []
for file in os.listdir(data_path):
    # txt_list.append(file)
    a = file.strip().split('-')
    a = a[1].strip().split('.')
    value1 = int(a[0])
    # index = file.find('-')
    # value1 = int(file[index+1:-4])
    # print(value1)
    # txt_num.append(file[index+1:-4])
    txt_path = os.path.join(data_path,file)
    sum = 0
    with open(txt_path,'r')as f:
        for line in f.readlines():
            value2 = int(line)
        sum = value1 + value2
    sum_list.append(sum)
result_path = os.path.join(result_dirpath,'result.txt')
with open(result_path,'w') as f:
    for i in range(len(sum_list)):
        f.write(str(sum_list[i])+'\n')

print(sum_list)



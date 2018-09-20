import os
home = os.path.abspath('.')
data_path = os.path.join(home,'data')

result_dirpath = os.path.join(home,'result')
if not os.path.exists(result_dirpath):
    os.mkdir(result_dirpath)
result_path = os.path.join(result_dirpath,'result.txt')

g = (file for file in os.listdir(data_path))  # 文件名生成器
sum_list = []

# 清空result.txt
with open(result_path,'w') as f:
    f.truncate()
for i in g:
    value1 = int(i.strip().split('-')[1].split('.')[0])
    with open(os.path.join(data_path,i),'r') as f:
        value2 = int(f.readline())
    with open(result_path,'a') as f:
        f.write(str(value1+value2)+'\n')
    sum_list.append(str(value1+value2))

print(sum_list)



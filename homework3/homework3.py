import os
home = os.path.abspath('.')
data_path = os.path.join(home,'data')

result_dirpath = os.path.join(home,'result')

if not os.path.exists(result_dirpath):
    os.mkdir(result_dirpath)
result_path = os.path.join(result_dirpath,'result.txt')
with open(result_path,'w') as result:
    result.truncate()


class HM3:

    def __init__(self,data_path,result_path):
        self.data_path = data_path
        self.result_path = result_path

    def data_add(self):
        sum_list=[]
        file_generator = (file for file in os.listdir(data_path))  # 文件名生成器
        with open(self.result_path, 'a') as result_file:
            for i in file_generator:
                value1 = int(i.strip().split('-')[1].split('.')[0])
                with open(os.path.join(self.data_path, i), 'r') as data_file:
                    value2 = int(data_file.readline())
                result_file.write(str(value1 + value2) + '\n')
                sum_list.append(str(value1 + value2))
        return sum_list

hm = HM3(data_path,result_path)
sum_list = hm.data_add()
print(sum_list)

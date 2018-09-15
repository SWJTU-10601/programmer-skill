import os
data_dir = r'./data'
files = os.listdir(data_dir)
all_result_num = []
for file in files:
    filename_num = int(file.split('.')[0].split('-')[1])
    file_path = os.path.join(data_dir, file)
    with open(file_path, 'r') as fout:
        context_num = int(fout.readlines()[0])
    all_result_num.append(filename_num + context_num)

with open('./result.txt', 'w') as fin:
    for num in all_result_num:
        fin.write(str(num)+'\n')



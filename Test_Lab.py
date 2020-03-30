# def check():
#     group_1_indices_check = [1, 2, 3]
#     group_2_indices_check = [4, 5, 6]
#
#     return "data1", "data2", group_1_indices_check, group_2_indices_check
#
#
# group_1_indices, group_2_indices = check()
#
# print(group_1_indices)
# print(group_2_indices)

import os

root_data_path = r'C:\Users\HP\Desktop\5th & 6th Semester\Bap Re Bap\Test.csv'
with open(root_data_path, encoding="utf-8") as opened_file:
    print(os.path.basename(root_data_path))
    q = opened_file.readlines()

    # Reading the data(line by line)
    # Each row should contain data of one type. e.g. All participants data of personality
    for line in q:
        line = line.split(',')
        print(line)


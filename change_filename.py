import os

path = '文件路径'
rpc = '要替换的字段'
# 获取路径内文件
file = os.listdir(path)
for i in range(len(file)):
    # 原文件名
    n1 = path + '\\' + file[i]
    # 新文件名
    n2 = n1.replace(rpc, '')
    # 调用改名函数，完成改名操作
    os.rename(n1, n2)

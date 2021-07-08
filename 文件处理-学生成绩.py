# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script file.
"""

"""
import random

x = [[random.randint(0,101) for i in range(random.randint(1, 10))]\
     for line in range(random.randint(10, 20))]
    
y = [ ','.join(map(str, item))+'\n' for item in x ]
with open(r"C:\data.txt", mode="wt", encoding="cp936") as fp:
    fp.writelines(y)
"""

# 文本文件data.txt中保存了某班所有同学的Python课成绩。
# 编程: (1) 读取该文本文件中的所有成绩，计算并输出平均分；
#       (2) 将所有不及格的按照从低到高写入文本文件“C:\不及格成绩单.txt”；
#       (3) 将所有高于平均分的成绩按照从高到低写入文本文件“C:\高于平均成绩单.txt”；

with open(r"C:\data.txt", mode="rt", encoding="cp936") as fp,\
    open(r"C:\不及格成绩单.txt", mode="wt", encoding="cp936") as fp1,\
    open(r"C:\高于平均成绩单.txt", mode="wt", encoding="cp936") as fp2:
        rows = fp.readlines()                       # 将文件每行读入列表
        rows = [row.strip() for row in rows]        # 删除列表中每个元素中的空白字符
        rows = ','.join(filter(None, rows))         # 只留下非空白字符串并组合成一个字符串
        # 可以用下面这句替换
        #rows = ','.join(filter(None, [row.strip() for row in fp.readlines()]))
       
        rows = rows.split(',')                      # 将数据分离出来
        rows = [item.strip() for item in rows]      # 删除列表中每个元素中的空白字符
        rows = list(map(int, filter(None, rows)))   #转换为整数
        ave = sum(rows) / len(rows)                 #计算平均分
        print("平均分为：{}".format(ave))
        
        result1, result2 = [], []
        for score in rows:
            if score < 60:                          # 低于60分
                result1.append(score)
            
            if score > ave:                         # 高于平均分
                result2.append(score)
        
        result1 = sorted(result1)
        result2.sort(reverse=True)
        result1 = ','.join(map(str, result1))       # 转换为字符串
        result2 = ','.join(map(str, result2))       # 转换为字符串
        
        fp1.write(result1)
        fp2.write(result2)
        

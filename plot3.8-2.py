import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

labels = "A难度水平", "B难度水平", "C难度水平", "D难度水平"
students = [0.35, 0.15, 0.20, 0.30]
colors = ["#377eb8","#4daf4a","#984ea3","#ff7f00"]
explode = (0.1, 0.2, 0.6, 0.1)

# exploded pie char
plt.pie(students,explode=explode,labels=labels,autopct="%3.1f%%",\
        startangle=30,shadow=True,colors=colors)

plt.title("选择不同难度测试试卷的学生占比")
plt.show()
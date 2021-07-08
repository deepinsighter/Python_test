def demo(x,y,z=1,*a,**b):
    print(x,y,z)
    print(a,type(a))
    print(b,type(b))

demo(10,20,30)
demo(10,20,30,a=100,b=200)


"""
fp = open(r"f:\ptest\students.txt","w")

for i in range(3):
    stu = input("输入学生信息：")
    fp.write(stu)

fp.close()
"""

"""
fp = open(r"f:\ptest\students.txt","r")
s = fp.read()
print(s)
fp.close()
"""         

"""
fp = open(r"f:\ptest\students.txt","r")
try:
    while True:
        s = fp.readline()
        if s == '':
            break
        print(s)
except:
    pass

fp.close()
"""

"""
fp = open(r"f:\ptest\students.txt","r")
s = fp.readlines()
print(s)

fp.close()
"""

"""
fp = open(r"f:\ptest\students.txt","r")
for line in fp:
    print(line)

fp.close()
"""
"""
with open(r"f:\ptest\students.txt","r") as fp:
    print(fp)
    for line in fp:
        print(line)
"""
"""
with open(r"f:\ptest\students.txt","r+") as fp:
    fp.seek(0)
    fp.write("有福")
"""

"""
with open(r"f:\ptest\test.txt","r+",encoding="utf-8") as fp:
    for line in fp:
        print(line, end='')
"""








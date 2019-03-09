#encoding=utf-8
import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

# 完成随机分配
# i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

# 获取办公室信息
i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,'')
    print("\n")
    print("-"*20)
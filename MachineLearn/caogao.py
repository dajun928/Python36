import jieba

result=jieba.cut('我是一个好程序员')

for i in result:
    print(i,end=" ")
# print(result)
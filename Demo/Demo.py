#encoding=utf-8



# f = open('test.txt', 'w')
# f.write('hello world, i am here!')
# f.close()
#
# f = open('test.txt', 'r')
#
# content = f.read(5)
#
# print(content)
#
# print("-"*30)
#
# content = f.read()
#
# print(content)
#
# f.close()

# hello world, i am here!

f = open("test.txt", "r")
str = f.read(3)
print "读取的数据是 : ", str

# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position

str = f.read(3)
print "读取的数据是 : ", str

# 查找当前位置
position = f.tell()
print "当前文件位置 : ", position

str = f.read(3)
print "读取的数据是 : ", str
f.close()













































#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 3.6.3
@file : copy_file.py
@time : 2019/04/16 19:21:50
@func : 
"""
import os
import shutil


def copydir(path, out):
    for files in os.listdir(path):
        name = os.path.join(path, files)
        back_name = os.path.join(out, files)
        if os.path.isfile(name):
            if os.path.isfile(back_name):
                # print(back_name)
                pass
            else:
                # print(back_name)
                pass
        else:
            if not os.path.isdir(back_name):
                os.makedirs(back_name)
                copydir(name, back_name)



def copyfile(src, dsc):
    tmp_list=[]
    for root, dirs, files in os.walk(src):
        if dirs:
            dsc_path=dsc
        else:
            dsc_path=os.path.join(dsc, os.path.split(root)[1])
        for file in files:
            src_file=os.path.join(root,file)
            tmp_trup=(src_file,dsc_path)
            tmp_list.append(tmp_trup)
    return tmp_list

def main():
    A = r"D:\test\b"
    B = r"D:\test\a"
    copydir(A, B)
    result = copyfile(A, B)
    # print(result)
    if result:
        src_file, dsc_path = result.pop()
        print(src_file)
        print(dsc_path)
        shutil.move(src_file, dsc_path)

if __name__ == '__main__':
    main()
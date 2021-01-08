#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : write_data_excel.py
@time : 2021/01/07 16:21:31
@func : xlwt 写入excel demo 备用
"""
import datetime
import xlwt

def write_excel(file_path, data1,data2):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet(u"统计数据", cell_overwrite_ok=True)
    title1 = ["管理员", "总计设备数", "设备类型", "分类设备数", "netbase监控率", "Wup监控率"]
    data1.insert(0, title1)
    style = xlwt.XFStyle()
    align = xlwt.Alignment()
    align.horz = 1
    style.alignment = align
    i = 0
    # admin_set = set([i[0] for i in data1 if i[0] != "管理员"])
    device_set = set([i[2] for i in data1])
    print(device_set)
    for data in data1:
        for j in range(len(data)):
            sheet1.write(i, j, data[j], style=style)
        i = i + 1
    f.save(file_path)
    sheet2 = f.add_sheet(u"设备详细信息", cell_overwrite_ok=True)
    title1 = ["管理IP", "监控类型", "主机名", "设备管理员", "netbase监控", "Wup监控"]
    data2.insert(0, title1)  # 写入表头
    style = xlwt.XFStyle()
    align = xlwt.Alignment()
    align.horz = 1
    style.alignment = align
    i = 0
    for data in data2:
        for j in range(len(data)):
            sheet2.write(i, j, data[j], style=style)
        i = i + 1
    f.save(file_path)


if __name__ == "__main__":
    str_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data1 = [['张三 ', 7, '安全客户端', 3, '33.33%', '100.00%'],
             ['张三 ', 7, '防火墙', 1, '100.00%', '100.00%'],
             ['张三 ', 7, '交换机', 1, '100.00%', '100.00%'],
             ['张三 ', 7, '异常行为', 2, '50.00%', '100.00%'],
             ['李四', 5, '安全客户端', 4, '50.00%', '100.00%'],
             ['李四', 5, '防火墙', 4, '75.00%', '100.00%'],
             ['李四', 5, '交换机', 2, '100.00%', '100.00%'],
             ['李四', 5, '异常行为', 2, '50.00%', '100.00%'],
             ['王五', 5, '安全客户端', 5, '40.00%', '100.00%'],
             ['王五', 5, '防火墙', 4, '75.00%', '100.00%'],
             ['王五', 5, '交换机', 4, '50.00%', '100.00%'],
             ['王五', 5, '异常行为', 4, '75.00%', '100.00%']]
    data2 = [['192.168.178.1', '安全客户端', '192.168.178.1', '张三 ', False, True],
             ['192.168.178.2', '安全客户端', '192.168.178.2', '张三 ', True, True],
             ['192.168.178.3', '安全客户端', '发斯蒂芬斯蒂芬', '张三 ', False, True],
             ['192.168.178.4', '防火墙', '192.168.178.4', '张三 ', True, True],
             ['192.168.178.5', '防火墙', '192.168.178.5', '李四', True, True],
             ['192.168.178.6', '防火墙', '法法', '李四', False, True],
             ['192.168.178.7', '防火墙', '192.168.178.7', '李四', True, True],
             ['192.168.178.8', '交换机', '撒阿发发', '王五', False, True],
             ['192.168.178.9', '交换机', '192.168.178.9', '张三 ', True, True],
             ['192.168.178.10', '异常行为', '192.168.178.10', '王五', True, True],
             ['192.168.178.11', '异常行为', '按时发发发', '张三 ', False, True],
             ['192.168.178.12', '异常行为', '192.168.178.12', '王五', True, True],
             ['192.168.178.13', '异常行为', '啊啊是发发', '张三 ', True, True],
             ['192.168.178.14', '安全客户端', '192.168.178.14', '李四', True, True],
             ['192.168.178.15', '交换机', '192.168.178.15', '王五', False, True],
             ['192.168.178.16', '交换机', '啊发发发生发发', '李四', True, True],
             ['192.168.178.17', '安全客户端', '192.168.178.17', '王五', False, True]]
    write_excel("安全管理员对应设备类型统计%s.xls" % str_time, data1,data2)

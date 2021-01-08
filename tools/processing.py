

# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@version :
@file : processing_data.py
@time : 2021/01/07 16:41:12
@func :
"""
import datetime
import xlwt
import pdb


def write_excel(file_path, data1, data2):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet(u"统计数据", cell_overwrite_ok=True)
    title1 = ["管理员", "总计设备数", "设备类型", "分类设备数", "netbase监控率", "Wup监控率"]
    style = xlwt.XFStyle()
    align = xlwt.Alignment()
    align.horz = 1
    style.alignment = align
    for j in range(len(title1)):
        sheet1.write(0, j, title1[j], style=style)
    i = 1
    dict_list=[]
    tmp_dict={}
    for data in data1:
        device_kinds = data[-1]
        data = data[:-1]
        keys_list=[list(i.keys())[0] for i in dict_list]
        if data[0] not in keys_list:
            tmp_dict[data[0]]=(data[1],device_kinds)
            dict_list.append(tmp_dict)
            tmp_dict={}
        for j in range(len(data)):
            sheet1.write(i, j, data[j], style=style)
        i += 1


    # dict_list=[{"张三":(7, 4)},{'李四': (5, 3)},{'王五': (5, 3)}]
    step0=0
    for k in dict_list:
        name=list(k.keys())[0]
        number,step=list(k.values())[0]
        sheet1.write_merge(step0+1, step0+step, 0, 0, name)  # 合并列单元格
        sheet1.write_merge(step0+1, step0+step, 1, 1, number)  # 合并列单元格
        step0+=step
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




def analysis_data(datas):
    tmp_list = []
    adminitors = {}
    for i in datas:
        if i[3] in adminitors:
            adminitors.setdefault(i[3], []).append(i)
        else:
            adminitors[i[3]] = [i]
    for k, v in adminitors.items():
        device_type = {}
        sum_devices = len(v)
        for i in v:
            if i[1] in device_type:
                device_type.setdefault(i[1], []).append(i)
            else:
                device_type[i[1]] = [i]
        davice_counts = len(device_type)
        device_type_keys = device_type.keys()
        # pdb.set_trace()
        for device_type_key in device_type_keys:
            items = device_type[device_type_key]
            items_num = len(items)
            netbase_true_num = 0
            whatsup_true_num = 0
            for item in items:
                if item[-2]:
                    netbase_true_num += 1
                if item[-1]:
                    whatsup_true_num += 1
            netbse_rate = '{:.2f}%'.format(netbase_true_num / items_num * 100)
            wup_rate = '{:.2f}%'.format(whatsup_true_num / items_num * 100)
            tmp_list.append([k, sum_devices, device_type_key, items_num, netbse_rate, wup_rate, davice_counts])
    # print(tmp_list)
    return tmp_list




if __name__ == '__main__':
    datas = [['192.168.178.1', '安全客户端', '192.168.178.1', '张三', False, True],
             ['192.168.178.2', '安全客户端', '192.168.178.2', '张三', True, True],
             ['192.168.178.3', '安全客户端', '发斯蒂芬斯蒂芬', '张三', False, True],
             ['192.168.178.4', '防火墙', '192.168.178.4', '张三', True, True],
             ['192.168.178.5', '防火墙', '192.168.178.5', '李四', True, True],
             ['192.168.178.6', '防火墙', '法法', '李四', False, True],
             ['192.168.178.7', '防火墙', '192.168.178.7', '李四', True, True],
             ['192.168.178.8', '交换机', '撒阿发发', '王五', False, True],
             ['192.168.178.9', '交换机', '192.168.178.9', '张三', True, True],
             ['192.168.178.10', '异常行为', '192.168.178.10', '王五', True, True],
             ['192.168.178.11', '异常行为', '按时发发发', '张三', False, True],
             ['192.168.178.12', '异常行为', '192.168.178.12', '王五', True, True],
             ['192.168.178.13', '异常行为', '啊啊是发发', '张三', True, True],
             ['192.168.178.14', '安全客户端', '192.168.178.14', '张三', True, True],
             ['192.168.178.15', '交换机', '192.168.178.15', '王五', False, True],
             ['192.168.178.16', '交换机', '啊发发发生发发', '李四', True, True],
             ['192.168.178.17', '安全客户端', '192.168.178.17', '王五', False, True]]
    tmp_list = analysis_data(datas)
    # print(tmp_list)
    str_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    write_excel("安全管理员对应设备类型统计%s.xls" % str_time, tmp_list, datas)









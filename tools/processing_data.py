# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@version : 2.7.14
@file : processingdata.py
@time : 2021/01/08 23:20:36
@func : 对数据进行统计，并用xlwt包写入excel(生产环境安装pandas依赖的包太多，环境变更麻烦)
"""
import datetime
import xlwt


def set_Style(name, size, color, borders_size, color_fore, blod=False):
    style = xlwt.XFStyle()  # 初始化样式
    # 字体
    font = xlwt.Font()
    font.name = name
    font.height = 20 * size  # 字号
    font.bold = blod  # 加粗
    font.colour_index = color  # 默认：0x7FFF 黑色：0x08
    style.font = font
    # 居中
    alignment = xlwt.Alignment()  # 居中
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment
    # 边框
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = borders_size  # 自定义：1：细线；2：中细线；3：虚线；4：点线
    style.borders = borders
    # 背景颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # 设置背景颜色的模式(NO_PATTERN; SOLID_PATTERN)
    pattern.pattern_fore_colour = color_fore  # 默认：无色：0x7FFF；黄色：0x0D；蓝色：0x0C
    style.pattern = pattern

    return style


def write_excel(file_path, data1, data2):
    f = xlwt.Workbook(encoding='utf-8')
    # 写入sheet1
    sheet1 = f.add_sheet(u"统计数据", cell_overwrite_ok=True)

    # 设置统一样式
    style = set_Style('宋体', 12, 0x08, 2, 0x7FFF, blod=False)
    title1 = ["管理员", "总计设备数", "设备类型", "分类设备数", "netbase监控率", "Wup监控率"]

    # 设置列宽
    sheet_list = ['first_' + str(i) for i in range(len(title1))]
    for i in range(len(title1)):
        sheet_list[i] = sheet1.col(i)
    for i in range(len(title1)):
        if i == 2:
            sheet_list[i].width = 256 * 40
        else:
            sheet_list[i].width = 256 * 20

    for j in range(len(title1)):
        sheet1.write(0, j, title1[j], style=style)
    i = 1
    dict_list = []
    tmp_dict = {}
    for data in data1:
        device_kinds = data[-1]
        data = data[:-1]
        keys_list = [list(m.keys())[0] for m in dict_list]
        if data[0] not in keys_list:
            tmp_dict[data[0]] = (data[1], device_kinds)
            dict_list.append(tmp_dict)
            tmp_dict = {}
        for j in range(len(data)):
            sheet1.write(i, j, data[j], style=style)  # 往单元格写入数据
        i += 1
    step0 = 0
    for k in dict_list:
        name = list(k.keys())[0]
        number, step = list(k.values())[0]
        sheet1.write_merge(step0 + 1, step0 + step, 0, 0, name, style=style)  # 合并单元格
        sheet1.write_merge(step0 + 1, step0 + step, 1, 1, number, style=style)
        step0 += step
    f.save(file_path)

    # 写入sheet2
    sheet2 = f.add_sheet(u"设备详细信息", cell_overwrite_ok=True)
    title2 = ["管理IP", "监控类型", "主机名", "设备管理员", "netbase监控", "Wup监控"]
    # 设置列宽
    sheet_list = ['first_' + str(i) for i in range(len(title2))]
    for i in range(len(title2)):
        sheet_list[i] = sheet2.col(i)
    for i in range(len(title2)):
        if i == 2:
            sheet_list[i].width = 256 * 40
        else:
            sheet_list[i].width = 256 * 20
    data2.insert(0, title2)
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
        for device_type_key in device_type_keys:
            items = device_type[device_type_key]
            items_num = len(items)
            netbase_true_num = 0
            whatsup_true_num = 0
            # todo 有可能存在bug
            # True if item[-2].lower() == "true" else False
            for item in items:
                if item[-2]:
                    netbase_true_num += 1
                if item[-1]:
                    whatsup_true_num += 1
            netbse_rate = '{:.2f}%'.format(float(netbase_true_num) / float(items_num) * 100)
            wup_rate = '{:.2f}%'.format(float(whatsup_true_num) / float(items_num) * 100)
            tmp_list.append([k, sum_devices, device_type_key, items_num, netbse_rate, wup_rate, davice_counts])
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
    # 统计数据
    tmp_list = analysis_data(datas)
    # 写入excel
    str_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    write_excel(u"安全管理员对应设备类型统计%s.xls" % str_time, tmp_list, datas)

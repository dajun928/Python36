# -*- coding: utf-8 -*-
import pandas as pd
import datetime

str_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
writer = pd.ExcelWriter("安全管理员对应设备类型统计%s.xls" % str_time)
data = pd.read_excel(r"D:\PycharmProjects\mywork\tools\test.xls")

tmp_list = []
for name, group in data.groupby([u"设备管理员", u"监控类型"]):
    counts = group[u"管理IP"].count()
    try:
        numerator1 = group["netbase监控"].value_counts()[True]
    except:
        numerator1 = 0
    try:
        numerator2 = group["Whatsup监控"].value_counts()[True]
    except:
        numerator2 = 0
    denominator = group['管理IP'].count()
    netbse_rate = '{:.2f}%'.format(numerator1 / denominator * 100)
    wup_rate = '{:.2f}%'.format(numerator2 / denominator * 100)
    tmp_list.append([name[0], name[1], counts, netbse_rate, netbse_rate])

data1 = data.groupby([u"设备管理员"], as_index=False)[u"管理IP"].count()
data2 = pd.DataFrame(tmp_list, columns=["设备管理员", "设备类型", "分类设备数", "netbase监控率", "Wup监控率"])

res_data = pd.merge(data1, data2, on=u"设备管理员")
res_data.rename(columns=({'设备管理员': '管理员', '管理IP': '总计设备数'}), inplace=True)
res_data.index = res_data.set_index(['管理员', '总计设备数', '设备类型']).index
res = res_data.iloc[:, 3:]

data_list = data.values.tolist()
print(data_list)
res1 = pd.DataFrame(data_list, columns=["管理IP", "监控类型", "主机名", "设备管理员", "netbase监控", "WhatsUp监控"])
res1.set_index(["管理IP"], inplace=True)


# res.to_excel(writer, sheet_name='统计数据')
# res1.to_excel(writer, sheet_name='设备详细信息')
# writer.save()
# writer.close()

import re

with open('./素材/中信证券资管产品_中信证券 CITIC Securities.html', 'r', encoding='UTF-8') as f:
    data = f.read()

# print(data)

'''
<span class="th3" value="R2-中低风险">R2-中低风险</span>
<span class="th3" value="R4-中高风险">R4-中高风险</span>
'''
print(re.findall('<span class="th3" value=".*?">(.*?)</span>', data, re.S))

# 练习
# 将产品名称管理人  风险评级 认购金额 起点公示  信息  全部抓到
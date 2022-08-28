import re
f = open('../素材/中信证券资管产品_中信证券 CITIC Securities.html', 'r', encoding='UTF-8')
data = f.read()
#第一次 抓取 包含 股票代码信息的数据
data = re.findall('<span class="th2" value="\w+">(.*?)</span>', data, re.S)
data = re.findall('<span class="th3" value=".+?">(.*?)</span>', data, re.S)
print(data)

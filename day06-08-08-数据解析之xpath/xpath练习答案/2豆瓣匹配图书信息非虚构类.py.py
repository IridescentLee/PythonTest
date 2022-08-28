from lxml import etree
# 实例化
tree = etree.HTML(open('../素材/豆瓣.html', 'r', encoding='UTF-8').read())
# print(tree)
'''
需求
1. 抓取封面
2. 抓取标题
3. 抓取简介
'''
# 抓取非虚构类
# cover-col-4 pl20 clearfix
res = tree.xpath('//ul[@class="cover-col-4 pl20 clearfix"]/li')
print(etree.tostring(res[-1], encoding='UTF-8').decode('UTF-8'))

# 匹配封面
print(res[0].xpath('./a/img')[0])
print(etree.tostring(res[0].xpath('./a/img')[0], encoding='UTF-8').decode('UTF-8'))

# 2. 抓取标题
print(res[0].xpath('.//h2/a/text()')[0])

# 3. 抓取简介
print(res[0].xpath('.//p[@class="color-gray"]/text() | .//div[@class="detail-frame"]/p[3]/text()'))

from lxml import etree

tree = etree.HTML(open('./素材/匹配天气.html', 'r', encoding='UTF-8').read())
# print(tree)
# 匹配当前的第一个table
# res = tree.xpath('/html/body/div[4]/div[2]/div/div/div[2]/div[1]/div[1]/table')
# 匹配当前出现的所有的天气的table
res = tree.xpath('//table')
# print(res)
for t in res:
    # 去除头俩个的标题行
    tr = t.xpath('./tr')[2:]
    # print(t)
    for r in tr:
        print(r.xpath('./td//text()'))
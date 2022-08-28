from lxml import etree
# 实例化
tree = etree.HTML(open('../素材/豆瓣.html', 'r', encoding='UTF-8').read())
'''
需求
1. 抓取封面
2. 抓取标题
3. 抓取简介
'''
# 抓取非虚构类
# cover-col-4 pl20 clearfix
res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li | //ul[@class="cover-col-4 pl20 clearfix"]/li')

for li in res:
    # 匹配封面
    img = etree.tostring(li.xpath('./a/img')[0], encoding='UTF-8').decode('UTF-8')

    # 2. 抓取标题
    title = li.xpath('.//h2/a/text()')[0]

    # 3. 抓取简介
    introduction = li.xpath('.//p[@class="color-gray"]/text() | .//p[@class="detail"]/text() | .//div[@class="detail-frame"]/p[3]/text()')
    introduction = ''.join(introduction).strip()
    print(img, title, introduction)

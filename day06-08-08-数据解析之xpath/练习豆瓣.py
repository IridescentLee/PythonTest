from lxml import etree

f = open('./素材/豆瓣.html', mode='r', encoding='utf-8')

douban_content = f.read()
f.close()

douban_tree = etree.HTML(douban_content)

res = douban_tree.xpath('//ul[@class="cover-col-4 clearfix"]/li')

dic = {}
for e in res:
    image = e.xpath('./a/img/@src')[0]
    print(image)
    name = e.xpath('./div/h2/a/text()')[0]
    print(name)
    detail = e.xpath('./div/p[@class="detail"]/text()')[0].strip()
    print(detail)
    dic[name] = e.xpath('./a/img/@src')
    dic[name].append(detail)

print(dic)



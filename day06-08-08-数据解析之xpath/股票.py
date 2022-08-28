from lxml import etree

f = open('./素材/股票.html', mode='r', encoding='utf-8')
content = f.read()
f.close()

res = etree.HTML(content)
# print(res)

tree = res.xpath('//table[@id="table1"]//tr')[1:-1]
# print(tree)
dic = {}
for e in tree:
    num1 = e.xpath('./td/a/text()')
    print(num1)
    num2 = e.xpath('./td[@class="align_right "]/text()')
    print(num2)
    num1.extend(num2)
    dic[num1[0]] = num1[1:]

print(dic)


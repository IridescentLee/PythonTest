from lxml import etree

tree = etree.HTML(open('./素材/大学排名.html', 'r', encoding='UTF-8').read())
# print(tree)
# res = tree.xpath('//table[@class="sticky-enabled tableheader-processed sticky-table"]//tr')

# res = tree.xpath('//*[@id="block-system-main"]/div/table[2]')
res = tree.xpath('//*[@id="block-system-main"]/div/table[2]//tr')
# print(res)
for tr in res:
    print(tr.xpath('./td//text()'))
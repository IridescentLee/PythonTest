from lxml import etree
# 本地HTML文件
# parser = etree.HTMLParser(encoding="utf-8")
# tree = etree.parse('./素材/豆瓣.html', parser=parser)
# print(tree)

# 网络html字符串/本地的html文件(建议)
f = open('./素材/豆瓣.html', 'r', encoding='UTF-8')
content = f.read()
f.close()
# print(content)
tree = etree.HTML(content)
print(tree)


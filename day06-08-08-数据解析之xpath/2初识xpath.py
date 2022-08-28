from lxml import etree
# 实例化tree对象
tree = etree.HTML(open('./素材/豆瓣.html', 'r', encoding='UTF-8').read())
# print(tree)
# xpath('语法')
# 找超链接  登录 注册
# res = tree.xpath('/html/body/div/div/div/a')
# print(res)
# 节点对象转换成字符串输出
# print(etree.tostring(res[0],encoding='UTF-8').decode('UTF-8'))
# print(etree.tostring(res[1],encoding='UTF-8').decode('UTF-8'))
# print(etree.tostring(res[2],encoding='UTF-8').decode('UTF-8'))
# for e in res:
#     print(etree.tostring(e,encoding='UTF-8').decode('UTF-8'))

# 超链接 a  获取所有当前页面中的a  无论在哪个位置
# res = tree.xpath('//a')
# res = tree.xpath('//img')  # 获取页面中所有的img标签
# print(res)
# for e in res:
#     print(etree.tostring(e,encoding='UTF-8').decode('UTF-8'))


# 文本内容获取
# res = tree.xpath('/html/body/div/div/div/a')
# res = tree.xpath('/html/body/div/div/div/a/text()')  # 获取a中的文本
# res = tree.xpath('//a/text()')  # 获取a中的文本
# print(res)

# 获取登陆注册  不要豆瓣
# xpath语法中 获取从1开始
# res = tree.xpath('/html/body/div/div/div[1]/a/text()')
# 下载豆瓣客户端
# res = tree.xpath('/html/body/div/div/div[2]/a/text()')
# print(res)

# / 和 // 在下一次路径中的使用
# res = tree.xpath('/html/body/div/div/div/a')
# 进行二次匹配
# print(res[0])
# ./ 代表从当前节点对象往下继续匹配
# print(res[0].xpath('./text()'))  # 等同于  tree.xpath('/html/body/div/div/div/a/text()')
# print(res[0].xpath('/text()'))  # 从跟下开始匹配 和 前面的res[0] 一点关系都没有
# print(res[0].xpath('/html/body/div/div/div/a'))
# print(res[0].xpath('//text()'))  # 和 tree.xpath('//text()')

# 路径中混合使用/ 和 //
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]')
# print(res)
# print(etree.tostring(res[0],encoding='UTF-8').decode('UTF-8'))
# 想获取虚构类里所有的li内的文本内容
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li//text()')
# 获取虚构类li里所有的img标签
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li//img')
# for e in res:
#     print(etree.tostring(e,encoding='UTF-8').decode('UTF-8'))
# 获取虚构类li里所有的img标签的src属性值
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li//img/@src')
# print(res)
# 数量限制
# 想要第一个li  现在讲的xpath语法 下面的完全可以使用列表切片替代
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[1]')
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li')[0]
# 获取最后一个li
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[last()]')
# 获取倒数第二个li
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[last()-1]')
# 获取前俩个li
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[position()<3]')
# print(res)
# print(etree.tostring(res[0],encoding='UTF-8').decode('UTF-8'))
# print(etree.tostring(res[1],encoding='UTF-8').decode('UTF-8'))

# @attr 属性
# res = tree.xpath('//img')  # 获取img标签
# res = tree.xpath('//img/@src')  # 获取img的src
# res = tree.xpath('//@src')  # 获取所有的src属性
# res = tree.xpath('//img[@src]')  # 获取所有具有src属性的img标签
# print(res)

# 判断
# res = tree.xpath('//a[@class]')  # 获取所有带有class属性的a
# res = tree.xpath('//a[@class="cover"]')  #  所有class属性值为"cover"的超链接
# res = tree.xpath('//a[@price>"10"]')  #  获取price属性大于10的标签
# res = tree.xpath('//a[@price>="10"]')  #  获取price属性大于等于10的标签
# res = tree.xpath('//a[@price<"10"]')  #  获取price属性小于10的标签
# res = tree.xpath('//a[@price<="10"]')  #  获取price属性小于10的标签
# res = tree.xpath('//a[@price!="10"]')  #  获取price属性小于10的标签
# print(res)
# for e in res:
#     print(etree.tostring(e,encoding='UTF-8').decode('UTF-8'))

# 通配符*的使用 一般只有在copy xpath的时候会出现* 自己写的时候很少用
# res = tree.xpath('//*[@class]')  # 获取所有具有class属性的标签（无论什么标签）
# res = tree.xpath('//*[@price]')

# // node()
# res = tree.xpath('//node()')
# for e in res:
#     print(etree.tostring(e,encoding='UTF-8').decode('UTF-8'))


# 匹配class为div1或class为div2的标签
# res = tree.xpath('//div[@class="div1"] | //div[@class="div2"]')
# and 匹配div标签 其中class值为div1  并且 id值为test1
# res = tree.xpath('//div[@class="div1" and @id="test1"]')
# res = tree.xpath('//div[@class="div1" and @id="test1"]/text()')

# 包含关系
# div标签中 class属性值包含div1的节点
# res = tree.xpath('//div[contains(@class, "div1")]//text()')
# 以...开头 查找div标签中class属性值以div开头的节点内容
res = tree.xpath('//div[starts-with(@class, "div")]//text()')
print(res)


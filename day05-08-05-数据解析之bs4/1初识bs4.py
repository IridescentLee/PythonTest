from bs4 import BeautifulSoup
# 实例化soup对象
# soup = BeautifulSoup('html文本内容', 'lxml')
soup = BeautifulSoup(open('./素材/豆瓣.html', 'r', encoding='UTF-8'), 'lxml')
# print(type(soup))
# 获取div标签
# print(soup.div)
# print(soup.a)
# print(soup.p)
# 获取属性
# print(soup.div.attrs)
# print(soup.div.attrs['id'])
# print(soup.div.attrs['class'])
# print(soup.div['id'])
# print(soup.div['class'])

# 获取文本内容
# print(soup.title)
# print(soup.title.string)
# print(soup.title.text)
# print(soup.title.get_text())


# find方法 只拿到一条
# print(soup.find('div'))  #  等同于 soup.div
# print(soup.find('div', attrs={'id':"db-global-nav"}))  # 查找div标签 并且id属性值为db-global-nav
# 条件筛选
# print(soup.find('div', attrs={'id':"db-global-nav", 'class': "global-nav"}))
# print(soup.find('div', id="db-global-nav"))
# print(soup.find('div', class_="global-nav"))  # 需要处理

# 小练习
# 获取img的src
# print(soup.find('a', class_="cover"))
# print(soup.find('a', class_="cover").img)
# print(soup.find('a', class_="cover").img['src'])
# print(soup.find('a', class_="cover").img.attrs)  # 获取img的所有属性值

# 获取文本内容
# print(soup.find('div', class_="article").string)  # 为None
# print(soup.find('div', class_="article").contents)  # 匹配所有返回列表
# print(soup.find('div', class_="article").text)  # 获取当前div标签里的所有文本内容
# print(soup.find('div', class_="article").get_text())  # 等同于上方
# print(soup.find('div', class_="article").strings)  # 返回生成器
# print(next(soup.find('div', class_="article").strings))  # 返回生成器
# print(list(soup.find('div', class_="article").strings))  # 返回生成器 匹配所有包含空白文本
# print(soup.find('div', class_="article").stripped_strings)  # 返回生成器 匹配所有
# print(list(soup.find('div', class_="article").stripped_strings))  # 返回生成器 会去除空白文本

# 获取简介
# print(soup.find('p', class_="color-gray"))
# print(soup.find('p', class_="color-gray").string)
# print(repr(soup.find('p', class_="color-gray").string))
# print(soup.find('p', class_="color-gray").contents) # 返回节点 以列表形式
# print(list(soup.find('p', class_="color-gray").strings))
# print(list(soup.find('p', class_="color-gray").stripped_strings))
# print(soup.find('p', class_="color-gray").prettify())  # 美化匹配结果
# print(soup.find('p', class_="color-gray"))  # 美化匹配结果


# 匹配所有
# print(soup.find_all('a'))
# print(soup.find_all('a', class_="cover"))
# print(soup.find_all('img'))  # 获取所有的图片标签
# 获取俩个图片
# print(soup.find_all('img')[0:2])  # 获取俩个图片标签
# print(soup.find_all('img', limit=2))  # 获取俩个图片标签
# print(soup.find_all(['a', 'title']))  # 获取title和img标签


# select 选择器
# print(soup.select('a'))  # 查找 HTML a标签选择器
# print(soup.select('.color-gray'))  # 查找 class属性为color-gray的标签
# print(soup.select('ul[class="cover-col-4 clearfix"]'))  # 属性选择器css3 ul选择器中 class属性值为cover-col-4 clearfix的节点标签

# 获取ul的直接子元素li
# print(soup.select('ul[class="cover-col-4 clearfix"]>li'))
# 获取ul的直接子元素li的直接子元素a
# print(soup.select('ul[class="cover-col-4 clearfix"]>li>a'))
# 获取ul的直接子元素li的直接子元素a的直接子元素img
# print(soup.select('ul[class="cover-col-4 clearfix"]>li>a>img'))
# 获取ul里面的img标签
# print(soup.select('ul[class="cover-col-4 clearfix"] img'))
# print(soup.select('#db-global-nav'))  # 获取id属性值为#db-global-nav的标签

img = soup.select('ul[class="cover-col-4 clearfix"] img')
for i in img:
    print(i['src'])

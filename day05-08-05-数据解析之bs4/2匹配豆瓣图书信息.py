from bs4 import BeautifulSoup
soup = BeautifulSoup(open('./素材/豆瓣.html', 'r', encoding='UTF-8'), 'lxml')
# print(soup)

# 获取标题 评分 简介等信息
div_list = soup.find_all('div', class_='detail-frame')
# print(con)
for d in div_list:
    # 获取标题
    # title = d.a.string
    # 获取评分
    # print(d.find('span', class_="font-small color-lightgray").string)
    # 获取简介
    # print(d.find('p', class_='color-gray').string)
    # print(d.find('p', class_='detail').string)
    print(d.find_all('p')[-1].string)
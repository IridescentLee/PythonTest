from bs4 import BeautifulSoup
soup = BeautifulSoup(open('素材/广州二手房.html', 'r', encoding='UTF-8'), 'lxml')
# print(soup)
div_list = soup.find_all('div', class_="house-item house-itemB clearfix")
for d in div_list:
    # print(d)
    # print(list(d.stripped_strings))
    # print(d.select('.cBlueB')[0].text)
    # print(d.select('.house-name')[0].text)
    print(d.select('.house-txt')[0].text)
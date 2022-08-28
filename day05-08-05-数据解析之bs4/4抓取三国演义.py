from bs4 import BeautifulSoup
with open('素材/三国演义.html', 'r', encoding='UTF-8') as f:
    data = f.read()
soup = BeautifulSoup(data, 'lxml')
a_list = soup.select('.book-mulu>ul>li>a')
# print(a_list)
for a in a_list:
    href = a['href']
    title = a.text
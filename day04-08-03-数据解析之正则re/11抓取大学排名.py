import re

with open('./素材/大学排名.html', 'r', encoding='UTF-8') as f:
    data = f.read()

# print(data)
data = re.findall('<tr class="\w+"><td><center>(\d+)</center></td><td><center>(\d+)</center></td><td><a href=".*?" target="_blank">(.*?)</a></td><td><a href=".*?"><img src=".*?"></a></td><td><center><img alt="bandera" src=".*?"></center></td><td><center>(\d+)</center></td><td><center>(\d+)</center></td><td><center>(\d+)</center></td> </tr>', data, re.S)
for line in data:
    print(line)